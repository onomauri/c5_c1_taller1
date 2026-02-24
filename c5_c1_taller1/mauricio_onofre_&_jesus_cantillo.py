
cantidad = int(input("¿Cuántas personas desea registrar?: "))


for i in range(cantidad):
    nombre= input(f"ingrese el nombre de la persona #{i+1}: ")
    edad = int(input(f"Ingrese la Edad de la persona #{i+1}: "))
    c= input("¿Tiene conocimientos básicos de computación? (si/no): ").lower()

    while edad <= 0:
        print("edad invalida favor ingrese la edad nuevamente: ")
        edad = int(input(f"Ingrese la Edad de la persona #{i+1}: "))

    if edad >= 15 and c == "si":
        print("Puede participar en el taller")
    else:
        print("No cumple los requisitos")

print("Proceso finalizado")


