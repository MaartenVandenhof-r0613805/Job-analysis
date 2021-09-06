import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import streamlit as st

# Load data
cards_df = pd.read_csv("../data/complete_df.csv")
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
st.subheader(title + ' jobs')
counts = pd.DataFrame(df_show.groupby(["Location"])["Title"].count())
st.bar_chart(counts)

# Create map
st.map(df_show)
