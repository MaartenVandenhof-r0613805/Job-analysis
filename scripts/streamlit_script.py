import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

# Prepare data
# Load data
cards_df = pd.read_csv(Path(__file__).parents[1] / 'data' / 'complete_df.csv')
cards_df["lon"] = cards_df["lng"]
tech_df = pd.read_csv(Path(__file__).parents[1] / 'data' / 'tech_df.csv')

# Drop null
cards_df = cards_df.dropna()

# Data Scientist
dc_titles = [("scientist" in a) | ("science" in a) for a in cards_df["Title"]]
dc_cards = cards_df[dc_titles]

# Data Analyst
da_titles = [("analyst" in a) for a in cards_df["Title"]]
da_cards = cards_df[da_titles]

# Data engineers
de_titles = [("engineer" in a) for a in cards_df["Title"]]
de_cards = cards_df[de_titles]

# Create layout
# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")
# Create buttons
df_show = dc_cards
title = "Data Science"
st.sidebar.write('''## Select job type''')
with st.sidebar:
    if st.button("Data Science"):
        title = "Data Science"
        df_show = dc_cards
    if st.button("Data Analyst"):
        title = "Data Analyst"
        df_show = da_cards
    if st.button("Data Engineer"):
        title = "Data Engineer"
        df_show = de_cards

# Create intro
'''
# LinkedIn job analysis for data jobs in Belgium

Examining the job description results given by LinkedIn when searching for the term **Data Science** in Belgium.
Select the job type in the left sidebar to see the results for the selected job.
'''
st.write('''### Current job type shown:  *''' + title + '''*''')
'''
# Location Analysis:
'''
# Create horizontal layout for location
col1, col2 = st.columns(2)
col1.header('''Job postings in each city for *''' + title + '''* jobs''')
col2.header('''Location of  *''' + title + '''* jobs on the map''')

# Create Bar chart
df = pd.DataFrame(df_show.groupby(["Location", "Experience"])["Experience"].count().sort_values(ascending=False))
df = df.rename(columns={"Experience": "Count"})
df = df.reset_index()

stacked_bar = alt.Chart(df).mark_bar().encode(
    x=alt.X("Location", sort=alt.EncodingSortField(field="Count", op="count", order="descending")),
    y='Count',
    color='Experience',
    tooltip=["Count", "Experience"]
).properties(
    width=700,
    height=600,
    title="Job type: " + title
).interactive()
col1.altair_chart(stacked_bar)

# Create map
col2.map(df_show)

# Job Specific skills
'''
# Job Description Analysis
'''
# Create count chart
horizontal_bar_count = alt.Chart(tech_df[title].value_counts().reset_index()).mark_bar().encode(
    x=alt.X("index", title="Skills", sort=alt.EncodingSortField(field=title, op="count", order="ascending")),
    y=alt.Y(title, title="Count"),
    tooltip=[title]
).properties(
    width=700,
    height=600,
    title="Most requested skilss in " + title
).interactive()

st.altair_chart(horizontal_bar_count)