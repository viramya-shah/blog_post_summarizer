import streamlit as st
import pandas as pd


df = pd.read_csv('./data/master_summaries.csv')[['id', 'url', 'short_summary', 'long_summary']]

st.dataframe(df)