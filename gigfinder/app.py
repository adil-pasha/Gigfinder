import streamlit as st

st.set_page_config(page_title="Test App", page_icon="🧪")
st.title("🧪 Streamlit Test App")

skill = st.text_input("Enter a skill")
if st.button("Click Me"):
    st.success(f"You entered: {skill}")
