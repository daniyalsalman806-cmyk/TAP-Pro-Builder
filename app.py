import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

st.set_page_config(page_title="TAP Pro Builder", layout="wide")
st.title("🛠️ TAP Pro: AI Website Architect")

# Safe API Configuration
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Yahan 'models/' lagana zaroori hai
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error("Secrets mein API Key missing hai ya galat hai!")

col1, col2 = st.columns(2)

if "code_output" not in st.session_state:
    st.session_state.code_output = "<!-- Website yahan render hogi -->"

with col1:
    st.subheader("⌨️ Design & Code")
    user_prompt = st.chat_input("Prompt likhein...")
    
    if user_prompt:
        with st.spinner("AI Engine kaam kar raha hai..."):
            system_instruction = "You are a pro web developer. Output ONLY clean HTML/CSS code. No talk, just code."
            # Error fix: check if model exists
            response = model.generate_content(f"{system_instruction}\n\nTask: {user_prompt}")
            st.session_state.code_output = response.text
            st.code(st.session_state.code_output, language='html')

with col2:
    st.subheader("🌐 Live Preview")
    components.html(st.session_state.code_output, height=600, scrolling=True)
