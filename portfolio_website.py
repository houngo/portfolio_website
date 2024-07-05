import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key= api_key)

model = genai.GenerativeModel('gemini-1.5-flash')
st.image("images/robot.png")
col1,col2 = st.columns(2)
with col1:
    st.subheader("HI :wave:")
    st.title("My Teacher's Name : Murtaza ")
with col2:
    st.image("images/Murtaza.png")
st.title(" ")

persona = """ You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 
         
        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.
 
        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """
st.title("Eli's AI Bot ")
st.write("Ask any information  about My Teacher:")
user_question = st.text_input("")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that "+user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")
col1,col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel for my Teacher ")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")


with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")

st.title(" ")
st.title("My  Setup ")
st.image("images/artificial.png")
st.title("My Skills")
st.slider("Student",0,100,70)
st.slider("Learning Program Python ",0,100,50)
st.slider("Arduino Programing",0,100,75)

# st.file_uploader("upl")
st.title(" ")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/artificial.jpg")
    st.image("images/g.png")
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")


with col2:
    st.image("images/image1.png")
    st.image("images/g3.jpg")
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")


with col3:
    st.image("images/image2.png")
    st.image("images/g6.jpg")
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")

st.subheader(" ")
st.write(" CONTACT")
st.write("For any inquiries ,please contact me")
st.write("ablamhoungo@gmail.com")
