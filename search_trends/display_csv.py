import streamlit as st
import pandas as pd


def load_csv(filename = './data/geoMap.csv'):
    return pd.read_csv(filename)

csv = load_csv()

def show_csv(csv = csv):
    st.write(csv)
    st.line_chart(csv.Search.head(5))


