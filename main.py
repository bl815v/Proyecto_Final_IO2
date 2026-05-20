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
st.subheader('Programación Entera Mixta e Inteligencia Artificial')


st.sidebar.title('Módulos')

modulo = st.sidebar.radio(
	'Seleccionar problema', ['Optimización de bodegas', 'Selección de proyectos', 'Manufactura']
)


if modulo == 'Optimización de bodegas':
	st.header('Optimización de Bodegas')

	if st.button('Resolver modelo'):
		resultados = resolver_modelo_bodegas()

		col1, col2 = st.columns(2)

		with col1:
			st.metric('Ganancia máxima', f'${resultados["ganancia"]:,}')

		with col2:
			st.metric('Bodegas abiertas', resultados['bodegas_abiertas'])

		st.subheader('Resultados')
		st.dataframe(resultados['tabla'])

		st.subheader('Interpretación IA')
		analisis = generar_analisis_ia('bodegas', resultados)

		st.success(analisis)


elif modulo == 'Selección de proyectos':
	st.header('Selección de Proyectos')

	if st.button('Resolver modelo'):
		resultados = resolver_modelo_proyectos()

		col1, col2 = st.columns(2)

		with col1:
			st.metric('Beneficio total', f'${resultados["beneficio"]:,}')

		with col2:
			st.metric('Proyectos seleccionados', resultados['cantidad'])
		st.success(analisis)
