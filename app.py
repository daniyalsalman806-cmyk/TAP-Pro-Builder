import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

st.set_page_config(page_title="TAP Pro Builder", layout="wide")
st.title("🛠️ TAP Pro: AI Website Architect")

# API Configuration
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets mein API Key missing hai!")
else:
    # Yahan se try block shuru hota hai
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    # Ye except block hona zaroori hai syntax theek karne ke liye
    except Exception as e:
        st.error(f"Config Error: {e}")

col1, col2 = st.columns(2)

if "code_output" not in st.session_state:
    st.session_state.code_output = "<h1>Welcome to TAP Pro</h1><p>Prompt likhein...</p>"

with col1:
    st.subheader("⌨️ Design & Code")
    user_prompt = st.chat_input("Prompt likhein...")
    
    if user_prompt:
        try:
            with st.spinner("AI Engine kaam kar raha hai..."):
                response = model.generate_content(f"Output ONLY clean HTML/CSS code for: {user_prompt}")
                st.session_state.code_output = response.text
                st.code(st.session_state.code_output, language='html')
        except Exception as e:
            st.error(f"Generation Error: {e}")

with col2:
    st.subheader("🌐 Live Preview")
    components.html(st.session_state.code_output, height=600, scrolling=True)
