Descripción General
Este proyecto es una aplicación web estilo blog desarrollada con Python y el framework Django. La plataforma permite a los usuarios registrar y autenticarse para crear, editar y eliminar sus propias publicaciones (Posts). Además, incluye un sistema completo de mensajería privada para que los usuarios puedan comunicarse entre sí.
________________________________________
⚙️ Tecnologías y Características Implementadas
Tecnologías Principales
•	Lenguaje: Python 3.11+
•	Framework: Django 5.x
•	Base de Datos: SQLite3 (por defecto en desarrollo)
•	Frontend: HTML, CSS (Bootstrap 5.3), JavaScript
Requisitos Base Cumplidos
Requisito	Implementación
Modelos Principales	Post (Blog) y Mensaje (Mensajería).
Vistas y Patrones	Uso de 2+ Clases Basadas en Vista (CBV) (ej. PostCreateView, MensajeCreateView).
Mixins y Decoradores	Uso de LoginRequiredMixin (en CBVs) y @login_required (en FVB de la Bandeja de Entrada).
CRUD Completo	Vistas de Creación, Listado, Detalle, Edición y Borrado de Posts.
Autenticación/Perfil	Aplicación accounts para Registro, Login, Logout, Vista de Perfil y Edición de Perfil.
Texto Enriquecido	Uso de CKEditor en el campo contenido del modelo Post.
Herencia de Templates	Plantilla base.html con barra de navegación (NavBar) heredada por todas las demás.
Rutas Estáticas	Vistas de inicio (/) y "Acerca de Mí" (/acerca-de/).
Mensajería	Aplicación mensajeria que permite enviar y recibir mensajes privados.
________________________________________
🛠️ Instrucciones de Instalación y Ejecución
Sigue estos pasos para poner en marcha el proyecto en tu máquina local.
1. Clonar el Repositorio
Bash
git clone https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories
cd primera-pagina
2. Crear y Activar el Entorno Virtual
Bash
# Crear entorno virtual (si no existe)
python -m venv venv

# Activar el entorno virtual (Windows)
.\venv\Scripts\activate
# Activar el entorno virtual (Linux/macOS)
source venv/bin/activate
3. Instalar Dependencias
Instala todas las librerías necesarias listadas en requirements.txt:
Bash
pip install -r requirements.txt
4. Migraciones de Base de Datos
Aplica las migraciones iniciales para crear las tablas de los modelos:
Bash
python manage.py makemigrations
python manage.py migrate
5. Crear Superusuario (Opcional, pero recomendado)
Necesitas un superusuario para acceder al panel de administración de Django:
Bash
python manage.py createsuperuser
6. Ejecutar el Servidor
Inicia el servidor de desarrollo de Django:
Bash
python manage.py runserver
El proyecto estará accesible en tu navegador en http://127.0.0.1:8000/.
________________________________________
🗺️ Rutas Principales de la Aplicación
URL (Ruta)	Funcionalidad
/	Vista de Inicio (Home).
/acerca-de/	Vista "Acerca de Mí" (About).
/pages/	Listado de todos los Posts.
/pages/<int:pk>/	Detalle de un Post.
/pages/nuevo/	Creación de un nuevo Post (Requiere Login).
/accounts/register/	Registro de nuevos usuarios.
/accounts/login/	Inicio de Sesión.
/accounts/profile/	Perfil del usuario logueado.
/mensajeria/	Bandeja de Entrada de mensajes (Requiere Login).
/mensajeria/nuevo/	Enviar un nuevo mensaje (Requiere Login).
________________________________________
🚫 Notas de Entrega
•	No se incluye la Base de Datos: El archivo db.sqlite3 no está incluido en este repositorio gracias a la configuración de .gitignore.
•	Archivos de Medios (Imágenes): La carpeta media/ está excluida para no subir archivos pesados. Las imágenes del proyecto deben subirse en tiempo de ejecución.
________________________________________
¡Gracias por revisar el proyecto!

