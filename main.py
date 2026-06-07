import requests
import streamlit as st
st.title("AI Implementation")
st.write("AI implementation")
def ask_ai(question):

    api_key = st.secrets["Chat_bot"]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openrouter/free",
        "messages": [{
                "role": "user",
                "content": question
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]


question = st.text_input("Ask Question: ")

answer = ask_ai(question)
st.markdown(answer)
