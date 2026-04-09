import json
from app.database import get_db_connection

def cantidad_correos():
    """Retorna la cantidad total de correos (recibidos + enviados)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM correos")
    result = cursor.fetchone()
    conn.close()
    return result[0]

def cantidad_correos_recibidos():
    """Retorna la cantidad total de correos recibidos"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM correos WHERE tipo = 'recibido'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

def cantidad_correos_enviados():
    """Retorna la cantidad total de correos enviados"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM correos WHERE tipo = 'enviado'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

def cantidad_correos_no_leidos():
    """Retorna la cantidad total de correos no leídos de la carpeta recibidos"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM correos WHERE tipo = 'recibido' AND leido = FALSE")
    result = cursor.fetchone()
    conn.close()
    return result[0]

def cantidad_contactos():
    """Retorna la cantidad total de contactos"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM contactos")
    result = cursor.fetchone()
    conn.close()
    return result[0]

def agregar_correo_recibido(asunto, mensaje, remitente, destinatarios):
    """Agrega un nuevo correo a la carpeta de recibidos"""
    conn = get_db_connection()
    cursor = conn.cursor()
    destinatarios_json = json.dumps(destinatarios)
    cursor.execute('''
        INSERT INTO correos (asunto, mensaje, remitente, destinatarios, tipo, leido)
        VALUES (%s, %s, %s, %s, 'recibido', FALSE)
    ''', (asunto, mensaje, remitente, destinatarios_json))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def enviar_correo(asunto, mensaje, remitente, destinatarios):
    """Agrega un nuevo correo a la carpeta de enviados"""
    conn = get_db_connection()
    cursor = conn.cursor()
    destinatarios_json = json.dumps(destinatarios)
    cursor.execute('''
        INSERT INTO correos (asunto, mensaje, remitente, destinatarios, tipo, leido)
        VALUES (%s, %s, %s, %s, 'enviado', TRUE)
    ''', (asunto, mensaje, remitente, destinatarios_json))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def agregar_contacto(nombre, apellido, email):
    """Agrega un nuevo contacto a la agenda"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO contactos (nombre, apellido, email)
            VALUES (%s, %s, %s)
        ''', (nombre, apellido, email))
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False

def obtener_todos_correos():
    """Obtiene todos los correos (para mostrar en la API)"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM correos ORDER BY fecha DESC")
    results = cursor.fetchall()
    conn.close()
    for result in results:
        result['destinatarios'] = json.loads(result['destinatarios'])
    return results

def obtener_todos_contactos():
    """Obtiene todos los contactos"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contactos ORDER BY nombre, apellido")
    results = cursor.fetchall()
    conn.close()
    return results