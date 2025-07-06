import streamlit as st
import requests

# Function to generate project listings using Hugging Face model
def generate_jobs(skill, hf_token):
   API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers = {
        "Authorization": f"Bearer {hf_token}"
    }

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
            return "Model responded, but format was unexpected. Try a different model or prompt."
    else:
        return f"❌ API Error {response.status_code}: {response.text}"

# Streamlit App UI
st.set_page_config(page_title="GigFinder AI", page_icon="💼")
st.title("🤖 GigFinder - AI Freelance Project Assistant")

skill = st.text_input("Enter your skill or category (e.g., Python, UI/UX, WordPress)")
hf_token = st.text_input("Paste your Hugging Face token (keep it safe!)", type="password")

if st.button("Find Projects"):
    if not skill or not hf_token:
        st.warning("Please enter both your skill and token.")
    else:
        with st.spinner("Talking to the AI assistant..."):
            output = generate_jobs(skill, hf_token)
            st.text_area("Here are some project listings:", output, height=300)
