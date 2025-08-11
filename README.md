✨ Codexia: Tu Tutor de Programación Personal con IA ✨
¡Bienvenido a Codexia! 👋 Este es tu tutor de programación personal, impulsado por la increíble inteligencia artificial de Google Gemini. Piensa en él como un amigo que te ayuda a aprender Python de una manera socrática y súper contextualizada. La mejor parte es que el tutor recuerda tus conversaciones anteriores, identifica tus puntos débiles y adapta la charla para que tu aprendizaje sea más divertido y eficaz.

El proyecto está diseñado con una arquitectura de backend y frontend separada. ¡Esto lo hace modular y muy fácil de mantener! 😉

🚀 Características que te encantarán
Tutoría Contextualizada: Usamos un historial de tus sesiones (guardado en PostgreSQL) para que el tutor sepa exactamente dónde te quedaste y qué necesitas reforzar. ¡Nunca más te sentirás perdido!

Aprendizaje Socrático: El tutor no te dará las respuestas de inmediato. En cambio, te guiará con preguntas inteligentes para que descubras las soluciones por ti mismo. ¡Así el conocimiento se te queda grabado! 🧠

Seguimiento del Progreso: Cada sesión se resume y se guarda en una base de datos para que puedas ver tu progreso y los temas que has dominado. ¡Es como tu propio diario de aprendizaje!

Backend Robusto: Todo el poder de la IA reside en el backend, construido con Flask, PostgreSQL y la API de Google Gemini. ¡Es la magia detrás de la cortina!

Despliegue en la Nube: El backend de la aplicación vive en la nube, gracias a Render. Esto significa que puedes acceder a él desde cualquier lugar. ☁️

🛠️ Tecnologías Utilizadas
Backend:

Python 🐍: ¡El lenguaje principal de la magia!

Flask: Un micro-framework ligero y poderoso para nuestra API.

Gunicorn: Nuestro servidor de producción, el que mantiene todo funcionando sin problemas.

Google Gemini API: El cerebro de nuestro tutor. 🤖

psycopg2: Para hablar con nuestra base de datos PostgreSQL.

python-dotenv: Mantiene nuestras claves de API y configuraciones seguras. 🔐

Frontend:

HTML, CSS, JavaScript: La cara bonita de la aplicación, con la que interactúas todos los días. 🎨

Base de Datos:

PostgreSQL: Nuestro baúl de tesoros, donde guardamos el historial de tus sesiones. 🗄️

🎮 Cómo Usar la Aplicación
¡Es súper fácil! Solo necesitas abrir el archivo frontend/index.html en tu navegador. El frontend ya sabe cómo encontrar el backend en Render.

Abre el archivo index.html en tu navegador favorito.

Haz clic en el botón "Nueva Sesión" para empezar la aventura. 🚀

¡Empieza a chatear! El tutor de IA está listo para ayudarte con cualquier tema de Python.

💻 Configuración del Entorno Local (para desarrolladores)
Si eres un aventurero y quieres ejecutar el proyecto en tu propia máquina, sigue estos sencillos pasos:

⚙️ Prerrequisitos
Python 3.x

Git

PostgreSQL

📦 Instalación
Clona el repositorio:

git clone https://github.com/Marcosnapo/codexia-tutoria-ia.git
cd codexia-tutoria-ia

Crea y activa un entorno virtual para el backend:

cd backend
python3 -m venv venv
source venv/bin/activate

Instala las dependencias del backend:

pip install -r requirements.txt

Configura las variables de entorno:

Crea un archivo .env en la carpeta backend.

Añade tus claves y el enlace de la base de datos (puedes usar un servidor de PostgreSQL local o el mismo de Render):

GEMINI_API_KEY="TU_CLAVE_API_DE_GEMINI"
DATABASE_URL="postgres://tu_usuario:tu_contraseña@tu_host:tu_puerto/tu_db"

Ejecuta el servidor de Flask:

python3 app.py

Abre el Frontend:

Ve a la carpeta frontend.

Importante: Modifica index.html para que const backendUrl apunte a http://127.0.0.1:5000.

Abre el archivo index.html en tu navegador.

☁️ Despliegue en Render
El backend de este proyecto está listo para desplegarse en Render. La configuración que necesitas es:

Root Directory: backend

Build Command: pip install -r requirements.txt

Start Command: gunicorn --bind 0.0.0.0:$PORT app:app

Recuerda configurar las variables de entorno GEMINI_API_KEY y DATABASE_URL directamente en la sección Environment de Render.

🤝 Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de GitHub. ¡Nos encanta saber de ti!

📜 Licencia
Este proyecto está bajo la Licencia MIT. ¡Siéntete libre de usarlo!
