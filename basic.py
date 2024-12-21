import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sidebar
option = st.sidebar.selectbox(
    "Select an option",
    [
        "Home",
        "Display Text",
        "Display Data",
        "Display Interactive Widgets",
        "Display Media",
        "Columns"
    ]
)

if option == 'Display Text':
    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.latex(r'''a\in\{i|i+1 = 0\}''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is', '<', '3']) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    st.code("print('Hello, World!')", language='python')

if option == "Display Interactive Widgets":
    st.button('Click me')
    #st.experimental_data_editor('Edit data', data)
    st.checkbox('I agree')
    st.radio('Pick one', ['cats', 'dogs'])
    st.selectbox('Pick one', ['cats', 'dogs'])
    st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
    st.slider('Pick a number', 0, 100)
    st.select_slider('Pick a size', ['S', 'M', 'L'])
    st.text_input('First name')
    st.number_input('Pick a number', 0, 10)
    st.text_area('Text to translate')
    st.date_input('Your birthday')
    st.time_input('Meeting time')
    st.file_uploader('Upload a CSV')
    #st.download_button('Download file', data)
    st.camera_input("Take a picture")
    st.color_picker('Pick a color')

if option == "Display Data":
    df = pd.read_csv('company_sales_data.csv')
    st.dataframe(df.head())
    st.table(df.iloc[0:3])
    st.json({'foo': 'bar', 'fu': 'ba'})
    st.metric('My metric', 42, 2)
