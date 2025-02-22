import streamlit as st
import requests

API_URL = "https://astronowai.fly.dev/chat"  # Replace with your actual API URL

st.title("AstroNow")

# Input fields
chat_id = st.text_input("Enter Chat ID:")
user_id = st.text_input("Enter User ID:")
query = st.text_area("Enter your query:", height=150)

if st.button("Send"):
    if chat_id and user_id and query:
        with st.spinner("Processing..."):
            try:
                response = requests.post(API_URL, json={
                    "chat_id": chat_id,
                    "user_id": user_id,
                    "query": query
                })
                response.raise_for_status()
                data = response.json()
                st.markdown("### Response:")
                st.text_area("Next Message:", data.get("next_message", "No next message"), height=300)
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please fill in all fields before sending.")
