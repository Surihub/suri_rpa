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
    st.warning('###### 어떻게 해결하나요?\n계수가 다른 이차방정식 문제 무한 생성')

st.write('아래의 이차방정식의 해를 구하세요.')
st.write('예를 들어, 이차방정식 $$x^2=1$$의 경우 답안에는 $$1, -1$$과 같이 컴마로 구분하여 입력하면 됩니다. ')


# 1. 임의의 일차방정식 생성 함수
def generate_equation():
    while True:
        a = random.choice([-1, 1, 2, 3, 4])  # a는 -1, 1, 2, 3, 4 중 선택
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)
        d = b**2 - 4*a*c  # 판별식

        # 판별식이 0보다 크거나 같을 때까지 반복
        if d >= 0:
            # a의 처리
            a_term = "" if abs(a) == 1 else str(a)
            if a == -1:
                a_term = "-"
            
            # b의 처리
            if b == 0:
                b_term = ""
            else:
                b_coeff = "" if abs(b) == 1 else abs(b)
                b_sign = "-" if b < 0 else " + "
                b_term = f"{b_sign}{b_coeff}x" if b != 1 else " + x"
                b_term = b_term if b != -1 else " - x"
            
            # c의 처리
            if c == 0:
                c_term = ""
            else:
                c_sign = " + " if c > 0 else " - "
                c_term = f"{c_sign}{abs(c)}"
            
            equation = f"{a_term}x^2{b_term}{c_term} = 0"
            
            # 해 구하기
            sol1 = (-b - np.sqrt(d)) / (2*a)
            sol2 = (-b + np.sqrt(d)) / (2*a)
            solution = [sol1, sol2]
            return equation, solution

# 문제 생성 버튼
if st.button("문제 생성"):
    equation, solution = generate_equation()
    st.session_state.equation = equation
    solution = np.round(solution, 2)
    st.session_state.solution = solution
    st.write(solution)

# 문제 제시
if 'equation' in st.session_state:
    st.write(f"## 😀 $${st.session_state.equation}$$")
    # 답안 입력 및 제출
    answer_input = st.text_input("방정식에 대한 답을 콤마와 함께 입력해주세요!\n(소수 둘째자리까지 반올림해주세요. 예를 들어 답이 0.16666, -0.16666이라면, 0.17,-0.17로 입력해주세요!)")
    answer_input = answer_input.replace(" ", "").split(',')
    
    try:
        answer = [float(num) for num in answer_input]
        answer = np.round(answer, 2)  # 입력받은 답안을 소수 둘째 자리까지 반올림

        if st.button("제출"):
            if np.allclose(np.sort(answer), np.sort(st.session_state.solution), atol=0.01):
                st.success("🎉정답입니다! 💯 참 잘했어요. **문제 생성** 버튼을 눌러 다음 문제를 해결해보세요.")
            else:
                st.error("😓오답입니다! 다시 한 번 시도해보세요!💪")
                st.write(f"힌트: 근의 공식을 생각해보세요! ")
    except ValueError:
        if st.button("제출"):
            st.error("입력 형식이 올바르지 않습니다. 숫자만 입력해주세요.")


