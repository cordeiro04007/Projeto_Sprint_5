import streamlit as st
import pandas as pd
import plotly_express as px

df_vehicles = pd.read_csv('vehicles.csv', sep=',')

st.header('Analisando dados de Veículos')

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig_hist = px.histogram(df_vehicles , x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button('Criar Gráfico de Dispersão') # criar um botão
        
if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um Gráfico de Dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um Scatter
    fig_scatter = px.scatter(df_vehicles, x="odometer", y="price") # criar um gráfico de dispersão

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
        
