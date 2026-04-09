import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'port': 3443,
    'user': 'root',
    'password': 'facundo111',
    'database': 'cliente_correo'
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