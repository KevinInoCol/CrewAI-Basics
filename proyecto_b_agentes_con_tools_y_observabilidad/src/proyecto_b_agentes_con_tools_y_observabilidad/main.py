#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from proyecto_b_agentes_con_tools_y_observabilidad.crew import CrearPublicacionBlogConHerramientas

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Ejecutar el 'crew'.
    """
    inputs = {
        'topico': 'Desarrollo de aplicaciones IA con Claude Code'
    }
    
    try:
        # Cambiado .crew() a .equipo()
        CrearPublicacionBlogConHerramientas().equipo().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"Ocurrió un error al ejecutar el 'crew': {e}")


def train():
    """
    Entrenar el 'crew' durante un número determinado de iteraciones.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        # Cambiado .crew() a .equipo()
        CrearPublicacionBlogConHerramientas().equipo().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"Ocurrió un error al entrenar el 'crew': {e}")

def replay():
    """
    Repetir la ejecución del 'crew' desde una tarea específica.
    """
    try:
        # Cambiado .crew() a .equipo()
        CrearPublicacionBlogConHerramientas().equipo().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Ocurrió un error al repetir la ejecución del 'crew': {e}")

def test():
    """
    Probar la ejecución del 'crew' y devolver los resultados.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        # Cambiado .crew() a .equipo()
        CrearPublicacionBlogConHerramientas().equipo().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"Ocurrió un error al probar el 'crew': {e}")

if __name__ == '__main__':
    run()