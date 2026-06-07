import requests
import streamlit as st
st.title("AI Implementation")
st.write("AI implementation")
def ask_ai(question, stream):

    api_key = st.secrets[
        "OPENROUTER_API_KEY"
    ]

    headers = {
        "Authorization":
        f"Bearer {api_key}",

        "Content-Type":
        "application/json"
    }

    payload = {

        "model":
        "openrouter/free",

        "messages": [

            {
                "role": "system",

                "content": f"""
You are Margdarshak AI.

Student Recommended Stream:
{stream}

You are an expert career counselor.

Provide:

1. Career guidance
2. Career roadmap
3. Required skills
4. Future opportunities
5. Exam suggestions
6. College suggestions

Keep answers practical and student friendly.
"""
            },

            {
                "role": "user",

                "content": f"""
Recommended Stream:
{stream}

Question:
{question}
"""
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=60
    )

    data = response.json()

    return data[
        "choices"
    ][0][
        "message"
    ][
        "content"
  ]
