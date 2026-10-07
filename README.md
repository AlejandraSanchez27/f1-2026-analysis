# 🏎️ F1 2026 Analysis
Proyecto de análisis de datos de Fórmula 1 desarrollado con Python. El proyecto recopila, procesa y organiza información de la temporada 2026 para analizar resultados de carreras, sprints, calendario, campeonatos, pilotos, constructores y estrategias de carrera.

El proyecto utiliza la API **Jolpica-F1** para obtener datos estructurados de Fórmula 1 y **FastF1** para trabajar con datos de sesiones y telemetría.

## 🎯 Objetivo
Construir un proyecto de analítica deportiva que permita recopilar y analizar datos de Fórmula 1 mediante Python, utilizando herramientas de procesamiento de datos y fuentes públicas.

El proyecto busca servir como base para futuros análisis de rendimiento de pilotos, equipos y estrategias de carrera.

## 📊 Datos analizados
El proyecto trabaja con diferentes tipos de información de la temporada 2026:

- Calendario de carreras.
- Resultados de Grandes Premios.
- Resultados de carreras Sprint.
- Clasificación del campeonato de pilotos.
- Clasificación del campeonato de constructores.
- Resultados por piloto.
- Estrategias de neumáticos.
- Paradas en boxes.
- Datos de vueltas y sesiones.
- Datos de telemetría mediante FastF1.

## 🔌 Fuentes de datos
*Jolpica-F1*

Se utiliza la API **Jolpica-F1** para consultar información estructurada de la temporada de Fórmula 1.

La API utiliza endpoints compatibles con la estructura de Ergast, por lo que las rutas pueden contener `/ergast/f1`, aunque la fuente utilizada por el proyecto es Jolpica-F1.

Documentación:

https://api.jolpi.ca/docs/

*FastF1*

Se utiliza la biblioteca FastF1 para acceder a datos de sesiones de Fórmula 1, incluyendo información de vueltas, pilotos, neumáticos, posiciones, clima, mensajes de control de carrera y telemetría.

Documentación:

https://docs.fastf1.dev/

## 🛠️ Tecnologías utilizadas

- Python
- pandas
- Requests
- FastF1
- Matplotlib
- VS Code
- CSV
- Excel

## 📁 Estructura del proyecto

```text
f1-2026-analysis/
│
├── assets/
│
├── data/
│   ├── all_results_2026.csv
│   ├── championship_2026.csv
│   ├── constructors_2026.csv
│   ├── schedule_2026.csv
│   ├── sprints_results_2026.csv
│   ├── strategy_all_races_2026.csv
│   └── strategy_australia_2026.csv
│
├── excel/
│   └── Archivos Excel generados durante el análisis
│
├── scripts/
│   ├── all_results_races.py
│   ├── all_results_sprints.py
│   ├── constructors.py
│   ├── data_loader.py
│   ├── drivers.py
│   ├── main.py
│   ├── results.py
│   ├── schedule.py
│   ├── season_classification.py
│   └── telemetry.py
│
├── .gitignore
└── README.md

```
**Autora**
*Alejandra Sanchez Vega*
*Estudiante de Ingeniería Informática interesada en analítica de datos y análisis deportivo.*
