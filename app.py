import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

st.set_page_config(page_title="CheckupDori", layout="wide")

# 세션 초기화
if "page" not in st.session_state:
    st.session_state["page"] = "profile"

tabs = {
    "profile": "👤 Profile",
    "chat": "🏥 Chatbot",
    "hospital": "🗂️ Hospital Finder"
}

# 탭 네비게이션
tab_selection = st.selectbox("Navigation", list(tabs.values()), index=list(tabs.keys()).index(st.session_state["page"]))
reverse_tabs = {v: k for k, v in tabs.items()}
st.session_state["page"] = reverse_tabs[tab_selection]

# Profile 입력 화면
if st.session_state["page"] == "profile":
    st.header("👤 User Information for Health Checkup Recommendation")

    with st.form(key="user_info_form"):
        age = st.number_input("Age", min_value=0, max_value=120)
        gender = st.radio("Gender", ["Male", "Female"])
        pregnancy_status = None
        if gender == "Female":
            pregnancy_status = st.radio("Are you pregnant?", ["Yes", "No", "Prefer not to say"])

        stay_type = st.radio("Type of stay in Korea", ["Short-term", "Long-term"])
        insurance = st.radio("Do you have Korean national health insurance?", ["Yes", "No"])
        purpose = st.selectbox("Purpose of checkup", ["General checkup", "Visa checkup", "Cancer screening"])
        premium_interest = st.radio("Are you interested in premium (full-body) checkups?", ["Yes", "No"])

        submit_button = st.form_submit_button(label="Save Information")

    if submit_button:
        st.session_state["user_profile"] = {
            "age": age,
            "gender": gender,
            "pregnancy_status": pregnancy_status,
            "stay_type": stay_type,
            "has_insurance": True if insurance == "Yes" else False,
            "purpose": purpose,
            "premium_interest": True if premium_interest == "Yes" else False
        }
        st.success("✅ Your information has been saved!")
        st.session_state["page"] = "chat"

# Chatbot 화면
elif st.session_state["page"] == "chat":
    from chat import dori_chat_page

    st.header("🏥 Chatbot for Health Checkup Guidance")
    if "user_profile" not in st.session_state or st.session_state["user_profile"] is None:
        st.error("❗ Please fill out your profile first.")
        st.stop()
    else:
        dori_chat_page()

# Hospital Finder 화면
elif st.session_state["page"] == "hospital":
    st.header("🗂️ Hospital Finder")
    st.info("🏥 (병원 검색 기능 연결 예정)")