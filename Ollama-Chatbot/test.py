import streamlit as st
from openai import OpenAI

# Streamlit UI 타이틀
st.title("Chatbot with OpenRouter API")

# OpenRouter API 클라이언트 설정
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# 세션 상태에 메시지 히스토리가 없으면 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "사용자와 한국어로 대화하세요. 대화는 자연스럽고 친근하게 진행하세요."}
    ]

# 과거 메시지 렌더링
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# 사용자 입력
prompt = st.chat_input("여기에 메시지 입력...")

if prompt:
    # 유저 메시지 화면에 출력 및 히스토리에 저장
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # DeepSeek 모델로 응답 생성
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct:free",
            messages=st.session_state.messages
        )
        response = completion.choices[0].message.content
    except Exception as e:
        response = f"❌ 오류 발생: {e}"

    # 모델 응답 출력 및 히스토리에 저장
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})