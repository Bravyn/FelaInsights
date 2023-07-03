import streamlit as st
from search_trends.display_csv import show_csv

t1, t2 = st.tabs(["Fella Trends", "Lyric Sentiments"])

with t1:
    st.subheader("Fella Trends")
    show_csv()
with t2:
    st.write("Lyric Sentiments")