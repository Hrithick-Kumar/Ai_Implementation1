import requests
import streamlit as st
from gtts import gTTS
st.title("AI Implementation")
st.write("AI implementation")

def Ask_friend(Question):
    api_url="https://openrouter.ai/api/v1/chat/completions"
    api_key=st.secrets["Chat_bot"]
    headers={
        "Authorization":f"Bearer {api_key}",
        "Content-Type":"application/json"
    }
    payload={
       "model":"openrouter/free",
       "messages":[{"role":"system","content":"You are Shweta.you are expert interviewer and ask questions related to programming only"},
                  {"role":"user","content":Question}]
    }
    response=requests.post(api_url,headers=headers,json=payload)
    result=response.json()
    return result["choices"][0]["message"]["content"]
Question=st.text_input("",value="Ask Shweta")
answer=Ask_friend(Question)
st.markdown(answer)

#______voice output------
text = "Hello! This is a cloud-based text to speech example."
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
output_file = "welcome.mp3"
speech.save(output_file)
st.audio(output_file)
