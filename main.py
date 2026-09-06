import requests

try:
    # Todo este bloque debe tener sangría (indentación)
    respuesta = requests.get(
        "https://official-joke-api.appspot.com/random_joke", timeout=5
    )
    respuesta.raise_for_status()
    datos = respuesta.json()
    print(datos["setup"])
    print(datos["punchline"])
except requests.RequestException as error:
    # Esta línea también debe tener sangría
    print(f"No se pudo obtener el chiste: {error}")