import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path


# Load path
current_dir = Path.cwd()
# Load data
cards_df = pd.read_csv(current_dir / 'complete_df.csv')
cards_df["lon"] = cards_df["lng"]

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

# Create buttons
df_show = dc_cards
title = "Data Science"
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

# Create Bar chart
df = pd.DataFrame(df_show.groupby(["Location", "Experience"])["Experience"].count().sort_values(ascending=False))
df = df.rename(columns={"Experience": "Count"})
df = df.reset_index()

stacked_bar = alt.Chart(df).mark_bar().encode(
    x='Location',
    y='Count',
    color='Experience',
    tooltip=["Count", "Experience"]
).properties(
    width=800,
    height=500,
    title="Job type: " + title
).interactive()
st.altair_chart(stacked_bar)

# Create map
st.map(df_show)

