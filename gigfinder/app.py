import streamlit as st
import requests

st.set_page_config(page_title="GigFinder", page_icon="💼")
st.title("🤖 GigFinder - AI Freelance Project Assistant")

skill = st.text_input("Enter your skill or category")
hf_token = st.text_input("Paste your Hugging Face token", type="password")

def generate_jobs(skill, hf_token):
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"  # LIGHTWEIGHT model
    headers = {"Authorization": f"Bearer {hf_token}"}
    prompt = f"List 3 freelance jobs for skill '{skill}' with platform, title, pay, and summary."
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    st.write("⚙️ Raw response:", response.json())  # Debug line

    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except:
            return "⚠️ Couldn't parse output from model."
    else:
        return f"❌ API Error {response.status_code}: {response.text}"

if st.button("Find Projects"):
    if not skill or not hf_token:
        st.warning("Enter both fields.")
    else:
        with st.spinner("Contacting AI..."):
            output = generate_jobs(skill, hf_token)
            st.text_area("Generated Jobs", output, height=300)
