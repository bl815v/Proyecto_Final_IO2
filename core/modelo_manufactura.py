"""Modelo de manufactura."""

import pandas as pd
import pulp


def resolver_modelo_manufactura():
	"""Resolver modelo manufacturero."""

	modelo = pulp.LpProblem('Manufactura', pulp.LpMaximize)

	mesas = pulp.LpVariable('Mesas', lowBound=0, cat='Integer')

	sillas = pulp.LpVariable('Sillas', lowBound=0, cat='Integer')

	horas_extra = pulp.LpVariable('Horas_Extra', lowBound=0, cat='Continuous')

	modelo += 80 * mesas + 50 * sillas - 20 * horas_extra

	modelo += 4 * mesas + 2 * sillas <= 240 + horas_extra

	modelo += horas_extra <= 40

	modelo.solve()

	tabla = pd.DataFrame(
		{'Producto': ['Mesas', 'Sillas'], 'Cantidad': [mesas.varValue, sillas.varValue]}
	)

	return {
		'ganancia': pulp.value(modelo.objective),
		'produccion_total': mesas.varValue + sillas.varValue,
		'tabla': tabla,
	}
