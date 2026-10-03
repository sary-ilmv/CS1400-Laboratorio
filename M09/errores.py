"""
TAREA M09: Cazando errores en Macondo
Herramienta: el depurador (debugger) de VS Code
Nombre:

En esta tarea el código tiene errores (bugs) escondidos. Tu trabajo NO es
adivinar: es usar el depurador para ENCONTRAR la causa de cada error, explicarla
y corregirla.

======================================================================
 GUÍA RÁPIDA DEL DEPURADOR DE VS CODE
======================================================================

1. PUNTO DE INTERRUPCIÓN (breakpoint)
   Haz clic a la izquierda del número de una línea: aparece un punto rojo.
   (También con F9.) El programa se detendrá ANTES de ejecutar esa línea.

2. INICIAR EL DEPURADOR
   Menú Run > Start Debugging, o presiona F5. Si VS Code pregunta, elige
   "Python File" (Depurar archivo Python actual).
   Cuando se detiene, la línea amarilla es la que SE VA A ejecutar (aún no se
   ha ejecutado).

3. BARRA DE CONTROLES (arriba, en la ventana)
   Continue (F5)             : sigue hasta el próximo breakpoint o hasta el final
   Step Over (F10)           : ejecuta la línea actual y pasa a la siguiente
   Step Into (F11)           : si la línea llama a una función, ENTRA en ella
   Step Out (Shift+F11)      : termina la función actual y regresa a quien la llamó
   Restart (Ctrl/Cmd+Shift+F5): reinicia la depuración
   Stop (Shift+F5)           : detiene todo (úsalo si el programa no termina)

   En Mac, las teclas F pueden requerir fn (por ejemplo fn+F10), o simplemente
   haz clic en los botones de la barra.

4. PANELES (a la izquierda, en la vista "Run and Debug")
   VARIABLES   : muestra el valor actual de cada variable. ¡Es tu mejor amigo!
   WATCH       : escribe una expresión (por ejemplo len(lista)) y VS Code te
                 muestra su valor en cada paso.
   CALL STACK  : muestra qué función llamó a cuál.
   DEBUG CONSOLE (abajo): puedes escribir expresiones para probarlas.

======================================================================
 MÉTODO PARA CADA EJERCICIO (síguelo en orden)
======================================================================

 Paso 1. Descomenta la llamada del ejercicio en la sección
         "ZONA DE PRUEBAS" al final del archivo (una a la vez).
 Paso 2. Ejecuta el programa normalmente y LEE el resultado o el error.
 Paso 3. Pon un breakpoint antes de la línea que sospechas y presiona F5.
 Paso 4. Avanza con F10 / F11 observando el panel VARIABLES.
         Pregúntate: ¿este valor es el que yo esperaba?
 Paso 5. Completa el bloque "MI ANÁLISIS" del ejercicio.
 Paso 6. Corrige el código y vuelve a ejecutar para comprobarlo.

 Al final, ejecuta verificar() para ver cuántos ejercicios tienes bien.

 REGLA: no cambies los nombres de las funciones ni lo que reciben.
 Solo corrige el error dentro de ellas.
"""

import threading

# ---------------------------------------------------------------------
# DATOS (no los modifiques)
# ---------------------------------------------------------------------

personajes = [
    "José Arcadio Buendía",
    "Úrsula Iguarán",
    "Aureliano Buendía",
    "Remedios la Bella",
    "Melquíades",
]

rasgos = {
    "Úrsula": "longeva y trabajadora",
    "José Arcadio Buendía": "soñador e inventor",
    "Aureliano": "coronel de las guerras",
    "Remedios": "belleza que ascendió al cielo",
    "Melquíades": "gitano alquimista",
}

familia = [
    "Aureliano José",
    "Aureliano Segundo",
    "Arcadio",
    "Aureliano Babilonia",
    "Amaranta",
    "Aureliano Triste",
]

generaciones = {
    1: ["José Arcadio Buendía", "Úrsula Iguarán"],
    2: ["José Arcadio", "Aureliano", "Amaranta", "Rebeca"],
    3: ["Arcadio", "Aureliano José"],
    4: ["Remedios la Bella", "Aureliano Segundo", "José Arcadio Segundo"],
    5: ["Meme", "José Arcadio", "Amaranta Úrsula"],
    6: ["Aureliano Babilonia"],
    7: ["El niño con cola de cerdo"],
}


# =====================================================================
# CALENTAMIENTO: este código SÍ funciona. Úsalo para practicar el depurador.
# =====================================================================

def nombre_mas_largo(lista):
    mas_largo = ""
    for nombre in lista:
        if len(nombre) > len(mas_largo):
            mas_largo = nombre
    return mas_largo


# Instrucciones:
#  - Pon un breakpoint en la línea "if len(nombre) > len(mas_largo):".
#  - Presiona F5 y luego F5 de nuevo para avanzar una vuelta del ciclo.
#  - En cada vuelta observa en VARIABLES: nombre y mas_largo.

