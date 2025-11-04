from datetime import datetime


class Proyecto:
    """
    Clase que representa un proyecto. Usa POO: Encapsulamiento con guion bajo.
    """

    def __init__(self, nombre: str, descripcion: str = "", id: int = None, estado: str = "Activo"):
        # Atributos internos (encapsulados)
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._estado = estado

    @property
    def id(self):
        """Getter para acceder al ID de forma limpia (proyecto.id)."""
        return self._id

    @id.setter
    def id(self, valor):
        """Setter necesario para que la DB pueda asignar el ID después de la creación."""
        self._id = valor

    def to_dict(self):
        """Convierte el objeto a un diccionario, útil para Flask y la DB."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'descripcion': self._descripcion,
            'fecha_inicio': self._fecha_inicio,
            'estado': self._estado
        }


class Tarea:
    """
    Clase que representa una tarea individual.
    Aplica POO: Encapsulamiento y un método que modela un comportamiento.
    """

    def __init__(self, titulo: str, fecha_limite: str, prioridad: str,
                 proyecto_id: int, descripcion: str = "", id: int = None,
                 estado: str = "Pendiente", fecha_creacion: str = None):

        self._id = id
        self._titulo = titulo
        self._descripcion = descripcion
        # Si no se proporciona fecha_creacion, se genera una nueva (para tareas nuevas)
        # Si se proporciona, se usa esa (para tareas cargadas de la DB)
        self._fecha_creacion = fecha_creacion if fecha_creacion else datetime.now(
        ).strftime("%Y-%m-%d %H:%M:%S")
        self._fecha_limite = fecha_limite
        self._prioridad = prioridad
        self._estado = estado
        self._proyecto_id = proyecto_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    # *Algoritmo de Comportamiento (Método)*
    def marcar_como_completada(self):
        """Método de la clase que cambia el estado si no está ya completada."""
        if self._estado != "Completada":
            self._estado = "Completada"
            return True
        return False

    def to_dict(self):
        return {
            'id': self._id,
            'titulo': self._titulo,
            'descripcion': self._descripcion,
            'fecha_creacion': self._fecha_creacion,
            'fecha_limite': self._fecha_limite,
            'prioridad': self._prioridad,
            'estado': self._estado,
            'proyecto_id': self._proyecto_id
        }