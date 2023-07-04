import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def load_csv(filename = './data/geoMap.csv'):
    return pd.read_csv(filename)

csv = load_csv()

def plot_trend_data(csv = csv):
    states = csv.State
    values = csv.Search

    fig, ax = plt.subplots()
    ax.bar(states, values)
    ax.set_xlabel("State")
    ax.set_ylabel("Search Volume")
    plt.xticks(rotation = 'vertical')
    ax.set_title("Fela Kuti Google Search Trend")
    st.pyplot(fig)
    st.write(csv)
    st.line_chart(csv.Search.head(23))


