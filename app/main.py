from fastapi import FastAPI, HTTPException
from typing import List
import app.crud as crud
from app.schemas import CorreoCreate, Correo, ContactoCreate, Contacto, Cuenta
from app.database import init_db

app = FastAPI(title="Cliente de Correo API", description="API para gestión de correo electrónico")

# Inicializar base de datos al iniciar
@app.on_event("startup")
async def startup_event():
    init_db()

# ========== ENDPOINTS DE CORREOS ==========

@app.get("/")
def root():
    return {"mensaje": "API de Cliente de Correo funcionando"}

@app.get("/correos/cantidad-total")
def get_cantidad_total():
    """Retorna la cantidad total de correos (recibidos + enviados)"""
    return {"total_correos": crud.cantidad_correos()}

@app.get("/correos/cantidad-recibidos")
def get_cantidad_recibidos():
    """Retorna la cantidad total de correos recibidos"""
    return {"correos_recibidos": crud.cantidad_correos_recibidos()}

@app.get("/correos/cantidad-enviados")
def get_cantidad_enviados():
    """Retorna la cantidad total de correos enviados"""
    return {"correos_enviados": crud.cantidad_correos_enviados()}

@app.get("/correos/cantidad-no-leidos")
def get_cantidad_no_leidos():
    """Retorna la cantidad total de correos no leídos de la carpeta recibidos"""
    return {"correos_no_leidos": crud.cantidad_correos_no_leidos()}

@app.post("/correos/recibir")
def recibir_correo(correo: CorreoCreate):
    """Simula la recepción de un correo"""
    id = crud.agregar_correo_recibido(
        correo.asunto, 
        correo.mensaje, 
        correo.remitente, 
        correo.destinatarios
    )
    return {"mensaje": "Correo recibido", "id": id}

@app.post("/correos/enviar")
def enviar_correo(correo: CorreoCreate):
    """Simula el envío de un correo"""
    id = crud.enviar_correo(
        correo.asunto, 
        correo.mensaje, 
        correo.remitente, 
        correo.destinatarios
    )
    return {"mensaje": "Correo enviado", "id": id}

@app.get("/correos/todos")
def get_todos_correos():
    """Obtiene todos los correos"""
    return crud.obtener_todos_correos()

# ========== ENDPOINTS DE CONTACTOS ==========

@app.get("/contactos/cantidad")
def get_cantidad_contactos():
    """Retorna la cantidad total de contactos"""
    return {"total_contactos": crud.cantidad_contactos()}

@app.post("/contactos/agregar")
def agregar_contacto(contacto: ContactoCreate):
    """Agrega un nuevo contacto a la agenda"""
    success = crud.agregar_contacto(contacto.nombre, contacto.apellido, contacto.email)
    if success:
        return {"mensaje": "Contacto agregado exitosamente"}
    else:
        raise HTTPException(status_code=400, detail="Error: El email ya existe")

@app.get("/contactos/todos")
def get_todos_contactos():
    """Obtiene todos los contactos"""
    return crud.obtener_todos_contactos()