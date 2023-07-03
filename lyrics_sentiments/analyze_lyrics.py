import streamlit as st
from transformers import pipeline
from lyrics_sentiments.get_lyrics import lyrics


def lyrical_sentiment(lyrics):
    classifier = pipeline("sentiment-analysis")
    return classifier(lyrics)