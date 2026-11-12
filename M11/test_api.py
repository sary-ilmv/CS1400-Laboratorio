from api import obtener_coordenadas
import sys

# Arreglamos la salida para que muestre bien los acentos
sys.stdout.reconfigure(encoding='utf-8')

print("[TEST] Iniciando pruebas de la API...")

# Prueba 1: Ciudad válida con acentos o espacios
print("\n--- Probando una ciudad válida (Bogotá) ---")
resultado_bogota = obtener_coordenadas("Bogotá ")
print(resultado_bogota)

# Prueba 2: Otra ciudad válida en otro país
print("\n--- Probando otra ciudad (Tokio) ---")
resultado_tokio = obtener_coordenadas("Tokyo")
print(resultado_tokio)

# Prueba 3: Ciudad inventada o que no existe
print("\n--- Probando un lugar falso (AtlantisXYZ) ---")
resultado_falso = obtener_coordenadas("AtlantisXYZ123")
print(resultado_falso)

print("\n[FIN] Pruebas finalizadas.")

# TODO 1: Que notas raro en la salida al correr test_api?
# Note que los acentos pueden aparecer incorrectamente
# en la terminal y que la ciudad inventada no devuelve resultados

# TODO 2: Agrega estas lineas para arreglar el problema con los acentos.
import sys
sys.stdout.reconfigure(encoding='utf-8')

# TODO 3: Intenta con otra ciudad.
resultado_otra = obtener_coordenadas("Berlin")
print("\n--- Probando otra ciudad (Berlin) ---")
print(resultado_otra)