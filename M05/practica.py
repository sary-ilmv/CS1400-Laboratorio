#### Ejemplo 1

num = int(input("Introduce un número entre 10 y 20: "))
print("Contando hacia arriba")
for i in range(0, num, 1):
    print(i)
print("Contando hacia abajo")
for i in range(num, 0, -1):
    print(i)

    #### Ejemplo 2
"""
    num = int(input("Introduce un número positivo o negativo (0 para salir): "))

negativos = 0

positivos = 0

while num != 0:

    if num < 0:

        print("El número es negativo")

        negativos += 1

    else:

        print("El número es positivo")

        positivos += 1

    num = int(input("Introduce un número positivo o negativo (0 para salir): "))

print("Total negativos:", negativos)

print("Total positivos:", positivos)
"""