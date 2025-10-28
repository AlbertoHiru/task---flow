from flask import Flask, render_template, request, redirect, url_for
from src.database import DBManager
from src.modelos import Tarea, Proyecto


app = Flask(__name__)
db_manager = DBManager()


@app.route('/')
def index():
    tareas_pendientes = db_manager.obtener_tareas(estado="Pendiente")
    proyectos = db_manager.obtener_proyectos()

    return render_template('index.html',
                           tareas=tareas_pendientes,
                           proyectos=proyectos)


@app.route('/crear', methods=['GET', 'POST'])
def crear_tarea_web():

    proyectos = db_manager.obtener_proyectos()

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        limite = request.form.get('fecha_limite')
        prioridad = request.form.get('prioridad')

        proyecto_id = int(request.form.get('proyecto_id'))

        nueva_tarea = Tarea(
            titulo=titulo,
            descripcion=descripcion,
            fecha_limite=limite,
            prioridad=prioridad,
            proyecto_id=proyecto_id
        )

        db_manager.crear_tarea(nueva_tarea)

        return redirect(url_for('index'))

    return render_template('formulario_tarea.html', proyectos=proyectos)


if __name__ == 'main':

    db_manager.crear_tablas()
    print("Iniciando servidor")
    app.run(debug=True)