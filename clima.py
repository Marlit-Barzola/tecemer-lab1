import requests 
import json
URL = "https://api.open-meteo.com/v1/forecast"
PARAMETROS = {
"latitude": -12.07, # Huancayo
"longitude": -75.21,
"daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
"timezone": "America/Lima",
"forecast_days": 7,
}
try:
    respuesta = requests.get(URL, params=PARAMETROS, timeout=5)
    respuesta.raise_for_status()
    datos = respuesta.json()
except requests.exceptions.RequestException as error:
    raise SystemExit(f'No se pudo obtener el pronóstico: {error}')
print(json.dumps(datos["daily"], indent=2, ensure_ascii=False))
print('Claves de primer nivel:', list(datos.keys()))
print('Claves de "daily":', list(datos["daily"].keys()))
print('Tipo de temperature_2m_max:', type(datos["daily"]["temperature_2m_max"]))
print('Primer valor de tiempo:', datos["daily"]["time"][0])