import streamlit as st
from search_trends.display_csv import plot_trend_data
from lyrics_sentiments.analyze_lyrics import lyrical_sentiment
from lyrics_sentiments.get_lyrics import lyrics
t1, t2 = st.tabs(["Fella Trends", "Lyric Sentiments"])

with t1:
    st.subheader("Fella Trends")
    plot_trend_data()
with t2:
    st.info("Pleasue use short lyric texts.")
    lyrics = lyrics()
    st.subheader("Lyric Sentiments")
    try:
        st.write(lyrical_sentiment(lyrics)[0]['label'])
    except Exception as e:
        st.warning("Text too large")

