Proyecto Blog

## Nombre: Natalia Salguero

### Descripción del Proyecto
Este es un proyecto de desarrollo web basado en el framework **Django**, siguiendo la arquitectura **Modelo-Vista-Template (MVT)**. El objetivo fue implementar un sistema de blog básico capaz de manejar la carga de datos y realizar búsquedas.

### Estructura del Modelo (Base de Datos)
El proyecto utiliza la aplicación `blog` y define tres modelos principales, siguiendo las instrucciones del ejercicio:

1.  **Autor:** (Campos: `nombre`, `apellido`, `email`).
2.  **Categoria:** (Campo: `nombre`).
3.  **Post:** (Campos: `titulo`, `subtitulo`, `contenido`, `fecha_creacion`). Este modelo establece las relaciones:
    * `ForeignKey` con **Autor** (Un Post pertenece a un Autor).
    * `ForeignKey` con **Categoria** (Un Post pertenece a una Categoría).

### Funcionalidades Implementadas
El proyecto cumple con las siguientes funcionalidades requeridas:

1.  **Formularios de Carga:** Se crearon formularios basados en los modelos (`AutorForm`, `CategoriaForm`, `PostForm`) para ingresar datos a la base de datos a través de la interfaz web.
2.  **Búsqueda:** Se implementó una funcionalidad de búsqueda que permite filtrar los **Posts** por **título** (usando la consulta `icontains` para búsquedas parciales e insensibles a mayúsculas/minúsculas).
3.  **Herencia de Plantillas:** Se utilizó una plantilla base (`base.html`) para crear una estructura de navegación y estilos común (Bootstrap), que fue heredada por las plantillas hijas (`index.html`, `form_general.html`, `busqueda.html`).

---

### Cómo Ejecutar el Proyecto

1.  **Clonar el Repositorio:**
    ```bash
    git clone [URL_DE_TU_REPOSITORIO_EN_GITHUB]
    ```
2.  **Activar Ambiente Virtual e Instalar Dependencias:**
    ```bash
    cd TuPrimeraPaginaEstudiante
    .\venv\Scripts\activate  # Windows
    pip install django
    ```
3.  **Aplicar Migraciones:** (Para asegurar la creación de las tablas de Django)
    ```bash
    python manage.py migrate
    ```
4.  **Crear Superusuario:**
    ```bash
    python manage.py createsuperuser
    ```
5.  **Iniciar el Servidor:**
    ```bash
    python manage.py runserver
    ```
6.  Acceder a la URL: `http://127.0.0.1:8000/` y probar las funcionalidades de carga y búsqueda.
