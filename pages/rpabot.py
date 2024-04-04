import streamlit as st
from openai import OpenAI

# 페이지 제목 설정
st.title("📚 교사 업무 자동화 챗봇")

# 세션 상태가 초기화되지 않았다면 초기화하기
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요, 선생님! 어떤 업무를 도와드릴까요? 예를 들어, 시험 채점, 출석 확인, 교육 자료 추천 등의 도움을 드릴 수 있어요."}]

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

    # OpenAI 클라이언트 설정
    client = OpenAI(api_key=openai_api_key)
    
    # 입력된 메시지를 세션 상태에 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 입력된 메시지를 화면에 표시
    st.chat_message("user").write(prompt)
    
    # 챗봇의 응답 생성을 위한 설정: 교육 관련 작업에 적합한 응답을 생성하도록 모델 지정
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages, 
                                              temperature=0.5, 
                                              max_tokens=300, 
                                              stop=["\n"])
    
    # 응답 메시지 추출 및 세션 상태에 추가
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    
    # 응답 메시지를 화면에 표시
    st.chat_message("assistant").write(msg)
