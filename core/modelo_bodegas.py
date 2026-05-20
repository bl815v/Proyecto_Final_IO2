"""Modelo de optimización de bodegas."""

import pandas as pd
import pulp


def resolver_modelo_bodegas():
	"""Resolver el modelo de bodegas."""

	modelo = pulp.LpProblem('Optimizacion_Bodegas', pulp.LpMaximize)

	x_bog = pulp.LpVariable('Toneladas_Bogota', lowBound=0, cat='Continuous')

	y_bog = pulp.LpVariable('Abrir_Bogota', cat='Binary')

	x_med = pulp.LpVariable('Toneladas_Medellin', lowBound=0, cat='Continuous')

	y_med = pulp.LpVariable('Abrir_Medellin', cat='Binary')

	modelo += 120 * x_bog + 100 * x_med - 10000 * y_bog - 8000 * y_med

	modelo += x_bog <= 200 * y_bog
	modelo += x_med <= 180 * y_med
	modelo += x_bog + x_med <= 300

	modelo.solve()

	tabla = pd.DataFrame(
		{
			'Ciudad': ['Bogotá', 'Medellín'],
			'Toneladas': [x_bog.varValue, x_med.varValue],
			'Abierta': [y_bog.varValue, y_med.varValue],
		}
	)

	return {
		'ganancia': pulp.value(modelo.objective),
		'bodegas_abiertas': int(y_bog.varValue + y_med.varValue),
		'tabla': tabla,
	}
