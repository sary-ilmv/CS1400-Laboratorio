#grecia lopez orozco
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""

# 1. Pedir la edad al usuario
edad_texto = input("Cual es tu edad?: ")
edad = int(edad_texto)

# 2. Pedir si aprobó el examen de manejo
paso_examen = input("Aprobaste el examen de conducir? (si/no): ").strip().lower()

# 3. Estructura condicional
# Primera sentencia: Debe ser mayor o igual a 18 años y haber pasado el examen
if edad >= 18 and paso_examen == "si":
    print("Felicidades! Eres elegible para tramitar y recibir tu licencia de conducir.")

# Segunda sentencia: Es mayor de edad pero NO aprobó el examen
elif edad >= 18 and paso_examen != "si":
    print("Tienes la edad suficiente, pero debes aprobar el examen práctico/teórico para obtener la licencia.")

# Tercera sentencia: Es menor de edad
else:
    print("Lo sentimos, debes tener al menos 18 años para solicitar la licencia de conducir.")