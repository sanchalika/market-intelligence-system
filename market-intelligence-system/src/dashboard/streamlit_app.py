import streamlit as st
import pandas as pd
import altair as alt


st.title("Market Intelligence Dashboard")
df = pd.read_parquet("data/sample/tweets_sample.parquet")
st.write("Sample Data:", df.head())
chart = alt.Chart(df).mark_bar().encode(
x='created_at:T',
y='likes:Q'
)

st.altair_chart(chart, use_container_width=True)