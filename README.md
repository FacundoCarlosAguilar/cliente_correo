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
├── .env # SQL remoto
└── README.md # Este archivo

### Documentación de Endpoints: (http://localhost:8050/docs)

# 1.Ingresar a terminal 

# 2. Clonar repositorio
git clone https://github.com/FacundoCarlosAguilar/cliente_correo.git
cd cliente_correo

# 3. Crear entorno virtual

    --creamos el entorno virtual--

    python -m venv venv

    --activamos el entorno virtual--

    venv\Scripts\activate  

# si da el caso de que no funciona y da [WinError 2] 
# descargar todo directamente de forma global 
# con el paso 4 en forma manual


# 4. Instalar dependencias

--De forma automática--
pip install -r requirements.txt

--De forma manual--

pip install fastapi uvicorn pydantic python-dotenv mysql-connector-python

# 5. Ejecutar la API levantando el servidor
python -m uvicorn app.main:app --reload --port 8050

# 6. para acceder a la documentacion interactiva pegar en el buscador del navegador de preferencia: -> http://localhost:8050/docs <- 

////////////////////////////////////////////////////////////
# Para usar metodos GET y POST en Postman 
 
# 1. Abrir postman en y si esta habilitado por el dueño del servicio y se cuenta con la API activa en el servidor, buscar en lado izquierdo la casilla colections 

# 2. desplegar carpeta "Endpoints", y desplegar sus aderidos "get" y "post"

# 3. por un lado GET nos permite consultar valores y por otro POST nos permite ingresarlos

# para listar o ver valores ingresados (por metodo GET):
| 
|-> Método: Seleccioná GET en el desplegable.
|
|-> URL: http://localhost:8050/contactos/todos
|
|-> Acción: Presioná el botón Send.
|
|-> Resultado esperado: Un código 200 OK y una lista de 
|  contactos en formato JSON (o una lista vacía [] si no hay 
|  nadie cargado).

# para agregar un contacto (por metodo POST):
|-> Método: Seleccioná POST.
|
|-> URL: http://localhost:8050/contactos/agregar
|
|-> Configuración del Body (Cuerpo):
|
|-> Hacé clic en la pestaña Body (debajo de la URL).
|
|-> Seleccioná la opción raw.
|
|-> A la derecha, donde dice "Text", cambialo por JSON.
|
|-> EJEMPLO
|    {
|        "id": 10,
|        "nombre": "Ayax",
|        "apellido": "FE",
|        "email": "AyaxDEFE@gmail.com"
|    },
|
|-> Acción: Presioná Send.
|
|-> Resultado esperado: Un mensaje de éxito y el objeto 
|   creado con su ID.

# Para enviar un correo (por metodo POST):
|
|-> Método: Seleccioná POST.
|
|-> URL: http://localhost:8050/enviar_correo
|
|-> Configuración del Body (Cuerpo):
|
|-> Hacé clic en la pestaña Body (debajo de la URL).
|
|-> Seleccioná la opción raw.
|
|-> EJEMPLO: 
|   {
|    "remitente_id": 1,
|    "destinatario_id": 2,
|    "asunto": "Entrega de Laboratorio",
|    "contenido": "Hola, adjunto el código del cliente de 
|    correo."
|   }

