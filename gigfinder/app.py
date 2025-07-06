import streamlit as st
import requests

# Function to call Hugging Face LLM API
def generate_jobs(skill, hf_token):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {
        "Authorization": f"Bearer {hf_token}"
    }

    # System-level prompt
    prompt = f"""
You are an AI freelance assistant. Given the skill '{skill}', generate 3 realistic freelance project listings.
Each listing must include:
- Platform (Upwork, Fiverr, Freelancer, Glassdoor)
- Title of the job
- Budget or Pay
- 1-line Summary of the work
Give clear output in bullet format.
"""

    # Call the model
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except:
            return "Model response format not understood. Try a different model or prompt."
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# Streamlit UI
st.set_page_config(page_title="GigFinder", page_icon="💼")
st.title("🤖 GigFinder - AI-Powered Freelance Project Assistant")

skill = st.text_input("Enter your skill (e.g., Python, UI/UX, Graphic Design)")
hf_token = st.text_input("Enter your Hugging Face API token", type="password")

if st.button("Find Projects"):
    if not skill or not hf_token:
        st.warning("Please enter both your skill and Hugging Face token.")
    else:
        st.info("⏳ Asking the AI assistant...")
        output = generate_jobs(skill, hf_token)
        st.text_area("🧾 Freelance Listings", output, height=300)
