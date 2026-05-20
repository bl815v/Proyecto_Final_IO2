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
	'Seleccionar problema', ['Optimización de bodegas', 'Selección de proyectos', 'Manufactura']
)


if 'resultados' not in st.session_state:
	st.session_state.resultados = {}

if 'analisis' not in st.session_state:
	st.session_state.analisis = {}


def ejecutar_modelo(nombre_modulo, funcion_modelo, tipo_ia):
	"""Ejecutar modelo y guardar resultados."""

	with st.spinner('Resolviendo modelo matemático...'):
		resultados = funcion_modelo()

	with st.spinner('Generando interpretación inteligente...'):
		analisis = generar_analisis_ia(tipo_ia, resultados)

	st.session_state.resultados[nombre_modulo] = resultados
	st.session_state.analisis[nombre_modulo] = analisis


def mostrar_resultados(nombre_modulo):
	"""Mostrar resultados almacenados."""

	resultados = st.session_state.resultados[nombre_modulo]
	analisis = st.session_state.analisis[nombre_modulo]

	if nombre_modulo == 'bodegas':
		col1, col2 = st.columns(2)

		with col1:
			st.metric('Ganancia máxima', f'${resultados["ganancia"]:,.0f}')

		with col2:
			st.metric('Bodegas abiertas', resultados['bodegas_abiertas'])

	elif nombre_modulo == 'proyectos':
		col1, col2 = st.columns(2)

		with col1:
			st.metric('Beneficio total', f'${resultados["beneficio"]:,.0f}')

		with col2:
			st.metric('Proyectos seleccionados', resultados['cantidad'])

	elif nombre_modulo == 'manufactura':
		col1, col2 = st.columns(2)

		with col1:
			st.metric('Ganancia total', f'${resultados["ganancia"]:,.0f}')

		with col2:
			st.metric('Producción total', resultados['produccion_total'])

	st.subheader('Resultados')
	st.dataframe(resultados['tabla'], width='stretch')

	st.subheader('Interpretación Inteligente')
	st.info(analisis)


if modulo == 'Optimización de bodegas':
	st.header('Optimización de Bodegas')

	if st.button('Resolver modelo', key='bodegas_btn'):
		ejecutar_modelo('bodegas', resolver_modelo_bodegas, 'bodegas')

	if 'bodegas' in st.session_state.resultados:
		mostrar_resultados('bodegas')


elif modulo == 'Selección de proyectos':
	st.header('Selección de Proyectos')

	if st.button('Resolver modelo', key='proyectos_btn'):
		ejecutar_modelo('proyectos', resolver_modelo_proyectos, 'proyectos')

	if 'proyectos' in st.session_state.resultados:
		mostrar_resultados('proyectos')


elif modulo == 'Manufactura':
	st.header('Producción Manufacturera')

	if st.button('Resolver modelo', key='manufactura_btn'):
		ejecutar_modelo('manufactura', resolver_modelo_manufactura, 'manufactura')

	if 'manufactura' in st.session_state.resultados:
		mostrar_resultados('manufactura')
