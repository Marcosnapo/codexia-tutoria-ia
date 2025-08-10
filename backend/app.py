import os
import psycopg2
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import json

# Cargar variables de entorno del archivo .env
load_dotenv()

# Almacena el historial de chat en memoria, esto es crucial
# para mantener la coherencia de la conversación.
chat_history = []

# Inicialización de la aplicación y CORS
app = Flask(__name__)
# Solución de CORS: Habilita CORS para todas las rutas.
CORS(app)

# Configurar API de Gemini con la clave de API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Usar el modelo que confirmamos que funciona
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

# --- Funciones de la base de datos ---
def get_db_connection():
    """Establece una conexión con la base de datos PostgreSQL."""
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        return conn
    except Exception as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None

def create_table_if_not_exists():
    """Crea la tabla 'sessions' si no existe."""
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id SERIAL PRIMARY KEY,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                topic TEXT,
                summary TEXT,
                weak_points TEXT
            );
        """)
        conn.commit()
        cur.close()
        conn.close()

# Asegurar que la tabla se crea al iniciar el servidor
create_table_if_not_exists()

# --- Endpoints de la API ---
@app.route("/start-session", methods=["POST"])
def start_session():
    """
    Inicia una nueva sesión de chat.
    Recupera el historial de la última sesión de la base de datos y
    genera un mensaje de bienvenida contextualizado.
    """
    global chat_history
    chat_history = []  # Limpiar el historial para una nueva sesión

    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Error de conexión a la base de datos.'}), 500
        
    cur = conn.cursor()
    cur.execute("SELECT summary, weak_points FROM sessions ORDER BY date DESC LIMIT 1;")
    last_session = cur.fetchone()
    cur.close()
    conn.close()

    # Definir el rol del tutor
    prompt = """
    Eres un tutor de programación experto llamado "Codexia". Tu objetivo es ayudar al estudiante a aprender Python.
    Tu estilo es socrático y paciente. No des la respuesta directamente, guíalo con preguntas.
    Tu misión es generar el mensaje de bienvenida y contextualizar la sesión.
    """
    
    if last_session:
        summary, weak_points = last_session
        prompt += f"\nEl estudiante tiene un historial. La última sesión se centró en: {summary}. Sus puntos débiles eran: {weak_points}. Debes comenzar la sesión repasando brevemente estos temas y luego introducir un nuevo concepto de forma gradual."
    else:
        prompt += "\nEs la primera vez que el estudiante interactúa contigo. Preséntate y pregunta qué tema de Python le gustaría aprender."

    try:
        response = model.generate_content(prompt)
        welcome_message = response.text
        
        # Guardar el mensaje de bienvenida en el historial de chat
        chat_history.append({'role': 'model', 'parts': [welcome_message]})
        
        return jsonify({"message": welcome_message})

    except Exception as e:
        print(f"Error al generar el mensaje de bienvenida: {e}")
        return jsonify({'error': 'Ocurrió un error en el servidor al iniciar la sesión.'}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """
    Maneja la conversación con el modelo de Gemini, manteniendo el historial.
    """
    global chat_history
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({'error': 'No se proporcionó un mensaje'}), 400

    try:
        # Añadir el mensaje del usuario al historial
        chat_history.append({'role': 'user', 'parts': [user_message]})

        # Generar la respuesta del modelo usando el historial completo
        response = model.generate_content(chat_history)
        ai_response = response.text

        # Añadir la respuesta de la IA al historial
        chat_history.append({'role': 'model', 'parts': [ai_response]})

        return jsonify({'response': ai_response})

    except Exception as e:
        print(f"Error al chatear con la IA: {e}")
        return jsonify({'error': 'Ocurrió un error en el servidor.'}), 500

@app.route("/end-session", methods=["POST"])
def end_session():
    """
    Finaliza la sesión, analiza la conversación y guarda un resumen en la base de datos.
    La respuesta de Gemini se solicita en formato JSON.
    """
    global chat_history
    
    # Unir el historial de chat en una cadena de texto para el análisis
    conversation_text = ""
    for message in chat_history:
        role = "Estudiante" if message['role'] == 'user' else "Codexia"
        conversation_text += f"{role}: {message['parts'][0]}\n"

    # El prompt ahora pide a Gemini que devuelva la respuesta en JSON
    prompt = f"""
    Analiza la siguiente conversación entre un tutor y un estudiante.
    1. Identifica el tema principal de la sesión.
    2. Resume los conceptos cubiertos.
    3. Identifica los puntos débiles o áreas de confusión del estudiante.
    4. Proporciona el resumen y los puntos débiles en formato JSON con las claves "topic", "summary", y "weak_points".

    Conversación:
    {conversation_text}
    """
    
    try:
        # Llamada a la API solicitando una respuesta en formato JSON
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        
        # Parsear la respuesta JSON
        session_info = json.loads(response.text)
        
        # Conexión a la base de datos y guardado de la información
        conn = get_db_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO sessions (topic, summary, weak_points) VALUES (%s, %s, %s)",
                        (session_info.get("topic"), session_info.get("summary"), session_info.get("weak_points")))
            conn.commit()
            cur.close()
            conn.close()
            
        chat_history = []
        return jsonify({"message": "Sesión finalizada y guardada con éxito."})
        
    except Exception as e:
        print(f"Error al analizar o guardar la sesión: {e}")
        chat_history = []
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
