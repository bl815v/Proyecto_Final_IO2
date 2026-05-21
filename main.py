"""Aplicación principal del sistema inteligente MIP."""

import streamlit as st

from core.modelo_bodegas import resolver_modelo_bodegas
from core.modelo_manufactura import resolver_modelo_manufactura
from core.modelo_proyectos import resolver_modelo_proyectos
from ia.agente import generar_analisis_ia

st.set_page_config(
	page_title='Sistema Inteligente MIP',
	page_icon='📊',
	layout='wide',
)

with open('styles.css', encoding='utf-8') as css_file:
	st.markdown(
		f'<style>{css_file.read()}</style>',
		unsafe_allow_html=True,
	)

st.markdown(
	"""
    <h1 class="main-title">
        Sistema Inteligente de Optimización de
        Programación Entera Mixta (MIP)
    </h1>
    """,
	unsafe_allow_html=True,
)

st.sidebar.title('Módulos')

modulo = st.sidebar.segmented_control(
	'Seleccionar problema',
	[
		'Expansión de bodegas logísticas',
		'Selección de proyectos de inversión',
		'Producción manufacturera',
	],
	selection_mode='single',
	default='Expansión de bodegas logísticas',
)


def cargar_markdown(ruta):
	"""Cargar contenido markdown."""

	with open(ruta, encoding='utf-8') as archivo:
		return archivo.read()


if 'resultados' not in st.session_state:
	st.session_state.resultados = {}

if 'analisis' not in st.session_state:
	st.session_state.analisis = {}

if 'procesando_ia' not in st.session_state:
	st.session_state.procesando_ia = False


def formatear_numero(valor):
	"""Formatear números al estilo colombiano."""

	if isinstance(valor, (int, float)):
		texto = f'{valor:,.2f}'
	else:
		texto = str(valor)

	return texto.replace(',', 'X').replace('.', ',').replace('X', '.')


def mostrar_tabla(tabla):
	"""Mostrar tabla formateada."""

	try:
		df_formateado = tabla.style.format(
			thousands='.',
			decimal=',',
		)

		st.dataframe(
			df_formateado,
			width='stretch',
			hide_index=True,
		)

	except Exception:
		st.dataframe(
			tabla,
			width='stretch',
			hide_index=True,
		)


def mostrar_resultados(nombre_modulo):
	"""Mostrar resultados."""

	resultados = st.session_state.resultados[nombre_modulo]

	metricas = resultados['metricas']

	col1, col2 = st.columns(2)

	with col1:
		st.metric(
			metricas[0]['titulo'],
			formatear_numero(metricas[0]['valor']),
		)

	with col2:
		st.metric(
			metricas[1]['titulo'],
			formatear_numero(metricas[1]['valor']),
		)

	st.subheader('Resultados del Modelo')

	mostrar_tabla(resultados['tabla'])

	# Mostrar IA si ya existe
	if nombre_modulo in st.session_state.analisis:
		st.subheader('Interpretación Inteligente')

		st.info(st.session_state.analisis[nombre_modulo])

	# Mostrar spinner si sigue generando
	elif st.session_state.procesando_ia:
		st.subheader('Interpretación Inteligente')

		st.info('Generando análisis inteligente...')


def ejecutar_modelo(nombre_modulo, funcion_modelo, tipo_ia):
	"""Ejecutar modelo y análisis IA."""

	# Resolver modelo
	resultados = funcion_modelo()

	st.session_state.resultados[nombre_modulo] = resultados

	# Marcar IA en proceso
	st.session_state.procesando_ia = True

	# Forzar rerender inmediato
	st.rerun()

	# Esta parte NO se ejecutará tras rerun


def ejecutar_ia(nombre_modulo, tipo_ia):
	"""Generar análisis IA."""

	if (
		nombre_modulo in st.session_state.resultados
		and nombre_modulo not in st.session_state.analisis
	):
		analisis = generar_analisis_ia(
			tipo_ia,
			st.session_state.resultados[nombre_modulo],
		)

		st.session_state.analisis[nombre_modulo] = analisis

		st.session_state.procesando_ia = False

		st.rerun()


if modulo == 'Expansión de bodegas logísticas':
	st.markdown(cargar_markdown('docs/bodegas.md'))

	if st.button(
		'Resolver modelo',
		key='bodegas_btn',
	):
		ejecutar_modelo(
			'bodegas',
			resolver_modelo_bodegas,
			'expansión de bodegas logísticas',
		)

	if 'bodegas' in st.session_state.resultados:
		mostrar_resultados('bodegas')

		if 'bodegas' not in st.session_state.analisis and st.session_state.procesando_ia:
			ejecutar_ia(
				'bodegas',
				'expansión de bodegas logísticas',
			)


elif modulo == 'Selección de proyectos de inversión':
	st.markdown(cargar_markdown('docs/proyectos.md'))

	if st.button(
		'Resolver modelo',
		key='proyectos_btn',
	):
		ejecutar_modelo(
			'proyectos',
			resolver_modelo_proyectos,
			'selección de proyectos de inversión',
		)

	if 'proyectos' in st.session_state.resultados:
		mostrar_resultados('proyectos')

		if 'proyectos' not in st.session_state.analisis and st.session_state.procesando_ia:
			ejecutar_ia(
				'proyectos',
				'selección de proyectos de inversión',
			)


elif modulo == 'Producción manufacturera':
	st.markdown(cargar_markdown('docs/manufactura.md'))

	if st.button(
		'Resolver modelo',
		key='manufactura_btn',
	):
		ejecutar_modelo(
			'manufactura',
			resolver_modelo_manufactura,
			'producción manufacturera',
		)

	if 'manufactura' in st.session_state.resultados:
		mostrar_resultados('manufactura')

		if 'manufactura' not in st.session_state.analisis and st.session_state.procesando_ia:
			ejecutar_ia(
				'manufactura',
				'producción manufacturera',
			)
