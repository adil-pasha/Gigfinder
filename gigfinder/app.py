import streamlit as st
import openai

# Load OpenAI API key from secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Define the assistant function
def generate_projects(skill):
    prompt = f"""
You are a freelance project assistant. Based on the skill '{skill}', list 3 relevant freelance projects.
Each project should include:
- Platform (like Upwork, Fiverr, Freelancer, Glassdoor)
- Project Title
- Budget or Payment
- A 1-line description
Format output clearly using bullet points.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that helps freelancers find projects."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"❌ Error: {e}"

# -------- Streamlit UI --------
st.set_page_config(page_title="GigFinder AI", page_icon="💼")
st.title("🤖 GigFinder - Freelance Project Assistant")

skill = st.text_input("Enter your skill or category (e.g., Python, UI/UX, WordPress)")

if st.button("Find Freelance Projects"):
    if not skill.strip():
        st.warning("⚠️ Please enter a skill.")
    else:
        with st.spinner("🔍 Searching..."):
            output = generate_projects(skill)
            st.text_area("📋 Project Listings", output, height=300)
