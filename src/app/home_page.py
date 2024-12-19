import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


if "current_summary" not in st.session_state:
    st.session_state['current_summary'] = []



current_summary = st.Page("./get_summary.py", title='Get summary')
home_page = st.Page("./view_history.py", title='View History')
search_page = st.Page("./search.py", title='Search')

pg = st.navigation([current_summary, home_page, search_page])
pg.run()