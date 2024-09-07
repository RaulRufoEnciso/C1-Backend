
estudiantes = [("Juan", [7, 8, 6]), ("Ana", [9, 9, 8]), ("Pedro", [4, 5, 6])]

def agregar_estudiante(nombre): estudiantes.append((nombre, []))

def añadir_nota(nombre, nota):
    for i, (n, notas) in enumerate(estudiantes):
        if n == nombre: estudiantes[i][1].append(nota)

def media(notas): return sum(notas) / len(notas) if notas else 0

def mostrar_aprobados(): print([n for n, notas in estudiantes if media(notas) >= 6])

def mejor_estudiante():
    print(max(estudiantes, key=lambda est: media(est[1]), default=("Ninguno", [])))

while True:
    op = input("\n1.Agregar\n2.Añadir nota\n3.Aprobados\n4.Mejor estudiante\n5.Salir\nElige: ")
    if op == "1": agregar_estudiante(input("Nombre: "))
    elif op == "2": añadir_nota(input("Nombre: "), float(input("Nota: ")))
    elif op == "3": mostrar_aprobados()
    elif op == "4": mejor_estudiante()
    elif op == "5": break
