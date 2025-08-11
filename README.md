Codexia - Tu Tutor de Programación Personal con IA
Codexia es una aplicación de tutoría de programación impulsada por la inteligencia artificial de Google Gemini. Actúa como un tutor personal que te ayuda a aprender Python de forma socrática y contextualizada. El tutor recuerda tus sesiones anteriores, identifica tus puntos débiles y adapta la conversación para ofrecerte una experiencia de aprendizaje personalizada y efectiva.

El proyecto está diseñado con una arquitectura de backend y frontend separada, lo que permite un despliegue modular y flexible.

Características
Tutoría Contextualizada: Codexia utiliza el historial de tus sesiones anteriores (almacenado en PostgreSQL) para adaptar la conversación y repasar conceptos clave.

Aprendizaje Socrático: El tutor no te da las respuestas directamente, sino que te guía con preguntas para que descubras la solución por ti mismo.

Seguimiento del Progreso: Cada sesión se resume y se guarda en una base de datos para que puedas llevar un registro de los temas cubiertos y tus áreas de mejora.

Backend Robusto: Desarrollado con Flask, PostgreSQL y la API de Google Gemini.

Despliegue en la Nube: El backend de la aplicación está desplegado en la plataforma Render.

Tecnologías Utilizadas
Backend:

Python: Lenguaje de programación principal.

Flask: Micro-framework web para la API.

Gunicorn: Servidor de producción para el despliegue.

Google Gemini API: Para la generación de texto y la lógica del tutor.

psycopg2: Adaptador de PostgreSQL para Python.

python-dotenv: Para la gestión de variables de entorno.

Frontend:

HTML, CSS, JavaScript: Para la interfaz de usuario.

Base de Datos:

PostgreSQL: Para almacenar el historial de las sesiones.

Cómo Usar la Aplicación
Para usar Codexia, simplemente abre el archivo frontend/index.html en tu navegador. El frontend se conectará automáticamente al backend desplegado en Render.

Abre el archivo index.html en tu navegador.

Haz clic en el botón "Nueva Sesión" para empezar.

Comienza a chatear con el tutor de IA sobre cualquier tema de Python que quieras aprender.

Configuración del Entorno Local
Si deseas ejecutar el proyecto localmente para desarrollo, sigue estos pasos:

Prerrequisitos
Python 3.x

Git

PostgreSQL

Instalación
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

Crea un archivo llamado .env en la carpeta backend.

Añade tus claves y el enlace de la base de datos (puedes usar un servidor de PostgreSQL local o el mismo de Render):

GEMINI_API_KEY="TU_CLAVE_API_DE_GEMINI"
DATABASE_URL="postgres://tu_usuario:tu_contraseña@tu_host:tu_puerto/tu_db"

Ejecuta el servidor de Flask:

python3 app.py

Abre el Frontend:

Ve a la carpeta frontend.

Modifica el archivo index.html para que const backendUrl apunte a http://127.0.0.1:5000.

Abre el archivo index.html en tu navegador.

Despliegue en Render
El backend de este proyecto está desplegado en Render. La configuración para un despliegue continuo es la siguiente:

Root Directory: backend

Build Command: pip install -r requirements.txt

Start Command: gunicorn --bind 0.0.0.0:$PORT app:app

Las variables de entorno GEMINI_API_KEY y DATABASE_URL deben ser configuradas en la sección de Environment de Render.

Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de GitHub.

Licencia
Este proyecto está bajo la Licencia MIT.
