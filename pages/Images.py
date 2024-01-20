import streamlit as st
from PIL import Image
import google.generativeai as genai

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

with st.sidebar:
    # Here we take Gemini API as a Input from user
    api_key = st.text_input("API Key", type="password")
    st.markdown("[Get Your API Key](https://makersuite.google.com/app/apikey)")

    option = st.selectbox(
    'Select type of app you want?',
    ('Ask to Photo', 'Photo to Recipe', 'Photo to Object list'))

genai.configure(api_key=api_key)   

##initialize our streamlit app
if(option=="Photo to Recipe"):
    st.header("Recipe Maker")
    input = "This given photo is may be food or not.If not then just say its not food. But if Given photo is food dish then create a vibrant recipe that captures its essence and guides even novice cooks to culinary success I want recipe of this dish. Give me recipe of this dish in following format. 1)Key ingredients: [List the main ingredients you can identify in the photo] 2)Culinary style: [Indicate the cuisine or cooking style, if apparent] 3)Desired recipe format: [Specify a step-by-step or narrative format] 4)Servings: [Mention the number of servings you'd like the recipe to yield] 5)Cooking time: [Approximate cooking time, if preferred] 6)Additional considerations: Dietary restrictions: Note any dietary needs (vegan, gluten-free, etc. 7)Creative variations: Encourage the AI to suggest alternative ingredients or regional variation "


    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)


    submit=st.button("Give Me Recipe")

## If ask button is clicked
    if not api_key:
        st.info("Please add your API key to continue.")

    elif submit:  
        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)

if(option=="Ask to Photo"):
    st.header("Ask Question to Image")
    input=st.text_input("Input Prompt: ",key="input")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)


    submit=st.button("Tell me about the image")

## If ask button is clicked
    if not api_key:
        st.info("Please add your API key to continue.")
    elif submit:
        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)


if(option=="Photo to Object list"):
    st.header("Object Classifier")
    input="Extract the objects in the provided image and output them in a list in alphabetical order"

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)


    submit=st.button("Classify")

## If ask button is clicked
    if not api_key:
        st.info("Please add your API key to continue.")
    elif submit:
        response=get_gemini_response(input,image)
        st.write(response)