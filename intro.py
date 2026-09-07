import streamlit as st 
st.title("My First Streamlit App Created by NIT")
st.write("Welcome! This app calculates the square of a number.") 
st.header("Select a Number") 
number = st.slider("Pick a number", 0, 0, 5) 
st.subheader("Result") 
squared_number = number * number 
st.write(f"The square of **{number}** is **{squared_number}**.")