# TODO 1. ¿Cuántas veces cambió el valor de mas_largo durante el ciclo?
# TODO 2. ¿Cuál es el valor de len(nombre) en la tercera vuelta? (míralo en WATCH)
# TODO 3. ¿Qué hace el botón Step Over comparado con Step Into?


# =====================================================================
# EJERCICIO 1: Listas
# Debe devolver el ÚLTIMO personaje de la lista.
# =====================================================================

def ultimo_personaje(lista):
    posicion = len(lista)
    return lista[posicion]


# TODO
# 4. Error o resultado incorrecto obtenido:
# 5. Valor de posicion y de len(lista) en el depurador:
# 6. Cómo lo corregí:


# =====================================================================
# EJERCICIO 2: Diccionarios
# Debe devolver el nombre seguido de su rasgo, por ejemplo:
#   "Melquíades: gitano alquimista"
# =====================================================================

def describir(nombre):
    return nombre + ": " + rasgos[nombre.lower()]


# Pista del método: en WATCH escribe nombre.lower() y compáralo con las
# llaves del diccionario rasgos.
#
# 
# 7. Error o resultado incorrecto obtenido:
# 8. Valor de nombre.lower() y por qué no se encuentra en el diccionario:
# 9. Cómo lo corregí:


# =====================================================================
# EJERCICIO 3: Ciclo for
# Debe contar cuántos nombres de la lista empiezan con "Aureliano".
# =====================================================================

def contar_aurelianos(lista):
    contador = 0
    for i in range(1, len(lista)):
        if lista[i].startswith("Aureliano"):
            contador += 1
    return contador


# OJO: este ejercicio no da error, pero el resultado es incorrecto.
# Esos son los bugs más difíciles. Usa el depurador para ver qué valores
# toma la variable i en cada vuelta.
#
# 10. Error o resultado incorrecto obtenido (¿qué número esperaba y cuál obtuve?):
# 11. Primer valor de i en el depurador y qué elemento se saltó:
# 12. Cómo lo corregí:


# =====================================================================
# EJERCICIO 4: Ciclo while  (la peste del insomnio)
# En Macondo, la peste del insomnio hacía que la gente olvidara las cosas.
# Supón que 1 persona la tiene el primer día y cada día el número de
# afectados SE DUPLICA. Debe devolver cuántos días pasan hasta que los
# afectados llegan a ser al menos "habitantes".
# =====================================================================

def dias_de_insomnio(habitantes):
    olvidados = 0
    dias = 0
    while olvidados < habitantes:
        olvidados = olvidados * 2
        dias += 1
    return dias


# CUIDADO: si lo ejecutas normal, puede no terminar nunca (como el tiempo
# circular de Macondo). Ejecútalo SOLO dentro del depurador con un breakpoint
# dentro del while. Si se queda pegado, presiona Stop (Shift+F5).
#
# Presiona F10 varias veces y mira el panel VARIABLES.
#
# 13. ¿Qué valor tenía olvidados después de 5 vueltas?
# 14. ¿Por qué nunca se cumple la condición del while?
# 15. Cómo lo corregí:


# =====================================================================
# EJERCICIO 5: if / elif / else
# Debe devolver la etapa de vida de un personaje según su edad:
#   menos de 12: "niño" | 12 a 17: "adolescente"
#   18 a 59: "adulto"   | 60 o más: "anciano"
# =====================================================================

def etapa_de_vida(edad):
    if edad < 12:
        return "niño"
    if edad >= 12 or edad < 18:
        return "adolescente"
    if edad >= 18 and edad < 60:
        return "adulto"
    return "anciano"


# Prueba con edad = 30 y avanza con F10. ¿En qué línea entra el programa?
#

# 16. Error o resultado incorrecto obtenido:
# 17. ¿Qué línea se ejecutó que NO debía ejecutarse con edad = 30?
# 18. Cómo lo corregí:


# =====================================================================
# EJERCICIO 6: Operadores
# La lluvia en Macondo duró 4 años, 11 meses y 2 días. Esta función debe
# convertir cualquier duración a días totales (año = 365 días, mes = 30 días).
# Para 4 años, 11 meses y 2 días debe devolver 1792.
# =====================================================================

def dias_de_lluvia(anios, meses, dias):
    return anios * 365 + meses * 30 * dias


# Usa WATCH para evaluar por separado:  anios * 365   y   meses * 30 * dias
#
# 19. Error o resultado incorrecto obtenido:
# 20. Valor de cada parte de la suma en WATCH:
# 21. Cómo lo corregí:


# =====================================================================
# EJERCICIO 7: Funciones (return vs print)
# es_longevo debe devolver True si el promedio de las edades es mayor que 50.
# =====================================================================

def promedio_de_soledad(edades):
    total = 0
    for edad in edades:
        total += edad
    print(total / len(edades))


def es_longevo(edades):
    promedio = promedio_de_soledad(edades)
    if promedio > 50:
        return True
    else:
        return False


