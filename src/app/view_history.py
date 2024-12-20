import time
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

def render_table(df):
    table_html = f"""
    <style>
        table {{
            width: 100%;
            border-collapse: collapse;
            overflow-x: auto;
            display: block;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
            white-space: pre-wrap; /* Wrap text */
            word-wrap: break-word; /* Wrap long words */
        }}
        th {{
            background-color: var(--background-secondary-color);
            color: var(--text-color);
            font-weight: bold;
        }}
        td {{
            background-color: var(--background-color);
            color: var(--text-color);
        }}
        tr:nth-child(even) td {{
            background-color: var(--background-secondary-color);
        }}
        tr:hover td {{
            background-color: var(--primary-color);
            color: var(--text-color-inverse);
        }}
    </style>
    <table>
        <thead>
            <tr>
                {''.join(f'<th>{col}</th>' for col in df.columns)}
            </tr>
        </thead>
        <tbody>
            {''.join('<tr>' + ''.join(f"<td><a href={str(cell)}>{str(cell)}</a></td>" if isinstance(cell, str) and cell.startswith('https') else f"<td>{str(cell)}</td>" for cell in row ) + '</tr>' for row in df.values)}
        </tbody>
    </table>
    """
    return table_html

COLS = ['url', 'short_summary', 'long_summary']
try:
    df = pd.read_csv('./data/master_summaries.csv')[COLS]
except (FileNotFoundError, Exception) as e:
    df = None
    st.markdown("<b><i>Once any summary is generated, it will be shown here.</i></b>", unsafe_allow_html=True)
    
    pbar_text = 'Going to Home Page...'
    pbar = st.progress(0, text=pbar_text)
    
    for percent_complete in range(100):
        time.sleep(0.05)
        pbar.progress(percent_complete + 1, text=pbar_text)
    st.switch_page("./get_summary.py")

if df is not None and df.shape[0] > 0:
    st.markdown(render_table(df), unsafe_allow_html=True)
