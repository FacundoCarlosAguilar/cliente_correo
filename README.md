# Cliente de Correo API

API para la materia de laboratorio de lenguajes de un correo electrónico básico similar a Outlook.

## Características

- Administración de una sola cuenta de correo
- Gestión de contactos
- Organización de correos en carpetas (Recibidos / Enviados)
- Persistencia de datos en **MySQL**
- API RESTful con **FastAPI**
- Documentación interactiva automática

## Tecnologías

| Tecnología | Versión   |
|------------|-----------|
| Python     | 3.14+     |
| FastAPI    | 0.135+    |
| MySQL      | 8.0 / 9.6 |
| Uvicorn    | 0.44+     |
| Pydantic   | 2.12+     |

## Estructura del Proyecto:

CLIENTE_CORREO/
│
├── app/
│ ├── init.py
│ ├── main.py # Endpoints de la API
│ ├── crud.py # Operaciones de base de datos
│ ├── database.py # Conexión a MySQL
│ └── schemas.py # Modelos
│
├── venv/ # Entorno virtual
├── requirements.txt # Dependencias
└── README.md # Este archivo


## Instalación y Configuración

### 1. Clonar o crear el proyecto

### 2. Crear el entorno virtual

python -m venv venv

# Activar en Windows:
venv\Scripts\activate

### 3. Instalar dependencias

pip install -r requirements.txt

### 4. TERMINAR EL README.md