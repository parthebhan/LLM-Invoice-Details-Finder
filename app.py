import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure the API key
api_key = st.secrets["auth_token"]
genai.configure(api_key=api_key)

# Create a generative model
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def get_gemini_response(input,image,prompt):
  response = model.generate_content([input,image[0],prompt])
  return response.text

def input_image_details(uploaded_file):
  if uploaded_file is not None:

    bytes_data = uploaded_file.getvalue()

    image_parts = [
      {
        "mime_type":uploaded_file.type,
        "data":bytes_data

      }
    ]
    return image_parts
  else:
    raise FileNotFoundError("No File Uploaded") 
  


# Initialize Streamlit App

st.set_page_config(page_title="LLM - Invoice Extractor")

input = st.text_input("Input prompt: ",key='input')
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=['jpg','jpeg','png'])

image=""
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image ,caption="Uploaded File.",use_column_width=True)

submit = st.button("Tell Me about the Invoice")



input_prompt = """
You are an expert in understanding the invoices.we will upload a image of invoice  
and you will have to answer based on the uploaeded invoice image

"""

# if submit button is clicked
if submit:
  image_data = input_image_details(uploaded_file)
  response=get_gemini_response(input_prompt,image_data,input)
  st.subheader("The response is")
  st.write(response)
