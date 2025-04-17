import streamlit as st
import pandas as pd

# 병원 데이터 로딩 함수 (캐시 사용)
@st.cache_data
def load_hospital_data():
    try:
        df = pd.read_csv("assets/checkupdori_hospital_with_tags.csv")
        return df
    except FileNotFoundError:
        st.error("병원 데이터 파일을 찾을 수 없습니다.")
        return pd.DataFrame()

# 병원 탐색 인터페이스
def run_hospital_finder():
    st.title("🏥 Hospital Finder")
    df = load_hospital_data()

    if df.empty:
        st.warning("등록된 병원 데이터가 없습니다.")
        return

    # 사용자 관심분야 가져오기
    user_interests = st.session_state.get("user_profile", {}).get("interests", [])

    # 관심분야 필터링
    if user_interests:
        st.markdown("### 🔍 Recommended Hospitals Based on Your Interests")
        filtered_df = df[df["관심분야"].apply(lambda tags: any(interest in tags for interest in user_interests))]
    else:
        st.markdown("### 🔍 All Available Hospitals")
        filtered_df = df
    search_query = st.text_input("🔎 Search Hospital Name, Address or Specialty", "")
    if search_query:
    
     filtered_df = filtered_df[
        filtered_df.apply(
            lambda row: search_query.lower() in row['병원이름'].lower()
            or search_query.lower() in row['주소'].lower()
            or search_query.lower() in row['관심분야'].lower(),
            axis=1
        )
    ]
    # 병원 리스트 출력
    st.markdown("---")
    for _, row in filtered_df.iterrows():
        st.markdown(f"""**🏥 {row['병원이름']}**  
📍 {row['주소']} ({row['지역']})  
📞 {row['전화번호']}  
🔗 [Visit Website]({row['웹사이트']})  
**Specialties:** {row['관심분야']}  
---""")

if __name__ == "__main__":
    run_hospital_finder()