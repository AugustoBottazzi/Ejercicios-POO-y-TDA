alumnos = [{"nombre": "Juan", "apellido": "Pérez", "edad": 20, "curso": ("Matematica",)},
    {"nombre": "Ana", "apellido": "González", "edad": 22, "curso": ("Matematica",)},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 21, "curso": ("Historia",)},
    {"nombre": "Elena", "apellido": "Sánchez", "edad": 23, "curso": ("Matematica",)},
    {"nombre": "Carlos", "apellido": "Rodríguez", "edad": 20, "curso": ("Historia",)}]

def alumnos_indice_edad():
    alumno_mas_joven = alumnos[0]
    alumno_mas_grande = alumnos[0]

    for alumno in alumnos[1:]:

        if alumno["edad"] < alumno_mas_joven["edad"]:
            alumno_mas_joven = alumno

        if alumno["edad"] > alumno_mas_grande["edad"]:
            alumno_mas_grande = alumno

    print(f"Alumno más joven: {alumno_mas_joven["nombre"]}, {alumno_mas_joven["apellido"]}, Edad: {alumno_mas_joven["edad"]}")
    print(f"Alumno más grande: {alumno_mas_grande["nombre"]} {alumno_mas_grande["apellido"]}, Edad: {alumno_mas_grande["edad"]}")