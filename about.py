import streamlit as st


def run():
    st.set_page_config(
        page_title="Welcome to 숩 RPA",
        page_icon="👋",
        layout="wide"
    )

    st.markdown("""
    <style>
    .main {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h1 {
        color: black;
    }
    .stMarkdown {
        color: #4f4f4f;
    }
    .stButton>button {
        color: white;
        background-color: #ff6347;
        border-radius: 5px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("💻 일상에서 업무자동화")

    st.markdown("""
        ### 업무 & 공부를 좀 쉽게 할 수는 없을까요?
        업무자동화 페이지에 오신 것을 환영합니다! 일상에서 반복해야 하는 단순 작업을 자동화하기 위한 웹앱입니다. 
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 8px; background-color: #f7f7f7; margin-bottom: 10px;">
            <p style="margin-bottom: 5px; color: #555;">
                숩숩 ✉ <a href="mailto:sbhath17@gmail.com">sbhath17@gmail.com</a> | 
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" height="20" style="vertical-align: middle;">
                <a href="https://github.com/Surihub/suri-rpa" target="_blank">GitHub</a>  | 
                <a href="https://forms.gle/nytXFQiRriwRgkKy7" target="_blank">피드백 하러 가기</a>
            </p>
            <p style="margin-bottom: 5px; color: #555;">
                업무자동화 페이지 1 구경하기 > <a href="https://surihub-rpa-app-ieocnc.streamlit.app/" target="_blank">RPAinSchool</a>
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button('Click me'):
        st.snow()

if __name__ == "__main__":
    run()
