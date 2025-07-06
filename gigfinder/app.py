def generate_jobs(skill, hf_token):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
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
