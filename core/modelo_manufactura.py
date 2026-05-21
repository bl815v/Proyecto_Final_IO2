"""Modelo de producción manufacturera."""

import pandas as pd
import pulp


def resolver_modelo_manufactura():
	"""Resolver modelo manufacturero."""

	modelo = pulp.LpProblem('Produccion_Manufacturera', pulp.LpMaximize)

	# Variables binarias
	w1 = pulp.LpVariable('w1', cat='Binary')
	w2 = pulp.LpVariable('w2', cat='Binary')

	# Variables continuas
	pa1 = pulp.LpVariable('pa1', lowBound=0, cat='Continuous')
	pb1 = pulp.LpVariable('pb1', lowBound=0, cat='Continuous')
	pc1 = pulp.LpVariable('pc1', lowBound=0, cat='Continuous')
	pa2 = pulp.LpVariable('pa2', lowBound=0, cat='Continuous')
	pb2 = pulp.LpVariable('pb2', lowBound=0, cat='Continuous')
	pc2 = pulp.LpVariable('pc2', lowBound=0, cat='Continuous')

	# Función objetivo
	modelo += 120 * (pa1 + pa2) + 150 * (pb1 + pb2) + 90 * (pc1 + pc2) - 5000 * w1 - 6000 * w2

	# Restricciones línea 1
	modelo += 2 * pa1 + 3 * pb1 + 1 * pc1 <= 300 * w1

	# Restricciones línea 2
	modelo += 1.5 * pa2 + 2 * pb2 + 2.5 * pc2 <= 250 * w2

	# Demandas máximas
	modelo += pa1 + pa2 <= 80
	modelo += pb1 + pb2 <= 60
	modelo += pc1 + pc2 <= 100

	modelo.solve()

	tabla = pd.DataFrame(
		{
			'Producto': [
				'A - Línea 1',
				'B - Línea 1',
				'C - Línea 1',
				'A - Línea 2',
				'B - Línea 2',
				'C - Línea 2',
			],
			'Producción': [
				pa1.varValue,
				pb1.varValue,
				pc1.varValue,
				pa2.varValue,
				pb2.varValue,
				pc2.varValue,
			],
		}
	)

	return {
		'ganancia': round(pulp.value(modelo.objective), 2),
		'tabla': tabla,
		'metricas': [
			{'titulo': 'Ganancia máxima', 'valor': (f'${pulp.value(modelo.objective):,.0f}')},
			{'titulo': 'Líneas activas', 'valor': int(w1.varValue + w2.varValue)},
		],
	}
