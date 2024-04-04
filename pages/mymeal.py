import streamlit as st
import requests
import json
import datetime
import pandas as pd
from mymodule.module1 import find_my_school, give_me_meal


st.title("😍급식타임")

neiskey = st.secrets['neis']['key']
url = "https://open.neis.go.kr/hub/schoolInfo"
# st.write(neiskey)



st.subheader("학교 조회")
school_input = st.text_input("학교이름을 입력해주세요.")

schools_by_district = find_my_school(school_input, url)
district = st.radio("학교가 소속된 교육청을 선택해주세요",options=schools_by_district)
school_name = schools_by_district[district][0]
school_code = schools_by_district[district][1]
district_code = schools_by_district[district][2]


st.subheader(school_name+"의 급식을 찾아볼게요!")
date = st.date_input("조회할 날짜를 입력해주세요:", datetime.date(2024, 4, 2)).strftime("%Y%m%d")


menu = give_me_meal(district_code, school_code, date)
st.table(menu)