import streamlit as st
from openai import OpenAI
import os

def dori_chat_page():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    ASSISTANT_ID = "asst_Iq1O3XWH1h2RG0O3IW1QXwK5"

    st.header("🏥 Chatbot for Health Checkup Guidance")

    if "user_profile" not in st.session_state or st.session_state["user_profile"] is None:
        st.error("❗ Please fill out your profile first.")
        st.stop()

    # Thread 초기화
    if "thread_id" not in st.session_state:
        thread = client.beta.threads.create()
        st.session_state["thread_id"] = thread.id

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # 사용자 프로필 메시지 초기 삽입
    def format_user_profile(profile):
        return (
            f"The user profile is as follows:\n"
            f"- Age: {profile['age']}\n"
            f"- Gender: {profile['gender']}\n"
            f"- Pregnancy status: {profile.get('pregnancy_status', 'N/A')}\n"
            f"- Stay type: {profile['stay_type']}\n"
            f"- Health insurance: {'Yes' if profile['has_insurance'] else 'No'}\n"
            f"- Purpose of checkup: {profile['purpose']}\n"
            f"- Interested in premium checkup: {'Yes' if profile['premium_interest'] else 'No'}\n"
        )

    if "profile_sent" not in st.session_state:
        profile_message = format_user_profile(st.session_state["user_profile"])
        client.beta.threads.messages.create(
            thread_id=st.session_state["thread_id"],
            role="user",
            content=f"This is my profile information:\n{profile_message}\nPlease recommend suitable health checkup types for me."
        )
        st.session_state["profile_sent"] = True

    # 기존 대화 표시
    for msg in st.session_state["chat_history"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 사용자 입력 받기
    if prompt := st.chat_input("What would you like to ask Dori?"):
        with st.chat_message("user"):
            st.markdown(prompt)

        client.beta.threads.messages.create(
            thread_id=st.session_state["thread_id"],
            role="user",
            content=prompt
        )

        with st.spinner("Dori is thinking..."):
            run = client.beta.threads.runs.create(
                thread_id=st.session_state["thread_id"],
                assistant_id=ASSISTANT_ID
            )

            while True:
                run_status = client.beta.threads.runs.retrieve(
                    thread_id=st.session_state["thread_id"],
                    run_id=run.id
                )
                if run_status.status == "completed":
                    break

            messages = client.beta.threads.messages.list(
                thread_id=st.session_state["thread_id"]
            )
            latest_message = messages.data[0]
            assistant_reply = latest_message.content[0].text.value

        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

        # 대화 기록 저장
        st.session_state["chat_history"].append({"role": "user", "content": prompt})
        st.session_state["chat_history"].append({"role": "assistant", "content": assistant_reply})