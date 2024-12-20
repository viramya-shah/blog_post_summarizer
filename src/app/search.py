import time
import streamlit as st

st.title("Search")

refresh_button = st.sidebar.button(label='Refresh')
if refresh_button:
    time.sleep(2)
    st.sidebar.write('Refreshed')

st.markdown("<i><center><h3>Work in progress. Coming soon!</center></i>", unsafe_allow_html=True)
keywords = st.text_input(label="Search the knowledge base...", disabled=True)
