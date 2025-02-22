import streamlit as st
import requests

st.set_page_config(page_title="Chat Application", page_icon="💬", layout="wide")

API_URL = "https://astronowai.fly.dev"  # Replace with your actual API URL

# Sidebar Navigation
page = st.sidebar.selectbox("Select Page", ["User Info", "Setup Chat", "New Chat"])

if page == "User Info":
    st.title("User Information")

    user_name = st.text_input("User Name:")
    date_of_birth = st.text_input("Date of Birth (DD-MM-YYYY):")
    place_of_birth = st.text_input("Place of Birth:")
    time_of_birth = st.text_input("Time of Birth (HH:MM:SS):")
    gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
    email = st.text_input("Email:")

    if st.button("Submit User Info"):
        if user_name and date_of_birth and place_of_birth and time_of_birth and gender and email:
            with st.spinner("Processing..."):
                try:
                    response = requests.patch(f"{API_URL}/user-info", json={
                        "user_name": user_name,
                        "date_of_birth": date_of_birth,
                        "place_of_birth": place_of_birth,
                        "time_of_birth": time_of_birth,
                        "gender": gender,
                        "email": email
                    })
                    data = response.json()
                    st.success("User info submitted successfully!")
                    st.markdown(f"### User ID: {data.get('user_id', 'N/A')}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please fill in all fields before submitting.")

elif page == "New Chat":
    st.title("New Chat")

    # Input fields
    chat_id = st.text_input("Enter Chat ID:")
    user_id = st.text_input("Enter User ID:")
    query = st.text_area("Enter your query:", height=150)

    if st.button("Send"):
        if chat_id and user_id and query:
            with st.spinner("Processing..."):
                try:
                    response = requests.post(f"{API_URL}/chat", json={
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
elif page == "Setup Chat":
    st.title("Setup Chat")

    # Input fields
    user_id = st.text_input("Enter User ID:")
    chat_type = st.selectbox("Select Chat Type:", ["CAREER", "LOVE", "WEALTH", "HEALTH"])

    if st.button("Start Chat"):
        if user_id and chat_type:
            with st.spinner("Processing..."):
                try:
                    response = requests.post(f"{API_URL}/chat/initialize", json={
                        "user_id": user_id,
                        "chat_type": chat_type
                    })
                    response.raise_for_status()
                    data = response.json()
                    st.success("Chat created successfully!")
                    st.markdown(f"### Chat ID: {data.get('chat', {}).get('id', 'N/A')}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please fill in all fields before starting a chat.")