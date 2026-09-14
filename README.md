# tecemer-lab1
Proyecto de práctica de la Semana 1 del curso Tecnologías Emergentes (ISO46B) — UNCP.
Consume una API pública de chistes como ejercicio de configuración de entorno.
# tecemer-lab1(2)
Proyecto de práctica de la semana 2 del curso Tecnologías Emergentes (ISO46B) — UNCP.
Consume la libreria numpy, una API meterologica, la instalación de pandas.
## Instalación

bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
## Numpy
.venv/Scripts/pip install numpy
.venv/Scripts/pip freeze > requirements.txt
## Pandas
.venv/Scripts/pip install pandas
.venv/Scripts/pip freeze > requirements.txt
## Uso

bash
python -m tecemer_lab1.app


## Estructura del repositorio

tecemer-lab1/
├── .venv/                              # Entorno virtual de Python
├── numpy_demo.py                       # Demostración de NumPy y benchmarks
├── clima.py                            # Extracción de API Open-Meteo y generación de CSV/JSON
├── analisis.py                         # Análisis de datos, transformaciones y resumen con Pandas
├── pronostico_huancayo.json            # Respuesta JSON cruda de la API
├── pronostico_huancayo.csv             # Datos extraídos formateados en CSV
├── pronostico_huancayo_procesado.csv   # Dataset procesado con columnas calculadas
├── resumen_por_categoria.csv           # Resumen estadístico agrupado por categoría
├── requirements.txt                    # Lista de dependencias del proyecto
└── README.md                           # Documentación del proyecto


## Autor

Curso: Tecnologías Emergentes (ISO46B) — Facultad de Ingeniería de Sistemas, UNCP.


