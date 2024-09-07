# Sistema de gestión de estudiantes

# Cada estudiante es una tupla (nombre, [lista de notas])
estudiantes = [
    ("Juan", [7, 8, 6]),
    ("Ana", [9, 9, 8]),
    ("Pedro", [4, 5, 6]),
]

# Función para agregar un nuevo estudiante
def agregar_estudiante(nombre, estudiantes):
    estudiantes.append((nombre, []))
    print(f"Estudiante {nombre} agregado exitosamente.")

# Función para añadir una nota a un estudiante
def añadir_nota(nombre, nota, estudiantes):
    for i, (nombre_estudiante, notas) in enumerate(estudiantes):
        if nombre_estudiante == nombre:
            estudiantes[i][1].append(nota)
            print(f"Nota {nota} añadida a {nombre}.")
            return
    print(f"Estudiante {nombre} no encontrado.")

# Función para calcular la media de notas de un estudiante
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Función para mostrar los estudiantes aprobados
def mostrar_estudiantes_aprobados(estudiantes):
    print("Estudiantes aprobados:")
    for nombre, notas in estudiantes:
        media = calcular_media(notas)
        if media >= 6:
            print(f"{nombre}: Media = {media}")

# Función para mostrar el estudiante con la mejor nota promedio
def mostrar_mejor_estudiante(estudiantes):
    mejor_estudiante = None
    mejor_media = -1
    
    for nombre, notas in estudiantes:
        media = calcular_media(notas)
        if media > mejor_media:
            mejor_media = media
            mejor_estudiante = nombre
            
    if mejor_estudiante:
        print(f"El mejor estudiante es {mejor_estudiante} con una media de {mejor_media}")
    else:
        print("No hay estudiantes registrados.")

# Función para mostrar la lista de estudiantes
def mostrar_estudiantes(estudiantes):
    print("Lista de estudiantes:")
    for nombre, notas in estudiantes:
        media = calcular_media(notas)
        print(f"{nombre}: Notas = {notas}, Media = {media}")

# Menú principal
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar nuevo estudiante")
        print("2. Añadir nota a un estudiante")
        print("3. Mostrar estudiantes aprobados")
        print("4. Mostrar el mejor estudiante")
        print("5. Mostrar todos los estudiantes")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del estudiante: ")
            agregar_estudiante(nombre, estudiantes)
        
        elif opcion == "2":
            nombre = input("Introduce el nombre del estudiante: ")
            nota = float(input("Introduce la nota: "))
            añadir_nota(nombre, nota, estudiantes)
        
        elif opcion == "3":
            mostrar_estudiantes_aprobados(estudiantes)
        
        elif opcion == "4":
            mostrar_mejor_estudiante(estudiantes)
        
        elif opcion == "5":
            mostrar_estudiantes(estudiantes)
        
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
menu()
