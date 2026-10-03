# Tarea 3: Organización de calaveritas y conteo de caracteres

calaveritas = ["Alebrije", "Catrina", "Cempasúchil", "Pan de muerto", "Papel picado"]

# Filtrar palabras que tengan más de 7 letras (Método tradicional)
largas_tradicional = []
for elemento in calaveritas:
    if len(elemento) > 7:
        largas_tradicional.append(elemento)

print("Palabras largas (Tradicional):", largas_tradicional)

"""
#8. Comprensión de Listas (List Comprehension): Re-escribe el bloque de código anterior
 en una sola línea utilizando comprensión de listas para crear largas_comprehension.

#9. Utiliza una comprensión de listas para convertir todos los elementos de la lista
 calaveritas a mayúsculas usando .upper().

#10. Comprensión de Diccionarios (Dictionary Comprehension): Crea un diccionario a
 partir de  la lista calaveritas donde la llave sea el nombre del elemento y el valor
 sea la cantidad de letras que tiene esa palabra (usando la función len()).

#11. Pregunta de análisis: ¿Qué ventaja ofrece escribir la solución con comprensiones
 en lugar de usar un bucle for tradicional con un .append()?
"""