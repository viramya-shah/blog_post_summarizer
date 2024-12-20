import streamlit as st
from openai import OpenAI
from src.model.web_scraper import WebScraper
from src.model.summary_generator import Summary
import json
import os

webscraper = WebScraper()

st.set_page_config(layout="wide")
st.title('Summarize')

prompt_config = json.load(open("./src/config/prompt.json", 'r'))

input_url = st.text_area(label="Paste the URLs here (enter each in a new line)")

if input_url is not None and len(input_url) > 0:
    input_url_list = input_url.split("\n")

    # TODO: _validate_urls()

    with st.status('Generating Summary'):
        st.write('Fetching content...')
        docs = webscraper.scrape(urls=input_url_list, nested=False)
        st.write('Generating summary...')
        client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        summary = Summary(client=client, prompts=prompt_config)
        summary_docs = summary.generate_summary(documents=docs)
        st.write('Making sure everything worked correctly...')
        for idx, url_and_ind_summary in enumerate(zip(input_url_list, summary_docs)):
            url, ind_summary = url_and_ind_summary
            st.session_state['current_summary'].append((idx, url, ind_summary))

if len(st.session_state['current_summary']) > 0:
    st.markdown("All your searches (in this session) will appear below")
    for idx, url, ind_summary in st.session_state['current_summary'][::-1]:
        st.markdown(f"<a href='{str(url)}'><b>{ind_summary.title}</b></a>", unsafe_allow_html=True)
        st.markdown(ind_summary.short_summary)
        st.markdown('<hr>', unsafe_allow_html=True)