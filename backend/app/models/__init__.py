# Importamos los modelos relacionados con usuarios.
from .user import User, UserRole

# Importamos los modelos y enumeraciones de incidentes.
from .incident import (
    Incident,
    IncidentCategory,
    IncidentPriority,
    IncidentStatus,
)

# Importamos el modelo de comentarios.
from .comment import Comment

# Importamos el modelo de historial de actividad.
from .activity_history import ActivityHistory

# Importamos el modelo de proyectos y sus estados.
from .project import Project, ProjectStatus

# Importamos el modelo de tareas,
# junto con sus estados y prioridades.
from .task import Task, TaskPriority, TaskStatus


# __all__ define qué elementos queremos exponer
# cuando importemos desde app.models.
#
# Esto también nos ayuda a mantener organizados
# todos los modelos del proyecto en un solo lugar.
__all__ = [
    "User",
    "UserRole",
    "Incident",
    "IncidentCategory",
    "IncidentPriority",
    "IncidentStatus",
    "Comment",
    "ActivityHistory",
    "Project",
    "ProjectStatus",
    "Task",
    "TaskPriority",
    "TaskStatus",
]