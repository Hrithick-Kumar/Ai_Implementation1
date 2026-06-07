import requests
import streamlit as st
st.title("AI Implementation")
st.write("AI implementation")

def Ask_friend():
    api_url="https://openrouter.ai/api/v1/chat/completions"
    api_key=st.secrets["Chat_bot"]
    headers={
        "Authorization":f"Bearer {api_key}",
        "Content-Type":"application/json"
    }
    payload={
       "model":"openrouter/free",
       "message":[{"role":"system","content":"You are Shweta.you are expert interviewer and ask questions related to programming only"},
                  {"role":"user","content":Question}]
    }
    response=requests.post(api_url,headers=headers,json=payload)
    result=response.json()
    return result["choices"][0]["message"]["content"]
Question=st.text_input("",values="Ask Shweta")
answer=Ask_friend()
st.markdown(answer)
