import streamlit as st
from langchain.chat_models import ChatOpenAI

api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(
    page_title="AI 기반 고객 응대 서비스",
    page_icon="🌐",
    layout="wide"
)

st.markdown("""
    <div style="background-color:#4A90E2;padding:10px;border-radius:10px;">
        <h1 style="color:white;text-align:center;"> 🤖 AI 고객 응대 서비스</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="padding: 10px;">
        <h3 style="color:#333; text-align:center;">AI와의 대화를 통해 고객님의 궁금증을 신속하게 해결해드리겠습니다.</h3>
        <p style="text-align:center;">문의사항을 아래에 입력하시고 <strong>보내기</strong> 버튼을 눌러주세요!</p>
    </div>
""", unsafe_allow_html=True)

def generate_response(input_text): 
    llm = ChatOpenAI(
        openai_api_key=api_key,
        temperature=1.0,
        model_name='gpt-3.5-turbo'  # OpenAI에서 지원하는 실제 모델명
    )
    response = llm.predict(input_text)
    st.markdown(f"""
        <div style="background-color:#F0F0F0;padding:15px;border-radius:10px;margin-top:15px;">
            <h4>💡 고객님께 드리는 답변:</h4>
            <p>{response}</p>
        </div>
    """, unsafe_allow_html=True)

with st.form("question_form"):
    text = st.text_area(
        "궁금한 점을 입력하세요:", 
        placeholder="예: 반품 정책은 어떻게 되나요?",
        height=150
    )
    submitted = st.form_submit_button("보내기", use_container_width=True)

    if submitted:
        if text.strip():
            generate_response(text)
        else:
            st.warning("질문을 입력해주세요.")

st.markdown("""
    <div style="margin-top: 50px; padding: 15px; background-color: #333; color: white; text-align: center; border-radius: 10px;">
        <p>Powered by LangChain & OpenAI API | 🏦 고객의 만족을 위해 언제나 최선을 다합니다.</p>
    </div>
""", unsafe_allow_html=True)
