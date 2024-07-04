import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key = api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2 = st.columns(2)
with col1:
    st.subheader("HI :wave:")
    st.title("My Teacher's Name : Murtaza ")
with col2:
    st.image("images/Eli.png")
st.title(" ")
persona = ""
st.title("Eli's AI Bot ")
st.write("Ask anything about  me ")
user_question = st.text_input("")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that "+user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")
col1,col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel ")
    st.write("-  Largest Computer Vision Channel")
    st.write("- L400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")


with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")

st.title(" ")
st.title("My  Setup ")
st.image("images/Eli.png")
st.title("My Skills")
st.slider("Programming",0,100,70)
st.slider("Programming",0,100,85)
st.slider("Programming",0,100,75)

st.file_uploader("upl")


col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/Eli.png")


with col2:
    st.image("images/Eli.png")


with col3:
    st.image("images/Eli.png")


st.subheader(" ")
st.write(" CONTACT")
st.write("for any inquiries ,please contact me")
st.write(" ablamhoungo@gmail.com")
