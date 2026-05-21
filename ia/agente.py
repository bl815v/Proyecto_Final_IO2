"""Agente inteligente para interpretar resultados MIP."""

import json
import os

import google.generativeai as genai
import streamlit as st

API_KEY = st.secrets['GEMINI_API_KEY']

def generar_analisis_ia(tipo_modelo, resultados):
	"""Generar interpretación inteligente del modelo."""

	try:
		genai.configure(api_key=API_KEY)

		modelo = genai.GenerativeModel('gemini-2.5-flash')

		resultados_json = json.dumps(resultados, indent=2, ensure_ascii=False, default=str)

		prompt = f"""
Eres un experto senior en Investigación de Operaciones,
Programación Entera Mixta (MIP)
y optimización matemática.

Se resolvió el siguiente modelo:

TIPO DE MODELO:
{tipo_modelo}

RESULTADOS:
{resultados_json}

Realiza un análisis profesional y estructurado.

Tu respuesta debe incluir:

1. Interpretación general de la solución:
- Explica qué decisiones tomó el modelo.
- Explica por qué la solución encontrada es eficiente.
- Interpreta los resultados en términos prácticos.

2. Validación conceptual:
- Explica si las restricciones parecen cumplirse.
- Identifica restricciones críticas o activas.
- Explica qué factores limitaron la solución óptima.

3. Análisis de sensibilidad:
Propón 2 escenarios hipotéticos concretos.

Para cada escenario:
- explica qué cambiaría,
- predice cómo afectaría el objetivo,
- indica si la solución mejoraría o empeoraría.

4. Recomendaciones:
Sugiere mejoras realistas para el modelo:
- nuevas restricciones,
- variables adicionales,
- objetivos multicriterio,
- mejoras operativas.

5. Riesgos y limitaciones:
Explica:
- supuestos fuertes del modelo,
- limitaciones matemáticas,
- factores reales no considerados.

IMPORTANTE:
- Responde completamente en español.
- Usa lenguaje técnico pero entendible.
- Organiza la respuesta por secciones.
- No uses JSON.
- No inventes valores inexistentes.
- Sé analítico y profesional.
"""

		respuesta = modelo.generate_content(prompt)

		return respuesta.text

	except Exception as error:
		return f'No fue posible generar el análisis inteligente.\n\nError detectado: {error}'
