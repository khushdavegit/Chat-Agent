import streamlit as st
import requests
import base64

API_URL = "http://127.0.0.1:8000/query"

st.title("🚢 Titanic Chatbot")

query = st.text_input("Ask a question about the Titanic dataset:")

if st.button("Submit"):
    if query:
        response = requests.post(API_URL, json={"query": query}).json()

        if "answer" in response:
            st.success(response["answer"])
        elif "image" in response:
            img_data = base64.b64decode(response["image"])
            st.image(img_data, caption="Generated Visualization", use_column_width=True)
        else:
            st.error("Unexpected response from the server.")
    else:
        st.warning("Please enter a question.")
