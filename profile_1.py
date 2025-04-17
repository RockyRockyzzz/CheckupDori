import streamlit as st

def user_profile_page():
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
