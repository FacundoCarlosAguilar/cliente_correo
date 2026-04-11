import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Esto carga las variables de tu archivo .env de forma segura
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE')
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if conn:
        print("Conexión a MySQL exitosa")
        conn.close()
    else:
        print("Error: Revisar la configuración de MySQL")