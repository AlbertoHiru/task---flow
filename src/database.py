import sqlite3
from .modelo import Proyecto, Tarea

import os

DATABASE_NAME = "tareas.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

class DBManager:
    
    def __init__(self):
        crear_tablas()

    def crear_tarea(self, tarea: Tarea) -> Tarea:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tareas (titulo, descripcion, fecha_creacion, fecha_limite, prioridad, estado, proyecto_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (tarea._titulo, tarea._descripcion, tarea._fecha_creacion, tarea._fecha_limite, tarea._prioridad, tarea._estado, tarea._proyecto_id))

        tarea.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return tarea   
    
    def obtener_proyectos(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proyectos")
        filas = cursor.fetchall()
        conn.close()
        proyectos = [
            Proyecto(nombre=fila['nombre'], descripcion=fila['descripcion'], fecha_inicio=fila['fecha_creacion'], id=fila['id'], estado=fila['estado'])
    ]


def crear_tablas():
    conn.get_connection()()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proyectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            fecha_creacion TEXT NOT NULL
        )""")
    
    # Crear tabla de tareas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,                               
            titulo TEXT NOT NULL,
            descripcion TEXT,
            fecha_creacion TEXT NOT NULL,
            fecha_limite TEXT,
            prioridad TEXT,
            estado TEXT,
            proyecto_id INTEGER,
            FOREIGN KEY (proyecto_id) REFERENCES proyectos (id)
        )""")

    try:
        cursor.execute("""insert into proyectos (id, nombre, descripcion, estado) VALUES (0, 'tareas generales', 'Tareas sin clasificar', 'Activo')""")
    except sqlite3.IntegrityError:
        pass  # El proyecto ya existe
    conn.commit()
    conn.close()



