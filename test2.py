import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.write("Hello :) ")
st.header("Hi")

#Display text
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3])
#st.write_stream(my_generator)
#st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("_Markdown_")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.html("<p>Hi!</p>")
st.code("print('Hello, World!')", language='python')  


btn = st.button("Submit")
# If the button is clicked, display an information message
if btn:
    st.info("Info")

option = st.radio("Select", ['A', 'B', 'C'])
#Display a message based on the selected option
if option == "A":
    st.warning("Warning :/")  # Display a warning message
elif option == "B":
    st.error("Error :(")       # Display an error message
elif option == "C":
    st.success("Success :)")   # Display a success message

chk = st.checkbox("I agree")
# If the checkbox is checked, display a custom exception message
if chk:
    st.exception("Agreement")


option = st.selectbox("Select", ['A', 'B', 'C'])
# Display different messages based on the selected option
if option == 'A':
    st.warning("Warning :/")
elif option == 'B':
    st.error("Error :(")
elif option == 'C':
    st.success("Success :)")
