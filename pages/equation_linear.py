import streamlit as st
import random
import numpy as np
import time
# 페이지 설명 부분

st.title("수학 문제 무한 생성기!🖍")


col1, col2 = st.columns(2)
with col1:
    st.info('###### 언제 사용하나요?\n연습이 필요한 계산 문제가 항상 부족하다구요? 문제 찾기 귀찮다구요? 숫자만 바꿔도 되는 문제라면, 문제를 자동으로 만들고 채점도 자동으로 해보세요! ')
with col2:
    st.warning('###### 어떻게 해결하나요?\n계수가 다른 일차방정식 문제 무한 생성')

st.write('아래의 일차방정식의 해를 구하세요.')
st.write('예를 들어, 2x-1=3인 경우 답안에는 2만 입력하면 됩니다. ')


# 1. 임의의 일차방정식 생성 함수
def generate_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    equation = f"{a}x + {b} = {c}"
    return equation, np.round((c-b)/a,2)


# 문제 생성 버튼
if st.button("문제 생성"):
    equation, solution = generate_equation()
    st.session_state.equation = equation
    st.session_state.solution = solution

# 문제 제시
if 'equation' in st.session_state:
    st.write(f"## 😀 $${st.session_state.equation}$$")
    # 답안 입력 및 제출
    answer = st.number_input("방정식에 대한 답을 입력하세요(소수 둘째자리까지 반올림! 예를 들어 답이 0.16666이라면, 0.17로 입력해주세요!)")
    if st.button("제출"):
        if answer == st.session_state.solution:
            st.success("🎉정답입니다! 💯 참 잘했어요. **문제 생성** 버튼을 눌러 다음 문제를 해결해보세요.")
        else:
            st.error("😓오답입니다! 다시 한 번 시도해보세요!💪")
            st.write(f"힌트: 이항을 먼저 하고, $$x$$의 계수로 나눠주세요. ")
