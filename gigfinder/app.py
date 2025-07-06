import streamlit as st
import requests

# Load Hugging Face token securely from Streamlit Secrets
hf_token = st.secrets["huggingface"]["api_token"]

# Hugging Face inference endpoint
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {hf_token}"
}

# Function to generate job results
def generate_jobs(skill):
    prompt = f"""
You are a freelance project assistant. Based on the skill '{skill}', list 3 relevant freelance projects.
Each project should include:
- Platform (like Upwork, Fiverr, Freelancer, Glassdoor)
- Project Title
- Budget or Payment
- A 1-line description
Format output clearly with bullet points.
"""

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except:
            return "⚠️ Model responded, but output format was unexpected."
    elif response.status_code == 401:
        return "❌ Unauthorized: Your Hugging Face token may be invalid or expired."
    else:
        return f"❌ API Error {response.status_code}: {response.text}"

# -------- Streamlit App UI --------
st.set_page_config(page_title="GigFinder AI", page_icon="💼")
st.title("🤖 GigFinder - Freelance Project Assistant")

skill = st.text_input("Enter your skill or category (e.g., Python, UI/UX, WordPress)")

if st.button("Find Freelance Projects"):
    if not skill.strip():
        st.warning("⚠️ Please enter a skill.")
    else:
        with st.spinner("🔍 Finding projects..."):
            result = generate_jobs(skill)
            st.text_area("📋 Project Listings", result, height=300)
