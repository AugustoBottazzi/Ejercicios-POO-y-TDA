alumnos = [{"nombre": "Juan", "apellido": "Pérez", "edad": 20, "curso": ("Matematica",)},
    {"nombre": "Ana", "apellido": "González", "edad": 22, "curso": ("Matematica",)},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 21, "curso": ("Historia",)},
    {"nombre": "Elena", "apellido": "Sánchez", "edad": 23, "curso": ("Matematica",)},
    {"nombre": "Carlos", "apellido": "Rodríguez", "edad": 20, "curso": ("Historia",)}]

def promedio_edad_curso(Matematica):
    alumnos_curso = [alumno["edad"] for alumno in alumnos if alumno["curso"] == (Matematica)]
    
    if len(alumnos_curso) == 0:
        return f"No hay alumnos en el curso {Matematica}"
    
    promedio = sum(alumnos_curso) / len(alumnos_curso)
    return promedio

curso = "Matematica"
promedio = promedio_edad_curso(curso)
print(f"El promedio de edad en el curso {curso} es: {promedio}")

#Mal