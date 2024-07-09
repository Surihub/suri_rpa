import streamlit as st
import numpy as np
import plotly.express as px
import seaborn as sns

# 페이지 제목 설정
st.title("Penguins 데이터 분석")

# 데이터 불러오기 및 표시
df = sns.load_dataset("penguins")
st.write(df.head())

# 첫 번째 그래프: 섬별 펭귄 몸무게 평균
df_plotly = df.pivot_table(index='island', values=['body_mass_g'], aggfunc='mean').reset_index()
fig1 = px.bar(df_plotly, x='island', y=['body_mass_g'], barmode='group', title='1. Average Body Mass by Island')
st.plotly_chart(fig1, use_container_width=True)

# 두 번째 그래프: 성별에 따른 펭귄의 Flipper 길이 분포
fig2 = px.box(df, x='sex', y='flipper_length_mm', title='2. Flipper Length Distribution by Sex')
st.plotly_chart(fig2, use_container_width=True)

# 세 번째 그래프: 서식지에 따른 부리 길이와 깊이의 산점도
fig3 = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='island', 
                  title='3. Bill Length vs. Bill Depth by Island')
st.plotly_chart(fig3, use_container_width=True)

# 네 번째 그래프: 종별 펭귄 몸무게 분포
fig4 = px.violin(df, x='species', y='body_mass_g', color='species', 
                 title='4. Body Mass Distribution by Species')
st.plotly_chart(fig4, use_container_width=True)

# 다섯 번째 그래프: 서식지별 성비 분포
fig5 = px.histogram(df, x='island', color='sex', barmode='group', 
                    title='5. Sex Distribution by Island')
st.plotly_chart(fig5, use_container_width=True)