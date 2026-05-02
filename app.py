import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

st.set_page_config(page_title="TAP Pro Builder", layout="wide")

st.title("🛠️ TAP Pro: AI Website Architect")

# Safe API Configuration (Secrets se uthayega)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Secrets mein API Key missing hai!")

# Layout: 50/50 Split (Ek taraf chat, ek taraf website)
col1, col2 = st.columns(2)

if "code_output" not in st.session_state:
    st.session_state.code_output = "<!-- Website yahan render hogi -->"

with col1:
    st.subheader("⌨️ Design & Code")
    user_prompt = st.chat_input("Prompt likhein (e.g. 'Build a professional cricket portfolio page')")
    
    if user_prompt:
        with st.spinner("AI Engine website bana raha hai..."):
            system_instruction = "You are a pro web developer. Output ONLY clean HTML/CSS code inside <html> tags. No prose, no talk, just code."
            response = model.generate_content(f"{system_instruction}\n\nTask: {user_prompt}")
            st.session_state.code_output = response.text
            st.code(st.session_state.code_output, language='html')

with col2:
    st.subheader("🌐 Live Preview")
    components.html(st.session_state.code_output, height=600, scrolling=True)
