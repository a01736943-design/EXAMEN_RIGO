import streamlit as st
import pandas as pd

@st.cache_resource
def load_all_data():
    df = pd.read_csv('data/exam_data.csv')
    return (
    df)
