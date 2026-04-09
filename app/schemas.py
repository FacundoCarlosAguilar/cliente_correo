from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CorreoBase(BaseModel):
    asunto: str
    mensaje: str
    remitente: str
    destinatarios: List[str]

class CorreoCreate(CorreoBase):
    leido: Optional[bool] = False

class Correo(CorreoBase):
    id: int
    leido: bool
    tipo: str
    fecha: datetime
    
    class Config:
        from_attributes = True

class ContactoBase(BaseModel):
    nombre: str
    apellido: str
    email: str

class ContactoCreate(ContactoBase):
    pass

class Contacto(ContactoBase):
    id: int
    
    class Config:
        from_attributes = True

class CuentaBase(BaseModel):
    nombre_usuario: str
    email: str
    servidor_entrada: str
    servidor_salida: str

class Cuenta(CuentaBase):
    id: int