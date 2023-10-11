# Definir una lista de estudiantes como una lista de diccionarios
estudiantes = []

# Función para agregar un nuevo estudiante
agregar_estudiante = lambda: estudiantes.append({
    "nombre": input("Ingrese el nombre del estudiante: "),
    "edad": int(input("Ingrese la edad del estudiante: ")),
    "grado": int(input("Ingrese el grado del estudiante: ")),
    "calificaciones": list(map(int, input("Ingrese las calificaciones del estudiante separadas por espacio: ").split()))
})

# Función para mostrar la lista de estudiantes
mostrar_estudiantes = lambda: print(estudiantes)

# Función para buscar un estudiante por nombre
buscar_estudiante_por_nombre = lambda nombre: next((estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre), None)

# Función para calcular el promedio de calificaciones de un estudiante
calcular_promedio_calificaciones = lambda estudiante: sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"]) if "calificaciones" in estudiante else None

# Código de prueba
agregar_estudiante()
agregar_estudiante()

print("Lista de Estudiantes:")
mostrar_estudiantes()

nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
estudiante_buscado = buscar_estudiante_por_nombre(nombre_buscar)

if estudiante_buscado:
    print(f"Información del Estudiante: {estudiante_buscado}")
    promedio_calificaciones = calcular_promedio_calificaciones(estudiante_buscado)
    if promedio_calificaciones:
        print(f"Promedio de Calificaciones: {promedio_calificaciones}")
    else:
        print("No hay calificaciones registradas para este estudiante.")
else:
    print("Estudiante no encontrado.")
