import streamlit as st

#Test/Title
st.title("My stremlit project") 
st.header(" As we know deploying any machine learning proble required lot of work")
st.subheader("This is my little approch to get more from it ") 

st.text("here you gonna see all my project work in and all information")

st.error("sucec j")
st.help(range)
st.write(range(10))
from PIL import Image 
img=Image.open("476827_PR.png")
st.image(img,caption="are you suprice ")


if st.checkbox("show/hide"):
    st.text("show or hidden widget ")


status=st.radio("FBHDSBHBHB",("Active","inactive"))
if status=="Active":
    st.success("your active ")
else :
    st.warning("inactive")    


knowleage=st.selectbox("knowleage in",['programming','doctor','web design'])        
st.write('you want to know about ', knowleage)

location=st.multiselect("where you want to work",('location','mumbai','lonavla'))
level=st.slider("whats your level",1, 6 )