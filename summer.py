import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from pillow import Image
plt.style.use('seaborn')

image1=Image.open('CSL_Behring_Logo.jpg')

col1,col2,col3= st.columns([6,6,6])
with col1:
    st.write("")
with col2:
    st.image(image1,caption=None, width=200)
with col3:
    st.write('')
    

st.markdown("<h1 style='text-align: center; color: red;'>Information, Insights, and Analytics</h1>",unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'>Welcome to Enterprise Data Management </h2>", unsafe_allow_html=True)

col1, col2=st.columns([15,30])
image2=Image.open('Kamayini_Bio_Pic.jpg')
with col1:
    st.image(image2,caption="Kamayini Kaul, VP, Data Insights & Analytics",width=200)
with col2:
    st.markdown('<h1 style="color: black;">quote here</h1>', unsafe_allow_html=True)

with st.sidebar:
    st.header('Quick Links')
    st.write('Yahoo Finance [Stock](https://finance.yahoo.com/quote/CSLLY)')
    st.header('Graph Options')
    

df1=pd.read_csv('CSLLY.csv')

    
st.write(df1)

fig, ax = plt.subplots(figsize=(20,5))
radio=st.sidebar.radio('Select Open, High, Low, or Close', ('Open','High','Low','Close'))
if radio=='Open':
    df1['Open'].plot.hist(bins=30)
elif radio=='High':
    df1['High'].plot.hist(bins=30)
elif radio=='Low':
    df1['Low'].plot.hist(bins=30)
elif radio=='Close':
    df1['Close'].plot.hist(bins=30)

    
st.pyplot(fig)