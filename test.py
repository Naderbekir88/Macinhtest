#import lib
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("Hello World :) ")

## Disply text

# Displaying Text

# Display simple text
st.text("Text")  

# Display text with 'write', which is a versatile function that can display different types of content
st.write("Super Function")  

# Display a header, which is typically larger and bolder than normal text
st.header("Header")  

# Display a sub-header, slightly smaller than header
st.subheader("Sub-Header")  

# Display text using Markdown syntax for more formatting options
st.markdown("**Markdown**")  

# Display formatted code, which can be syntax highlighted for various languages
st.code("print('Hello, World!')", language='python')  

# Display mathematical expressions using LaTeX
st.latex(r"e^{i\pi} + 1 = 0")  

# Displaying Interactive Widgets

# Create a button that users can click
btn = st.button("Submit")
# If the button is clicked, display an information message
if btn:
    st.info("Info")

# Create a set of radio buttons for users to select an option
option = st.radio("Select", ['A', 'B', 'C'])
# Display a message based on the selected option
if option == "A":
    st.warning("Warning :/")  # Display a warning message
elif option == "B":
    st.error("Error :(")       # Display an error message
elif option == "C":
    st.success("Success :)")   # Display a success message

# Create a checkbox that users can check or uncheck
chk = st.checkbox("I agree")
# If the checkbox is checked, display a custom exception message
if chk:
    st.exception("Agreement")

# Using interactive widgets in Streamlit

# Create a select box for users to choose an option
option = st.selectbox("Select", ['A', 'B', 'C'])
# Display different messages based on the selected option
if option == 'A':
    st.warning("Warning :/")
elif option == 'B':
    st.error("Error :(")
elif option == 'C':
    st.success("Success :)")

# Create a slider to select an age between 0 and 100
age = st.slider("Select Age", 0, 100)

# If the intention is to create another select slider, here's how it might look:
rating = st.select_slider("Select Rating", options=['A', 'B', 'C'])

# Create a single-line text input field
text_input = st.text_input("Enter a text")

# Create a multi-line text area for longer input
text_area = st.text_area("Enter a paragraph")

# File uploader widget allows users to upload files which can then be used in the app.
st.file_uploader("Upload")

# Camera input widget enables users to take a photo using their device's camera.
st.camera_input("Take a Photo")

# Date input widget allows users to select a date from a calendar.
st.date_input("Today")

# Time input widget allows users to input a time value.
st.time_input("Now")

# Number input widget lets users input a numerical value. It can be fine-tuned for step values, min/max limits, etc.
st.number_input("Num")

# Multiselect widget provides a list of options from which users can select multiple items.
st.multiselect("Select", ['A', 'B', 'C'])

# Color picker widget enables users to select a color from a color palette.
st.color_picker("Colors")


import seaborn as sns  # Importing seaborn for dataset loading
import streamlit as st  # Importing streamlit for creating web apps

# Load a dataset named 'taxis' from seaborn's built-in datasets
df = sns.load_dataset('taxis')

# Initially display the entire dataframe using Streamlit
st.write(df)

# Create a button in the Streamlit app labeled "Show Data"
btn = st.button("Show Data")

# When the button is clicked, display a random sample of 5 rows from the dataframe
if btn:
    st.dataframe(df.sample(5))


import pandas as pd              # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import streamlit as st           # Import Streamlit for creating web apps

# Load data from a CSV file
df = pd.read_csv('company_sales_data.csv')

# Display the first few rows of the DataFrame
st.write(df.head())

# Add a header in the Streamlit app
st.header("Matplotlib")

# Add a subheader in the Streamlit app
st.subheader("Line Plot")

# Create a figure for plotting
fig, ax = plt.subplots(figsize=(15, 8))  
# Plotting data: months on the x-axis and total profit on the y-axis
ax.plot(df['Sales'], df['profit'])

# Setting title and labels with custom font sizes
ax.set_title("Month vs. Profit", fontsize=20)
ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Profit", fontsize=14)

# Display the plot in the Streamlit app
st.pyplot(fig)
