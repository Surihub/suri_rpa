import streamlit as st
from openai import OpenAI

# 페이지 제목 설정
st.title("📚 교사 업무 자동화 챗봇")
customize_temp = st.number_input("챗봇의 말투를 설정해주세요. 0에 가까울수록 짧고 단답으로, 1에 가까울수록 말이 화려하고 길어집니다.", min_value = 0, max_value=1)
character = "Propose innovative and practical AI-powered solutions to automate specific teaching tasks, such as grading, attendance tracking, lesson preparation, or student performance monitoring, specialized and professional in ROBOTIC PROCESS AUTOMATION IN SCHOOL AS A TEACHER"
# 세션 상태가 초기화되지 않았다면 초기화하기
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant",
                                     "system":character, 
                                     "content": "안녕하세요, 선생님! 어떤 업무를 도와드릴까요? 예를 들어, 시험 채점, 출석 확인, 교육 자료 추천 등의 도움을 드릴 수 있어요."}]

if "token_usage_count" not in st.session_state:
    st.session_state["token_usage_count"] = 0

# 이전 대화 내용을 화면에 표시
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 사용자 입력 받기
if prompt := st.chat_input():
    openai_api_key = st.secrets['openai']['key']
    # API 키 확인
    if not openai_api_key:
        st.info("계속하려면 OpenAI API 키를 입력해주세요.")
        st.stop()

    # 토큰 사용 횟수 체크
    if st.session_state["token_usage_count"] >= 20:
        st.warning("토큰 사용 횟수를 초과했습니다. 더 이상 메시지를 보낼 수 없습니다.")
    else:
        # OpenAI 클라이언트 설정
        client = OpenAI(api_key=openai_api_key)
        
        # 입력된 메시지를 세션 상태에 추가
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # 입력된 메시지를 화면에 표시
        st.chat_message("user").write(prompt)
        
        # 챗봇의 응답 생성을 위한 설정: 교육 관련 작업에 적합한 응답을 생성하도록 모델 지정
        response = client.chat.completions.create(model="gpt-3.5-turbo", 
                                                  messages=st.session_state.messages, 
                                                  temperature=customize_temp, 
                                                  max_tokens=300, 
                                                  stop=["\n"])
        
        # 응답 메시지 추출 및 세션 상태에 추가
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        
        # 응답 메시지를 화면에 표시
        st.chat_message("assistant").write(msg)
        
        # 토큰 사용 횟수 증가
        st.session_state["token_usage_count"] += 1

        # st.write(st.session_state.messages)