# ==========================================
#  M7 Proyecto Día de Los Muertos
# ==========================================

"""Tarea 1: Preparando la Ofrenda (Listas y Tuplas)"""

# ----------------------------------------------------
# PARTE 1: Listas (Mutable)
# ----------------------------------------------------
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]

# Mostrar la segunda ofrenda inicial (índice 1)
print("Segunda ofrenda inicial:", ofrendas[1])

# TODO: Modificación 1 (Listas)
# 1. Agrega "Incienso copal" a la lista usando .append()
# 2. Ordena la lista alfabéticamente usando .sort()
# 3. Imprime la lista completa para verificar los cambios.

# PREGUNTA 1: ¿Qué elemento ocupa ahora el índice 1 después de usar .sort()? 
# ¿Por qué cambió o se mantuvo la posición?


# ----------------------------------------------------
# PARTE 2: Tuplas (Inmutable)
# ----------------------------------------------------
NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")

# TODO: Modificación 2 (Tuplas)
# Descomenta la siguiente línea e intenta ejecutar el código:
# NIVELES_ALTAR[0] = "Gloria"

# PREGUNTA 2: ¿Qué error aparece al ejecutar la línea anterior y por qué Python no permite este cambio?


# ----------------------------------------------------
# PARTE 3: Recorrer con enumerate()
# ----------------------------------------------------
# TODO: Usa un bucle for junto con enumerate() para imprimir cada ofrenda
# formateada con su número de posición (ejemplo: "0: Calaverita de azúcar").

print("\nOfrendas del altar:")
# Escribe tu código aquí: