
import requests

def obtener_coordenadas(nombre_ciudad):
    """
    Consulta la API Open-Meteo Geocoding para obtener
    la latitud y longitud de una ciudad dada.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    parametros = {
        "name": nombre_ciudad,
        "count": 1,
        "language": "es",
        "format": "json"
    }

    try:
        # Hacemos la solicitud con un limite de tiempo de 10 segundos
        respuesta = requests.get(url, params=parametros, timeout=10)
        respuesta.raise_for_status()

        datos = respuesta.json()

        # Verificamos si encontramos resultados
        if "results" not in datos or not datos["results"]:
            print(f"No se encontro la ubicacion: '{nombre_ciudad}'.")
            return None

        # Extraemos los datos del primer resultado
        lugar = datos["results"][0]
        info_lugar = {
            "nombre": lugar.get("name"),
            "pais": lugar.get("country", "Desconocido"),
            "lat": lugar.get("latitude"),
            "lon": lugar.get("longitude")
        }

        return info_lugar

    except requests.exceptions.RequestException as e:
        print("Error de conexion: No se pudo contactar al servidor de la API.")
        return None


# Probamos la funcion
resultado = obtener_coordenadas("Paris")

if resultado:
    print("Ubicacion encontrada:")
    print(f"Ciudad: {resultado['nombre']}")
    print(f"Pais: {resultado['pais']}")
    print(f"Latitud: {resultado['lat']}")
    print(f"Longitud: {resultado['lon']}")
