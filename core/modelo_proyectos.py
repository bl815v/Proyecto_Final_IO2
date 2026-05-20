"""Modelo de selección de proyectos."""

import pandas as pd
import pulp


def resolver_modelo_proyectos():
	"""Resolver modelo de proyectos."""

	modelo = pulp.LpProblem('Seleccion_Proyectos', pulp.LpMaximize)

	proyectos = {
		'A': {'beneficio': 10000, 'costo': 5000},
		'B': {'beneficio': 12000, 'costo': 7000},
		'C': {'beneficio': 8000, 'costo': 3000},
	}

	variables = {nombre: pulp.LpVariable(nombre, cat='Binary') for nombre in proyectos}

	modelo += pulp.lpSum(proyectos[p]['beneficio'] * variables[p] for p in proyectos)

	modelo += pulp.lpSum(proyectos[p]['costo'] * variables[p] for p in proyectos) <= 10000

	modelo.solve()

	seleccionados = []

	for proyecto, variable in variables.items():
		if variable.varValue == 1:
			seleccionados.append(proyecto)

	tabla = pd.DataFrame({'Proyecto': seleccionados})

	return {
		'beneficio': pulp.value(modelo.objective),
		'cantidad': len(seleccionados),
		'tabla': tabla,
	}
