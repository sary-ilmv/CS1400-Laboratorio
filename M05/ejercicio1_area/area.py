"""
## 📗 Calcular el Área de Varios Círculos (Práctica de Iteraciones)

### Instrucciones:
1. Importa el módulo math.
2. Crea una lista con los radios: [5, 12, -3, 8, 0].
3. Utiliza un bucle for para recorrer cada radio de la lista.
4. Dentro del bucle, usa un condicional if/else para calcular y mostrar el área únicamente si el radio es mayor que 0.
5. Reto de Iteración Continuada: Cambia la estructura a un bucle while que le pida al usuario radios continuamente con input() hasta que ingrese 'salir', calculando el área de cada radio válido o pidiendo el dato de nuevo si no es válido.

NOMBRE: [Tu Nombre]
MÓDULO 5 - TAREA 1 (Adaptada)
ÁREA DE CÍRCULOS E ITERACIONES
Uso de bucles (for / while), listas, validación y estructuras de control.
"""

import math

# --- PARTE 1: Iteración sobre una lista de datos (Bucle FOR) ---

radios = [5, 12, -3, 8, 0]

print("--- Procesando lista de radios ---")

# TODO Tarea 1: Crea un bucle 'for' que recorra la lista 'radios'.
for radio in radios:
    # TODO Tarea 2: Verifica con if/else si el radio es válido (mayor a 0).
    if radio > 0:
        area = math.pi * (radio ** 2)
        print(f"Radio: {radio} -> Área: {area:.2f}")
    else:
        print(f"Radio: {radio} -> Error: El radio debe ser mayor que cero.")


# --- PARTE 2 Y RETO: Iteración interactiva y continua (Bucle WHILE) ---

print("\n--- Modo Interactivo (Escribe 'salir' para terminar) ---")

# TODO Reto: Completa el bucle while para solicitar radios al usuario indefinidamente.
# Debe repetirse hasta que el usuario escriba 'salir'.

while True:
    entrada = input("Ingresa el radio del círculo (o 'salir'): ").strip().lower()
    
    if entrada == 'salir':
        print("¡Programa finalizado!")
        break  # Interrumpe la iteración
    
    try:
        radio_usuario = float(entrada)
        
        # Validar si es positivo mediante iteración/condición
        if radio_usuario > 0:
            area = math.pi * (radio_usuario ** 2)
            print(f"El área del círculo es: {area:.2f}\n")
        else:
            print("Error: El radio debe ser mayor que cero. Intenta de nuevo.\n")
            
    except ValueError:
        print("Error: Por favor ingresa un número válido o la palabra 'salir'.\n")