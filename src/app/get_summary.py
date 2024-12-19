import streamlit as st
from openai import OpenAI
from src.model.web_scraper import WebScraper
from src.model.summary_generator import Summary
import json
import os
from itertools import chain

webscraper = WebScraper()

st.title('Summarize')



input_url = st.text_area(label="Paste the URLs here (enter each in a new line)")

if input_url is not None and len(input_url) > 0:
    input_url_list = input_url.split("\n")

    # TODO: _validate_urls()

    docs = webscraper.scrape(urls=input_url_list, nested=False)

    prompt_config = json.load(open("./src/config/prompt.json", 'r'))

    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    summary = Summary(client=client, prompts=prompt_config)

    summary_docs = summary.generate_summary(documents=docs)

    st.session_state['current_summary'].append(summary_docs)

# clean_button = st.sidebar.button("Clean")
# if clean_button:
#     st.session_state['current_summary'] = []

if len(st.session_state['current_summary']) > 0:
    st.write(list(map(lambda x: x.short_summary, chain.from_iterable(st.session_state['current_summary']))))
