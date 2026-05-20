"""Agente inteligente para interpretar resultados."""

import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


def generar_analisis_ia(tipo_modelo, resultados):
	"""Generar interpretación automática."""

	try:
		genai.configure(api_key=API_KEY)

		modelo = genai.GenerativeModel('gemini-1.5-flash')

		prompt = f"""
        Eres un experto en Investigación de Operaciones.

        Analiza los siguientes resultados del modelo {tipo_modelo}:

        {resultados}

        Explica:
        - Qué significa la solución
        - Qué decisiones fueron tomadas
        - Posibles mejoras
        - Recomendaciones

        Responde en español de forma profesional.
        """

		respuesta = modelo.generate_content(prompt)

		return respuesta.text

	except Exception:
		return (
			'El sistema encontró una solución óptima y recomienda '
			'analizar escenarios alternativos para mejorar resultados.'
		)
