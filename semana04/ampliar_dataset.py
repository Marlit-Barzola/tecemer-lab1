import datetime as dt
import pandas as pd
import requests
# Mismas coordenadas usadas en el Laboratorio 02 (Huancayo)
LATITUD, LONGITUD = -12.07, -75.21
DIAS_HISTORIAL = 90 # cuántos días hacia atrás se consultan
DIAS_REZAGO = 5 # el archivo histórico de Open-Meteo tiene algunos días de rezago
fecha_fin = dt.date.today() - dt.timedelta(days=DIAS_REZAGO)
fecha_inicio = fecha_fin - dt.timedelta(days=DIAS_HISTORIAL)
url = "https://archive-api.open-meteo.com/v1/archive"
parametros = {
"latitude": LATITUD,
"longitude": LONGITUD,
"start_date": fecha_inicio.isoformat(),
"end_date": fecha_fin.isoformat(),
"daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
"timezone": "auto",
}
try:
    respuesta = requests.get(url, params=parametros, timeout=15)
    respuesta.raise_for_status()
except requests.exceptions.RequestException as error:
    print(f"No se pudo consultar la API histórica de Open-Meteo: {error}")
    raise SystemExit(1)
datos = respuesta.json()["daily"]
df_historico = pd.DataFrame({
"fecha": datos["time"],
"temp_max": datos["temperature_2m_max"],
"temp_min": datos["temperature_2m_min"],
"precipitacion": datos["precipitation_sum"],
})
# Sobrescribe el CSV copiado en el Paso 1.3 con el historial ampliado
df_historico.to_csv("pronostico_huancayo.csv", index=False)
print(f"Rango consultado: {fecha_inicio} a {fecha_fin}")
print(f"Filas obtenidas: {len(df_historico)}")
print("\nArchivo pronostico_huancayo.csv actualizado con historial ampliado.")
import pandas as pd
df = pd.read_csv("pronostico_huancayo.csv")
n_lluvioso = (df["precipitacion"] > 0).sum()
n_no_lluvioso = (df["precipitacion"] == 0).sum()
print(f"Total de filas: {len(df)}")
print(f"Días lluviosos: {n_lluvioso} | Días no lluviosos: {n_no_lluvioso}")
assert len(df) >= 30, "Muy pocas filas; aumenta DIAS_HISTORIAL en ampliar_dataset.py"
assert n_lluvioso >= 5 and n_no_lluvioso >= 5, "Alguna clase tiene muy pocos casos; amplía el rango de fechas"
print("Dataset ampliado validado correctamente.")