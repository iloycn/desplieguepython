from database import db
from sqlalchemy.sql import func

# Para crear las tablas, desde el entorno de ejecución de Python, ejecutar:
# from database import app, db
# from jugador import Jugador
# app.app_context().push()
# db.create_all()

class Jugador(db.Model):
    
    __tablename__ = 'jugadores'
         
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30), nullable=False)
    Equipo = db.Column(db.String(100), nullable=False)
    Altura = db.Column(db.Integer)
    Posicion = db.Column(db.Text)

     
    def __init__(self, Nombre, Equipo, Altura, Posicion):
        self.nombre = Nombre
        self.equipo = Equipo
        self.altura = Altura
        self.posicion = Posicion

    def __repr__(self):
        return f'<Estudiante {self.id}>: {self.nombre}, {self.equipo}'
    
    