import streamlit as st
import numpy as np
import plotly.express as px
import seaborn as sns


df = sns.load_dataset("titanic")
st.write(df.head())
df_plotly = df.pivot_table(index='pclass', values=['fare'], aggfunc='mean').reset_index()
fig = px.bar(df_plotly, x = 'pclass', y = ['fare'],  barmode = 'group')

st.plotly_chart(fig, use_container_width=True)
fig = px.box(df, x='survived', y='age')
st.plotly_chart(fig, use_container_width=True)
