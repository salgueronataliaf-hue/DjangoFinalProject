# Proyecto Final: Blog Dinámico y Mensajería (Django)

## Descripción General

Este proyecto es una aplicación web estilo blog desarrollada con Python y el framework Django. La plataforma permite a los usuarios registrar y autenticarse para crear, editar y eliminar sus propias publicaciones (Posts). Además, incluye un sistema completo de mensajería privada para que los usuarios puedan comunicarse entre sí.

El proyecto está estructurado en tres aplicaciones principales: `blog` (contenido), `accounts` (autenticación/perfil) y `mensajeria` (comunicación).

---

## ⚙️ Tecnologías y Características Implementadas

### Tecnologías Principales
* **Lenguaje:** Python 3.11+
* **Framework:** Django 5.x
* **Base de Datos:** SQLite3 (por defecto en desarrollo)
* **Frontend:** HTML, CSS (Bootstrap 5.3), JavaScript
* **Texto Enriquecido:** CKEditor (en el campo `contenido` del modelo `Post`).

### Requisitos Base Cumplidos
| Requisito | Implementación |
| :--- | :--- |
| **Modelos Principales** | `Post` (Blog) y `Mensaje` (Mensajería). |
| **Vistas y Patrones** | Uso de Clases Basadas en Vista (CBV) (ej. `PostCreateView`). |
| **Mixins y Decoradores** | Uso de `LoginRequiredMixin` y `@login_required` para proteger vistas. |
| **CRUD Completo** | Vistas de Creación, Listado, Detalle, Edición y Borrado de Posts. |
| **Autenticación/Perfil** | Aplicación `accounts` para Registro, Login, Logout, Vista de Perfil y Edición. |
| **Mensajería** | Aplicación `mensajeria` funcional para enviar y recibir mensajes privados. |
| **Herencia de Templates** | Plantilla `base.html` con barra de navegación heredada por todas las demás vistas. |
| **Rutas Estáticas** | Vistas de inicio (`/`) y "Acerca de Mí" (`/acerca-de/`). |

---

## 🛠️ Instrucciones de Instalación y Ejecución

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### 1. Clonar el Repositorio y Entorno Virtual
```bash
git clone [https://github.com/salgueronataliaf-hue/DjangoFinalProject.git](https://github.com/salgueronataliaf-hue/DjangoFinalProject.git)
cd DjangoFinalProject
# Crear y activar entorno (Windows)
python -m venv venv
.\venv\Scripts\activate