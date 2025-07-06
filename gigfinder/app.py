import streamlit as st

# Mock freelance project listings
project_listings = {
    "python": [
        {"platform": "Upwork", "title": "Automate Excel Reports", "budget": "$250", "desc": "Automate reports using pandas."},
        {"platform": "Freelancer", "title": "PDF Parser", "budget": "₹4,500", "desc": "Parse scanned PDFs with Python."},
        {"platform": "Fiverr", "title": "Automation Bot", "budget": "₹2,000", "desc": "Create bot for browser tasks."}
    ],
    "design": [
        {"platform": "Fiverr", "title": "Logo for Clothing Brand", "budget": "₹2,500", "desc": "Minimalist logo for streetwear."},
        {"platform": "Upwork", "title": "Poster Design", "budget": "$150", "desc": "Design event posters in Illustrator."},
        {"platform": "Freelancer", "title": "UI/UX for Web App", "budget": "₹5,000", "desc": "Design UI screens for dashboard."}
    ]
}

st.set_page_config(page_title="GigFinder", page_icon="🧠")
st.title("🤖 GigFinder - Your Freelance Project Buddy")

category = st.text_input("What is your skill/category? (e.g., Python, Design)").lower()

if st.button("Find Projects"):
    if category in project_listings:
        st.subheader(f"🔎 Projects for '{category}'")
        for job in project_listings[category]:
            st.markdown(f"""
            **Platform**: {job['platform']}  
            **Title**: {job['title']}  
            **Budget**: {job['budget']}  
            **Description**: {job['desc']}  
            ---
            """)
    else:
        st.warning("Sorry, no projects found for this category. Try 'Python' or 'Design'.")