# Usa Step Into (F11) para entrar a promedio_de_soledad y mira el panel
# CALL STACK. Después, al regresar a es_longevo, mira el valor de promedio.
#
# 
# 22. Error o resultado incorrecto obtenido:
# 23. Valor de promedio dentro de es_longevo y por qué tiene ese valor:
# 24. Cómo lo corregí:


# =====================================================================
# RETO FINAL: dos errores escondidos, sin pistas
# Trabaja con el diccionario "generaciones" de la familia Buendía.
#   generacion_mas_numerosa: devuelve el NÚMERO de la generación con más
#                            personajes (debe devolver 2).
#   total_personajes:        devuelve cuántos personajes hay en total
#                            (debe devolver 16).
# =====================================================================

def generacion_mas_numerosa(gens):
    mayor = 0
    ganadora = 0
    for numero in gens:
        miembros = gens[numero]
        if len(miembros) > mayor:
            mayor = len(miembros)
        ganadora = numero
    return ganadora


def total_personajes(gens):
    total = 0
    for numero in gens:
        total = len(gens[numero])
    return total


# TODO (para cada una de las dos funciones):
# 25. Error o resultado incorrecto obtenido:
# 26. Variable que me dio la pista y su valor:
# 27. Cómo lo corregí:


# =====================================================================
# REFLEXIÓN FINAL
# 28. ¿Cuál error fue el más difícil de encontrar y por qué?
# 29. ¿Cuál herramienta del depurador te ayudó más
#   (Variables, Watch, Step Into, Call Stack)?
# 
# =====================================================================


# =====================================================================
# VERIFICACIÓN (no modifiques esta sección)
# =====================================================================

def _ejecutar(funcion, segundos=2):
    """Ejecuta funcion con límite de tiempo para detectar ciclos infinitos."""
    resultado = {}

    def tarea():
        try:
            resultado["valor"] = funcion()
        except Exception as error:
            resultado["error"] = type(error).__name__

    hilo = threading.Thread(target=tarea, daemon=True)
    hilo.start()
    hilo.join(segundos)
    if hilo.is_alive():
        return None, "tarda demasiado (¿ciclo infinito?)"
    return resultado.get("valor"), resultado.get("error")


def _revisar(nombre, funcion, esperado):
    valor, error = _ejecutar(funcion)
    if error:
        print(f"[FALLA] {nombre}: {error}")
        return 0
    if valor == esperado:
        print(f"[OK]    {nombre}")
        return 1
    print(f"[FALLA] {nombre}: el resultado no es el esperado")
    return 0


def verificar():
    print("--- VERIFICACIÓN ---")
    aciertos = 0
    aciertos += _revisar("Ejercicio 1", lambda: ultimo_personaje(personajes), "Melquíades")
    aciertos += _revisar("Ejercicio 2", lambda: describir("Melquíades"), "Melquíades: gitano alquimista")
    aciertos += _revisar("Ejercicio 3", lambda: contar_aurelianos(familia), 4)
    aciertos += _revisar("Ejercicio 4", lambda: dias_de_insomnio(100), 7)
    aciertos += _revisar(
        "Ejercicio 5",
        lambda: [etapa_de_vida(e) for e in (5, 15, 30, 80)],
        ["niño", "adolescente", "adulto", "anciano"],
    )
    aciertos += _revisar("Ejercicio 6", lambda: dias_de_lluvia(4, 11, 2), 1792)
    aciertos += _revisar(
        "Ejercicio 7",
        lambda: [es_longevo([60, 80, 100]), es_longevo([20, 30])],
        [True, False],
    )
    aciertos += _revisar("Reto final (a)", lambda: generacion_mas_numerosa(generaciones), 2)
    aciertos += _revisar("Reto final (b)", lambda: total_personajes(generaciones), 16)
    print(f"Resultado: {aciertos} de 9 correctos")


# =====================================================================
# ZONA DE PRUEBAS: descomenta UNA línea a la vez
# =====================================================================

if __name__ == "__main__":
    # print(nombre_mas_largo(personajes))            # Calentamiento
    # print(ultimo_personaje(personajes))            # Ejercicio 1
    # print(describir("Melquíades"))                 # Ejercicio 2
    # print(contar_aurelianos(familia))              # Ejercicio 3 (esperado: 4)
    # print(dias_de_insomnio(100))                   # Ejercicio 4 (esperado: 7)
    # print(etapa_de_vida(30))                       # Ejercicio 5 (esperado: adulto)
    # print(dias_de_lluvia(4, 11, 2))                # Ejercicio 6 (esperado: 1792)
    # print(es_longevo([60, 80, 100]))               # Ejercicio 7 (esperado: True)
    # print(generacion_mas_numerosa(generaciones))   # Reto (esperado: 2)
    # print(total_personajes(generaciones))          # Reto (esperado: 16)

    verificar()


# =====================================================================
# AL TERMINAR: guarda y sube tu trabajo a tu fork
#   git add .
#   git commit -m "Completé M09 depurador"
#   git push origin main        (o el nombre de tu rama)
# =====================================================================