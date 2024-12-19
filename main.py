from src.model.web_scraper import WebScraper
from src.model.summary_generator import Summary
from openai import OpenAI
import json
import os
import pandas as pd


# web scraper
urls = [
    'https://swiggybytes.medium.com/capturing-data-and-photographs-a-swiggy-managers-analytical-adventure-37edcbe7d16e',
    'https://swiggybytes.medium.com/solving-the-tech-puzzle-a-senior-lead-software-engineers-empowering-story-26dc647f7d04',
    'https://dev.to/programmerraja/generative-ai-a-personal-deep-dive-my-notes-and-insights-1ph0'
]

webScraper = WebScraper()
content = webScraper.scrape(urls=urls, nested=False)

# llm
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
prompt_config = json.load(open("./config/prompt.json", 'r'))

# summary
summary = Summary(client=client, prompts=prompt_config)
s = summary.generate_summary(documents=content)
# print(s)


# csv view
df = pd.read_csv("./data/master_summaries.csv")
print(df)
# db save
# Prolly a simple CSV file. BTS a vector+keyword index is stored. It gets triggered on a manual user refresh. 
# Breakdown
# 1) Save the summaries in a CSV file. Append the new ones to it. 


# streamlit application
# 3 pages - View current summaries, view all summaries and search for previous records. 

