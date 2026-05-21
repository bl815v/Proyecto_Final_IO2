"""Modelo de selección de proyectos de inversión."""

import pandas as pd
import pulp


def resolver_modelo_proyectos():
	"""Resolver modelo de proyectos."""

	modelo = pulp.LpProblem('Seleccion_Proyectos', pulp.LpMaximize)

	# Variables binarias
	z_a = pulp.LpVariable('z_a', cat='Binary')
	z_b = pulp.LpVariable('z_b', cat='Binary')
	z_g = pulp.LpVariable('z_g', cat='Binary')
	z_d = pulp.LpVariable('z_d', cat='Binary')

	# Variables continuas
	inv_a = pulp.LpVariable('inv_a', lowBound=0, cat='Continuous')
	inv_b = pulp.LpVariable('inv_b', lowBound=0, cat='Continuous')
	inv_g = pulp.LpVariable('inv_g', lowBound=0, cat='Continuous')
	inv_d = pulp.LpVariable('inv_d', lowBound=0, cat='Continuous')

	# Función objetivo
	modelo += (
		0.15 * inv_a
		+ 0.18 * inv_b
		+ 0.12 * inv_g
		+ 0.20 * inv_d
		- 10000 * z_a
		- 15000 * z_b
		- 8000 * z_g
		- 20000 * z_d
	)

	# Restricción de presupuesto
	modelo += (
		10000 * z_a + 15000 * z_b + 8000 * z_g + 20000 * z_d + inv_a + inv_b + inv_g + inv_d
		<= 200000
	)

	# Exclusión Alpha-Delta
	modelo += z_a + z_d <= 1

	# Límites de inversión
	modelo += inv_a >= 20000 * z_a
	modelo += inv_a <= 80000 * z_a

	modelo += inv_b >= 30000 * z_b
	modelo += inv_b <= 100000 * z_b

	modelo += inv_g >= 15000 * z_g
	modelo += inv_g <= 60000 * z_g

	modelo += inv_d >= 50000 * z_d
	modelo += inv_d <= 120000 * z_d

	modelo.solve()

	tabla = pd.DataFrame(
		{
			'Proyecto': ['Alpha', 'Beta', 'Gamma', 'Delta'],
			'Seleccionado': [
				int(z_a.varValue),
				int(z_b.varValue),
				int(z_g.varValue),
				int(z_d.varValue),
			],
			'Inversión': [inv_a.varValue, inv_b.varValue, inv_g.varValue, inv_d.varValue],
		}
	)

	seleccionados = int(z_a.varValue) + int(z_b.varValue) + int(z_g.varValue) + int(z_d.varValue)

	return {
		'beneficio': round(pulp.value(modelo.objective), 2),
		'tabla': tabla,
		'metricas': [
			{'titulo': 'ROI neto máximo', 'valor': (f'${pulp.value(modelo.objective):,.0f}')},
			{'titulo': 'Proyectos seleccionados', 'valor': seleccionados},
		],
	}
