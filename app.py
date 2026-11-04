import streamlit as st
import pandas as pd
import plotly_express as px

df_vehicles = pd.read_csv('vehicles.csv', sep=',')
