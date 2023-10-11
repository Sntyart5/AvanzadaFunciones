estudiantes = []

def agregar_estudiante(nombre, grado, nota1, nota2, nota3,curso):
    estudiante = {
        "nombre": nombre,
        "curso": curso,
        "grado": grado,
        "N1": nota1,
        "N2": nota2,
        "N3": nota3,
    }
    estudiantes.append(estudiante)

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def mostrar_estudiantes():
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Curso: {estudiante['curso']}")
        print(f"Grado: {estudiante['grado']}")
        print(f"Nota N'1: {estudiante['N1']}")
        print(f"Nota N'2: {estudiante['N2']}")
        print(f"Nota N'3: {estudiante['N3']}")
        print("-------------------------")

def actualizar_informacion():
    print("Opciones de Actualización:")
    print("1. Nombre")
    print("2. Curso")
    print("3. Grado")
    print("4. Nota N'1")
    print("5. Nota N'2")
    print("6. Nota N'3")
    opcion = input("Seleccione el campo que desea actualizar: ")

    if opcion == "1":
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        return nuevo_nombre
    elif opcion == "2":
        nuevo_curso = input("Ingrese el nuevo curso: ")
        return nuevo_curso
    elif opcion == "3":
        nuevo_grado = int(input("Ingrese el nuevo grado: "))
        return nuevo_grado
    elif opcion == "4":
        nueva_nota1 = float(input("Ingrese la nueva Nota N'1: "))
        return nueva_nota1
    elif opcion == "5":
        nueva_nota2 = float(input("Ingrese la nueva Nota N'2: "))
        return nueva_nota2
    elif opcion == "6":
        nueva_nota3 = float(input("Ingrese la nueva Nota N'3: "))
        return nueva_nota3
    else:
        print("Opción no válida.")
        return None



con_estudiantes = 0

while True:
    print("="*20)
    print("Menu:")
    print("1. Agregar Estudiante")
    print("2. Consultar Estudiantes")
    print("3. Actualizar Información")
    print("0. Salir")
    print("="*20)
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese Su Nombre Completo: ")
        curso = (input("Digite Nombre del curso: "))
        grado = int(input("Digite Grado que esta cursando: "))
        nota1 = float(input("Digite la primera Nota: "))
        nota2 = float(input("Digite la segunda Nota: "))
        nota3 = float(input("Digite la tercera Nota: "))
        
        promedio = calcular_promedio(nota1, nota2, nota3)
        agregar_estudiante(nombre, grado, nota1, nota2, nota3, curso)
        
        print("-"*30)
        print(f"Nombre: {nombre}")
        print(f"Curso: {curso}")
        print(f"Grado: {grado}")
        print(f"Nota N'1: {nota1}")
        print(f"Nota N'2: {nota2}")
        print(f"Nota N'3: {nota3}")
        print(f"Promedio del estudiante: {promedio}")
        
        
    elif opcion == "2":
        if estudiantes:
            print("Lista de Estudiantes:")
            mostrar_estudiantes()
        else:
            print("No hay estudiantes registrados.")
            
    elif opcion == "3":
        if estudiantes:
            mostrar_estudiantes()
            indice = int(input("Ingrese el número de estudiante que desea actualizar: "))
            if 0 < indice <= len(estudiantes):
                nuevo_valor = actualizar_informacion()
                if nuevo_valor is not None:
                    campo_actualizado = list(estudiantes[indice - 1].keys())[int(opcion) - 1]
                    estudiantes[indice - 1][campo_actualizado] = nuevo_valor
                    print(f"Información actualizada exitosamente para el campo '{campo_actualizado}'.")
            else:
                print("Número de estudiante inválido.")
        else:
            print("No hay estudiantes registrados.")

            
    elif opcion == "0":
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
        
    con_estudiantes += 1

print("Numero de estudiantes",con_estudiantes)
