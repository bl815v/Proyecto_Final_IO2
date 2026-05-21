"""Aplicación principal del sistema inteligente MIP."""

import streamlit as st

from core.modelo_bodegas import resolver_modelo_bodegas
from core.modelo_manufactura import resolver_modelo_manufactura
from core.modelo_proyectos import resolver_modelo_proyectos
from ia.agente import generar_analisis_ia

st.set_page_config(page_title='Sistema Inteligente MIP', page_icon='📊', layout='wide')

with open('styles.css', encoding='utf-8') as css_file:
	st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)

st.title('Sistema Inteligente de Optimización de Programación Entera Mixta (MIP)')

st.sidebar.title('Módulos')

modulo = st.sidebar.radio(
	'Seleccionar problema',
	[
		'Expansión de bodegas logísticas',
		'Selección de proyectos de inversión',
		'Producción manufacturera',
	],
)


def cargar_markdown(ruta):
	"""Cargar contenido markdown."""

	with open(ruta, encoding='utf-8') as archivo:
		return archivo.read()


if 'resultados' not in st.session_state:
	st.session_state.resultados = {}

if 'analisis' not in st.session_state:
	st.session_state.analisis = {}


def ejecutar_modelo(nombre_modulo, funcion_modelo, tipo_ia):
	"""Ejecutar modelo."""

	with st.spinner('Resolviendo modelo matemático...'):
		resultados = funcion_modelo()

	with st.spinner('Generando análisis inteligente...'):
		analisis = generar_analisis_ia(tipo_ia, resultados)

	st.session_state.resultados[nombre_modulo] = resultados
	st.session_state.analisis[nombre_modulo] = analisis


def mostrar_resultados(nombre_modulo):
	"""Mostrar resultados almacenados."""

	resultados = st.session_state.resultados[nombre_modulo]
	analisis = st.session_state.analisis[nombre_modulo]

	metricas = resultados['metricas']

	col1, col2 = st.columns(2)

	with col1:
		st.metric(metricas[0]['titulo'], metricas[0]['valor'])

	with col2:
		st.metric(metricas[1]['titulo'], metricas[1]['valor'])

	st.subheader('Resultados del Modelo')
	st.dataframe(resultados['tabla'], width='stretch')

	st.subheader('Interpretación Inteligente')
	st.info(analisis)


if modulo == 'Expansión de bodegas logísticas':
	st.markdown(cargar_markdown('docs/bodegas.md'))

	if st.button('Resolver modelo', key='bodegas_btn'):
		ejecutar_modelo('bodegas', resolver_modelo_bodegas, 'expansión de bodegas logísticas')

	if 'bodegas' in st.session_state.resultados:
		mostrar_resultados('bodegas')


elif modulo == 'Selección de proyectos de inversión':
	st.markdown(cargar_markdown('docs/proyectos.md'))

	if st.button('Resolver modelo', key='proyectos_btn'):
		ejecutar_modelo(
			'proyectos', resolver_modelo_proyectos, 'selección de proyectos de inversión'
		)

	if 'proyectos' in st.session_state.resultados:
		mostrar_resultados('proyectos')


elif modulo == 'Producción manufacturera':
	st.markdown(cargar_markdown('docs/manufactura.md'))

	if st.button('Resolver modelo', key='manufactura_btn'):
		ejecutar_modelo('manufactura', resolver_modelo_manufactura, 'producción manufacturera')

	if 'manufactura' in st.session_state.resultados:
		mostrar_resultados('manufactura')
