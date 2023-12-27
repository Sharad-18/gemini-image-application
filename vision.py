from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image):
    model=genai.GenerativeModel("gemini-pro-vision")
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config("Gemini LLM  Application ")
st.header("Gemini LLM  Application")

input=st.text_input("Input: ",key="input")

upload_file=st.file_uploader("Choose an image..",type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="uploaded image ",use_column_width=True)
    
submit=st.button("tell me about the image ")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is ")
    st.write(response)
