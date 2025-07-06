import streamlit as st
import requests

# Load Hugging Face API token from secrets.toml
hf_token = st.secrets["huggingface"]["api_token"]

def generate_jobs(skill):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {
        "Authorization": f"Bearer {hf_token}"
    }

    # Prompt for the AI
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
        except Exception:
            return "⚠️ Model responded but output format was unexpected."
    else:
        return f"❌ API Error {response.status_code}: {response.text}"

# ---------- Streamlit UI ----------
st.set_page_config(page_title="GigFinder AI", page_icon="💼")
st.title("🤖 GigFinder - AI Freelance Project Assistant")

# User input
skill = st.text_input("Enter your skill or category (e.g., Python, UI/UX, WordPress)")

# Trigger AI generation
if st.button("Find Projects"):
    if not skill:
        st.warning("Please enter a skill.")
    else:
        with st.spinner("⏳ Fetching AI-generated freelance gigs..."):
            output = generate_jobs(skill)
            st.text_area("📋 Project Listings", output, height=300)
