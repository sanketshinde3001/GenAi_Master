import streamlit as st

st.title("Multi Functional GENAI Application")
st.write("This Project is Under Development and OpenSource for everyone.")
st.header(">>>>Open sidebar to use this app<<<<")

st.subheader("Current Features")
tab1, tab2 , tab3 , tab4 = st.tabs(["TextGen", "Image-Gen","Chatbot","Summerization"])

with tab1:
    st.subheader("Text Generation")
    with st.expander("1) Email Generation"):
        st.write("A) Compose Email \n On basis of given input , it will generate email")

        st.write("B) Reply to Email \n it will understand given email & reply it.")

    with st.expander("2) Post Generation"):
        st.write("A) Linkedin Posts \n B) X/Twitter Posts")

    with st.expander("3) Eassy Generation"):
        st.write("Eassay will generate as per given topic.")

    with st.expander("4) Text Generation"):
        st.write("As Anything Random")


with tab2:
    st.subheader("Interact with Images")
    with st.expander("1) Image Generation"):
        st.write("As per given Prompt , Image get generated")

    with st.expander("2) Recipe Maker"):
        st.write("As per given Prompt , Image get generated")

    with st.expander("3) Object Classifier"):
        st.write("Objects get classified from photo.")



with tab3:
    st.subheader("Chatbots")
    st.write("Just like Chatgpt , Bard. Here also , we can chat with llm models.")




with tab4:
    st.subheader("Summerization")
    st.write("Coming Soon....")

st.subheader("upcoming Features 👇")

st.write("Chat with pdf")
st.write("Chat with txt")
st.write("Chat with csv")
st.write("Chat with Youtube Video")
st.write("Chat with Url")

st.write("Summerize Paragraph")
st.write("Summerize Conversation")
st.write("Summerize Website")
st.write("Summerize Youtube Video")

st.write("\n \n Weekly updates . so stay tuned")