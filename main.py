import requests
import streamlit as st
import edge_tts
import asyncio
from io import BytesIO
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
       "messages":[{"role":"system","content":"you are expert interviewer evaluate the answer of users"},
                  {"role":"user","content":Question}]
    }
    response=requests.post(api_url,headers=headers,json=payload)
    result=response.json()
    return result["choices"][0]["message"]["content"]
Question=st.text_input("")
answer=Ask_friend(Question)
#voice function
async def get_neural_audio(answer) -> BytesIO:
    communicate = edge_tts.Communicate(text, "en-US-AndrewNeural")
    audio_buffer = BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_buffer.write(chunk["data"])
    audio_buffer.seek(0)
    return audio_buffer
if st.button("Ask"):
    st.markdown(answer)
    #______voice output------
    if answer:
        with st.spinner("Synthesizing neural voice..."):
            sound_stream = asyncio.run(get_neural_audio(answer))
            st.audio(sound_stream, format="audio/mp3", autoplay=True)
