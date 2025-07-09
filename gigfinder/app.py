import streamlit as st
import requests

# ✅ load token securely
hf_token = st.secrets["huggingface"]["api_token"]
st.write("🔑 Token Preview:", hf_token[:8] + "..." if hf_token else "❌ Not loaded")


# ✅ headers used for authorization
headers = {
    "Authorization": f"Bearer {hf_token}"
}

# ✅ simple test function
def test_model():
    payload = {"inputs": "Say Hello"}
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.status_code, response.text

# ✅ test in UI
st.title("🔍 Hugging Face Token Debug")
status, text = test_model()
st.write("Status Code:", status)
st.code(text)
