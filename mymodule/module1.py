import streamlit as st
import json
import requests
@st.cache_data
def greeting(name):
    st.write(f"안녕하세요, {name}")

def chat(name):
    st.write(f"{name}님, 오늘 기분이 어떠세요?")
    response = st.text_input("기분:")
    if response !="":
        st.write(f"저도 {response}!")
        
import math

def grid(v1, v2) :
 
    RE = 6371.00877 # 지구 반경(km)
    GRID = 5.0      # 격자 간격(km)
    SLAT1 = 30.0    # 투영 위도1(degree)
    SLAT2 = 60.0    # 투영 위도2(degree)
    OLON = 126.0    # 기준점 경도(degree)
    OLAT = 38.0     # 기준점 위도(degree)
    XO = 43         # 기준점 X좌표(GRID)
    YO = 136        # 기1준점 Y좌표(GRID)

    DEGRAD = math.pi / 180.0
    RADDEG = 180.0 / math.pi

    re = RE / GRID;
    slat1 = SLAT1 * DEGRAD
    slat2 = SLAT2 * DEGRAD
    olon = OLON * DEGRAD
    olat = OLAT * DEGRAD
 
    sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(math.pi * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn);
    rs = {};

    ra = math.tan(math.pi * 0.25 + (v1) * DEGRAD * 0.5)
    ra = re * sf / math.pow(ra, sn)

    theta = v2 * DEGRAD - olon
    if theta > math.pi :
        theta -= 2.0 * math.pi
    if theta < -math.pi :
        theta += 2.0 * math.pi
    theta *= sn
    rs['x'] = math.floor(ra * math.sin(theta) + XO + 0.5)
    rs['y'] = math.floor(ro - ra * math.cos(theta) + YO + 0.5)

    nx = str(rs["x"]).split('.')[0]
    ny = str(rs["y"]).split('.')[0]
    # string = "http://www.kma.go.kr/wid/queryDFS.jsp?gridx={0}&gridy={1}".format(
    # str(rs["x"]).split('.')[0], str(rs["y"]).split('.')[0])
    return nx, ny

# 출처: https://doriri.tistory.com/18 [My Programming:티스토리]


# 학교 조회하는 함수/ 합수 입력 > 라디오버튼 선택하게
@st.cache_data
def find_my_school(school_name, url):
    params={
        'KEY':st.secrets['neis']['key'],
        'Type':'json',
        'pIndex' :1,
        'pSize' : 100,
        'SCHUL_NM' : school_name
        }

    response = requests.get(url, params=params)
    contents = response.text
    # JSON 문자열을 Python 딕셔너리로 파싱
    data = json.loads(contents)
    # st.write(data)

    schools_by_district = {}
    for item in data["schoolInfo"][1]["row"]:
        district = item["ATPT_OFCDC_SC_NM"]
        district_code = item['ATPT_OFCDC_SC_CODE']
        school_name = item["SCHUL_NM"]
        school_code = item['SD_SCHUL_CODE']
        schools_by_district.setdefault(district, []).append(school_name)
        schools_by_district.setdefault(district, []).append(school_code)
        schools_by_district.setdefault(district, []).append(district_code)
    return schools_by_district

@st.cache_data
def give_me_meal(district_code, school_code, date):
    mealurl = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    params={
        'KEY':st.secrets['neis']['key'],
        'Type':'json',
        'pIndex' :1,
        'pSize' : 100,
        'ATPT_OFCDC_SC_CODE' : district_code,
        'SD_SCHUL_CODE' : school_code,
        'MLSV_YMD' : date
        }

    response = requests.get(mealurl, params=params)
    contents = response.text
    # JSON 문자열을 Python 딕셔너리로 파싱
    data = json.loads(contents)
    # st.write(data)
    try:
        menu = data["mealServiceDietInfo"][1]['row'][0]['DDISH_NM'].split('<br/>')
    except:
        st.error("정보를 불러올 수 없습니다. 날짜를 다시 확인해주세요! 급식이 없던 날 같아요. ")
        menu = []
    # st.write(data)
    return menu