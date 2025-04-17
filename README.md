📄 CheckupDori - Help for Health Checkups in Korea
CheckupDori is a Streamlit-based chatbot service designed to assist foreigners living in or visiting Korea to easily find hospitals, understand health checkups, and get medical support in English and other languages.

🌟 Features
🦉 Chat with Dori
Personalized AI medical assistant chatbot based on user profile (age, gender, etc.)

🏥 Hospital Finder
Location-based hospital search with department filtering (Internal Medicine, Orthopedics, etc.)

💊 Medication Image OCR
Upload medication label images to interpret and explain drug usage and storage instructions.

📷 Smart OCR Guidance
In-app camera guide to improve OCR recognition quality.

📍 Kakao Map Integration
Automatic generation of nearby hospital search links.

🛠️ Tech Stack
Frontend: Streamlit

AI: OpenAI GPT (via API)

OCR: EasyOCR + Torch

Map Integration: Folium + Streamlit-Folium

Data Handling: Pandas, Numpy

Deployment Ready: Streamlit Cloud / Docker-compatible

🚀 How to Run Locally
Clone the repository:

bash
복사
편집
git clone https://github.com/your_username/checkupdori.git
cd checkupdori
Install dependencies:

bash
복사
편집
pip install -r requirements.txt
Set up .env file:

ini
복사
편집
OPENAI_API_KEY=your-openai-api-key
KAKAO_API_KEY=your-kakao-api-key
Run the app:

bash
복사
편집
streamlit run app.py
🔒 Important
Never upload your .env file to GitHub.

.env is already included in .gitignore.

✨ Future Plans
Multilingual Support (Korean, English, Vietnamese, Chinese)

Hospital Review and Rating System

More advanced symptom triage & emergency guidance

Continuous health management assistant

📬 Contact
If you'd like to collaborate or have any inquiries, feel free to reach out!
koreanrocky819@gmail.com

🦉 CheckupDori: Your friendly guide for health checkups in Korea!
