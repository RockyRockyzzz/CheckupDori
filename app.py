import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

st.set_page_config(page_title="CheckupDori", layout="wide")

# 세션 초기화
if "page" not in st.session_state:
    st.session_state["page"] = "start"

# 페이지 네비게이션
if st.session_state["page"] == "start":
    st.image("assets/dori.png", width=200)  # 도리 이미지 출력
    st.title("🦉 Welcome to CheckupDori!")
    st.subheader("Your friendly health checkup guide in Korea 🇰🇷")
    st.write(
        """
        CheckupDori helps foreigners visiting or living in Korea easily navigate health checkups, 
        find hospitals, and prepare for their exams through an AI chatbot.
        """
    )
    if st.button("🚀 Get Started"):
        st.session_state["page"] = "profile"

elif st.session_state["page"] == "profile":
    from profile_1 import user_profile_page
    user_profile_page()

elif st.session_state["page"] == "chat":
    from chat import dori_chat_page
    dori_chat_page()

elif st.session_state["page"] == "hospital":
    st.header("🗂️ Hospital Finder")
    from hospital import run_hospital_finder

    run_hospital_finder()