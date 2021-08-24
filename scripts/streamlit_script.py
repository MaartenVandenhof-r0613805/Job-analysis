import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import streamlit as st


@st.cache
def load_data():
    with open('E:/Projects/Job analysis/data/Jobcards.json', "r") as json_file:
        data = json.load(json_file)
        data = pd.read_json(data)
    return data


# Load data
cards_df = load_data()
cities = pd.read_csv("../data/cities_be.csv")
cities["lon"] = cities["lng"]
# Drop null
cards_df = cards_df.dropna()

# Replace backspaces with ""
for name in cards_df.columns:
    cards_df[name] = [a.replace("\n", "") for a in cards_df[name]]

# Select city as Location
cards_df["Location"] = [a.split()[0].replace(",", "") for a in cards_df["Location"]]

# Data Scientist
dc_titles = [("scientist" in a) | ("Scientist" in a) | ("science" in a) | ("Science" in a) for a in cards_df["Title"]]
dc_cards = cards_df[dc_titles]

# Data Analyst
da_titles = [("analyst" in a) | ("Analyst" in a) for a in cards_df["Title"]]
da_cards = cards_df[da_titles]

# Data engineers
de_titles = [("engineer" in a) | ("Engineer" in a) for a in cards_df["Title"]]
de_cards = cards_df[de_titles]

# Print amounts
print("Data Scientist jobs: " + str(dc_cards["Title"].count()) +
      ", Data Engineer jobs:  " + str(de_cards["Title"].count()) +
      ", Data Analyst jobs:  " + str(da_cards["Title"].count()))

st.subheader('Data Science jobs')
dc_counts = pd.DataFrame(dc_cards.groupby(["Location"])["Title"].count().sort_values(ascending=False))
st.bar_chart(dc_counts)
dc_counts = dc_counts.reset_index()

dc_counts_cities = dc_counts.merge(cities, left_on="Location", right_on="city")
print(dc_counts_cities)
st.map(dc_counts_cities)
