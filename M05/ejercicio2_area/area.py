"""
## 📗 Calcular el Área de Varios Círculos (Práctica de Iteraciones)

### Instrucciones:
1. Descomenta la linea que dejara importar el módulo math.
2. Crea una lista con los radios: [5, 12, -3, 8, 0].
3. Utiliza un bucle for para recorrer cada radio de la lista.
4. Dentro del bucle, usa un condicional if/else para calcular y mostrar el área únicamente si el radio es mayor que 0.
5. Reto de Iteración Continuada: Cambia la estructura a un bucle while que le pida al usuario radios continuamente con input() hasta que ingrese 'salir', calculando el área de cada radio válido o pidiendo el dato de nuevo si no es válido.

NOMBRE: [Tu Nombre]
MÓDULO 5 - EJERCICIO 2 (Adaptada)
ÁREA DE CÍRCULOS E ITERACIONES
Uso de bucles (for / while), listas, validación y estructuras de control.
"""

# importando el modulo math
# import math

# --- PARTE 1: Iteración sobre una lista de datos (FOR Loop) ---

radios = [5, 12, -3, 8, 0]

print("--- Procesando lista de radios ---")

# TODO Tarea 1: Crea un bucle 'for' que recorra la lista 'radios' mira las palabras claves mas adelante para evitar errores.
#

    # TODO Tarea 2: Verifica con if/else si el radio es válido (mayor a 0).
    #
        area = math.pi * (radio ** 2)
        print(f"Radio: {radio} -> Área: {area:.2f}")
    else:
        print(f"Radio: {radio} -> Error: El radio debe ser mayor que cero.")


# --- PARTE 2: Iteración interactiva y continua (WHILE Loop) ---

print("\n--- Modo Interactivo (Escribe 'salir' para terminar) ---")

# TODO Reto: Completa el while loop para solicitar radios al usuario indefinidamente.
# Debe repetirse hasta que el usuario escriba 'salir'.

# while True:
    # variable A
    #

    # if sentence si A es igual a algo para salir
    #entonces imprimir mensage de finalizacion
    # aqui un break
    # break  # Interrumpe la iteración
    
#   try:
       # otro variable B cambiar variable A a flotante
        #
        
        # Validar si es positivo mediante iteración/condición
        #if variable B > 0:  # para evitar errores de matematica
            #entonces la matematica se hace igual que en la Parte 1
            # area = math.pi * (radio_usuario ** 2)
            #print(f"El área del círculo es: {area:.2f}\n")
        #else:
            # print un mesage de error que deplano no fue un numero mayor a 0

     # Otra manera de encontrar errores del usuario. Descomenta las siguientes lineas al finalizar tu while loop.       
    #except ValueError:
     #   print("Error: Por favor ingresa un número válido o la palabra 'salir'.\n")