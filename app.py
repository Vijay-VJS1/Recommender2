import streamlit as st
import os
##################
st.set_page_config(page_title='👻👻🚗🌫️‍', page_icon='👻',
                   layout="wide", initial_sidebar_state="collapsed",
                   menu_items=None)
from Recommender import *
# from Download import *
##################
page = st.sidebar.selectbox('Select page',['Recommender','Download Data'])
# st.markdown(os.listdir(os.getcwd()))

if page=='Recommender':
    Recommender()
    st.markdown("Recommend")
elif page=='Download Data':
#     Download()
  st.markdown("Download")
