"""Modelo de expansión de bodegas logísticas."""

import pandas as pd
import pulp


def resolver_modelo_bodegas():
	"""Resolver modelo de expansión de bodegas."""

	modelo = pulp.LpProblem('Expansion_Bodegas', pulp.LpMaximize)

	# Variables binarias
	y_bog = pulp.LpVariable('y_bog', cat='Binary')
	y_med = pulp.LpVariable('y_med', cat='Binary')
	y_cal = pulp.LpVariable('y_cal', cat='Binary')

	# Variables continuas
	x_bog = pulp.LpVariable('x_bog', lowBound=0, cat='Continuous')
	x_med = pulp.LpVariable('x_med', lowBound=0, cat='Continuous')
	x_cal = pulp.LpVariable('x_cal', lowBound=0, cat='Continuous')

	# Función objetivo
	modelo += (
		300 * x_bog + 350 * x_med + 280 * x_cal - 50000 * y_bog - 40000 * y_med - 35000 * y_cal
	)

	# Restricción de presupuesto
	modelo += 50000 * y_bog + 40000 * y_med + 35000 * y_cal <= 100000

	# Máximo de aperturas
	modelo += y_bog + y_med + y_cal <= 2

	# Demanda mínima
	modelo += x_bog + x_med + x_cal >= 180

	# Restricciones de capacidad
	modelo += x_bog <= 200 * y_bog
	modelo += x_med <= 150 * y_med
	modelo += x_cal <= 100 * y_cal

	modelo.solve()

	tabla = pd.DataFrame(
		{
			'Ciudad': ['Bogotá', 'Medellín', 'Cali'],
			'Toneladas almacenadas': [x_bog.varValue, x_med.varValue, x_cal.varValue],
			'Bodega abierta': [int(y_bog.varValue), int(y_med.varValue), int(y_cal.varValue)],
		}
	)

	return {
		'ganancia': round(pulp.value(modelo.objective), 2),
		'tabla': tabla,
		'metricas': [
			{'titulo': 'Ganancia máxima', 'valor': (f'${pulp.value(modelo.objective):,.0f}')},
			{
				'titulo': 'Bodegas abiertas',
				'valor': int(y_bog.varValue + y_med.varValue + y_cal.varValue),
			},
		],
	}
