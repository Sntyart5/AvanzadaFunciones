# Definir una lista de estudiantes como una lista de diccionarios
estudiantes = []

# Función para agregar un nuevo estudiante
def agregar_estudiante(nombre, edad, grado, calificaciones):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "grado": grado,
        "calificaciones": calificaciones
    }
    estudiantes.append(estudiante)

# Función para mostrar la lista de estudiantes
def mostrar_estudiantes():
    for estudiante in estudiantes:
        print(estudiante)

# Función para buscar un estudiante por nombre
def buscar_estudiante_por_nombre(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            return estudiante
    return None

# Función para calcular el promedio de calificaciones de un estudiante
def calcular_promedio_calificaciones(estudiante):
    calificaciones = estudiante["calificaciones"]
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio

# Código de prueba
agregar_estudiante("Juan Pérez", 15, 10, [90, 85, 88])
agregar_estudiante("María Gómez", 16, 11, [92, 89, 91])

print("Lista de Estudiantes:")
mostrar_estudiantes()

nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
estudiante_buscado = buscar_estudiante_por_nombre(nombre_buscar)

if estudiante_buscado:
    print(f"Información del Estudiante: {estudiante_buscado}")
    promedio_calificaciones = calcular_promedio_calificaciones(estudiante_buscado)
    print(f"Promedio de Calificaciones: {promedio_calificaciones}")
else:
    print("Estudiante no encontrado.")
