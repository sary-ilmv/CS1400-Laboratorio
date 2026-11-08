# -*- coding: utf-8 -*-
"""
==========================================================
 PROGRAMA DE DEMOSTRACION: ENTRADA / SALIDA EN PYTHON
==========================================================
Este programa tiene tres partes:

  PARTE 1: Entrada y salida basica (input / print)
  PARTE 2: (Extra) Consumir una API que devuelve JSON
"""

# ----------------------------------------------------------
# IMPORTACIONES
# ----------------------------------------------------------
import json
import random
import urllib.request
import urllib.error


# ==========================================================
# LOS REFRANES DE LA ABUELA
# ==========================================================
# Un diccionario guarda parejas "clave: valor".
# Aqui la clave es el refran y el valor es lo que significa.
# TODO 1: Agregar al menos un refran de tu familia.
REFRANES = {
    "Haz el bien y no mires a quien.":
        "Ayuda a los demas sin esperar nada a cambio.",

    "El leon juzga por su condicion.":
        "Cada quien cree que los demas piensan y actuan como uno.",

    "Uno pone y Dios dispone.":
        "Hacemos planes, pero la vida decide el resultado.",

    "Agua que no has de beber, dejala correr.":
        "Si algo no te conviene o no te toca, no te metas.",

    "Mas vale tarde que nunca.":
        "Es mejor hacer algo tarde que no hacerlo."
}


def refran_al_azar():
    """Devuelve una pareja (refran, significado) elegida al azar."""
    return random.choice(list(REFRANES.items()))


def decir_refran(introduccion="Como decia la abuela:"):
    """Muestra un refran al azar con su significado."""
    refran, significado = refran_al_azar()

    print()
    print(f"  {introduccion}")
    print(f'     "{refran}"')
    print(f"     (Es decir: {significado})")
    print()


def decir_refran_especifico(refran):
    """Muestra un refran en particular con su significado."""
    print()
    print(f'  La abuela diria: "{refran}"')
    print(f"     (Es decir: {REFRANES[refran]})")
    print()


# ==========================================================
# PARTE 1: ENTRADA Y SALIDA BASICA
# ==========================================================
def parte_uno_entrada_salida():
    """Pide datos al usuario con input() y los muestra con print()."""

    print("=" * 50)
    print("  PARTE 1: Entrada y salida basica")
    print("=" * 50)

    decir_refran("Antes de empezar, la abuela dice:")

    # input() pide informacion al usuario.
    nombre = input("Hola! Como te llamas? ")

    # Este bloque evita que el programa se cierre si escribimos algo
    # que no sea un numero.
    # Si escribimos "veinte" sin try/except, apareceria ValueError
    # y el programa se detendria.
    try:
        edad = int(input("Cuantos anos tienes? "))
    except ValueError:
        print("Eso no parece un numero. Usare 0 como edad.")
        edad = 0

    comida = input("Cual es tu comida favorita? ")

    # SALIDA: mostramos los datos
    print()
    print(f"Mucho gusto, {nombre}!")

    # Podemos escribir los acentos normalmente porque usamos UTF-8.
    print("Tienes", edad, "anos.")
    print("Tu comida favorita es " + comida + ".")

    anos_para_100 = 100 - edad
    print(f"Te faltan {anos_para_100} anos para cumplir 100.")

    # DECISIONES (if / elif / else)
    if edad >= 60:
        decir_refran_especifico("Agua que no has de beber, dejala correr.")
    elif edad >= 18:
        decir_refran_especifico("Uno pone y Dios dispone.")
    else:
        decir_refran_especifico("Haz el bien y no mires a quien.")

    return nombre


# ==========================================================
# PARTE 2 (EXTRA): CONSUMIR UNA API JSON
# ==========================================================
# Esta API permite solicitar informacion de usuarios.
# Recibe los datos en formato JSON y podemos mostrarlos en Python.
def parte_dos_api_json(nombre):
    """Consulta una API publica que responde en formato JSON."""

    print()
    print("=" * 50)
    print("  PARTE 2 (EXTRA): Usando una API JSON")
    print("=" * 50)

    url_base = "https://jsonplaceholder.typicode.com/users/"

    entrada = input("Elige un numero de usuario del 1 al 10: ")

    if not entrada.isdigit():
        print("Debes escribir un numero. Terminando esta parte.")
        return

    url = url_base + entrada
    print(f"Consultando: {url}")

    try:
        with urllib.request.urlopen(url, timeout=10) as respuesta:
            texto_json = respuesta.read().decode("utf-8")

        datos = json.loads(texto_json)

        if not datos:
            print("No se encontro ese usuario.")
            return

        print()
        print(f"Resultado para {nombre}:")
        print("-" * 30)
        print(f"Nombre completo : {datos['name']}")
        print(f"Usuario         : {datos['username']}")
        print(f"Correo          : {datos['email']}")

        # Datos anidados: un diccionario dentro de otro.
        print(f"Ciudad          : {datos['address']['city']}")
        print(f"Empresa         : {datos['company']['name']}")

        print()
        print("Direccion en formato JSON:")
        print(json.dumps(datos["address"], indent=2, ensure_ascii=False))

        decir_refran_especifico("Haz el bien y no mires a quien.")

    except urllib.error.HTTPError as error:
        print(f"Error del servidor: codigo {error.code}")
        decir_refran_especifico("Uno pone y Dios dispone.")

    except urllib.error.URLError as error:
        print(f"No se pudo conectar a internet: {error.reason}")
        decir_refran_especifico("Uno pone y Dios dispone.")

    except json.JSONDecodeError:
        print("La respuesta no tiene un formato JSON valido.")
        decir_refran_especifico("Agua que no has de beber, dejala correr.")


# ==========================================================
# PARTE 3: JUEGO "COMPLETA EL REFRAN"
# ==========================================================
def parte_tres_juego_refranes():
    """Muestra la primera mitad de un refran y el usuario adivina la otra."""

    print()
    print("=" * 50)
    print("  PARTE 3: Completa el refran de la abuela")
    print("=" * 50)

    refran, _ = refran_al_azar()

    palabras = refran.split()
    mitad = len(palabras) // 2
    primera_parte = " ".join(palabras[:mitad])
    segunda_parte = " ".join(palabras[mitad:])

    print(f'La abuela empieza: "{primera_parte} ..."')
    intento = input("Como sigue? ")

    limpio_intento = intento.lower().strip().rstrip(".")
    limpio_correcto = segunda_parte.lower().strip().rstrip(".")

    if limpio_intento == limpio_correcto:
        print("Muy bien! La abuela estaria orgullosa.")
    else:
        print("Casi! El refran completo es:")
        print(f'   "{refran}"')


# ==========================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================================
def main():
    """Funcion principal: ejecuta las partes en orden."""
    nombre = parte_uno_entrada_salida()

    respuesta = input("\nQuieres probar la parte extra con la API? (si/no): ")
    if respuesta.lower().strip() in ("si", "s", "yes", "y"):
        parte_dos_api_json(nombre)
    else:
        print("Esta bien, saltamos la parte extra.")
        decir_refran_especifico("Agua que no has de beber, dejala correr.")

    respuesta = input("Quieres jugar a completar un refran? (si/no): ")
    if respuesta.lower().strip() in ("si", "s", "yes", "y"):
        parte_tres_juego_refranes()

    decir_refran("Para despedirnos, la abuela dice:")
    print(f"Fin del programa. Hasta luego, {nombre}!")


# Ejecuta main() solo si corremos este archivo directamente.
if __name__ == "__main__":
    main()