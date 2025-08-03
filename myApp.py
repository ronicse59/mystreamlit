! pip install seaborn
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import time

# App title
st.title("Linear Regression Training Animation")
st.subheader("Data Science with Dr. MS Rahman")

# Sidebar
st.sidebar.header("Upload CSV Data or Use Sample")
use_example = st.sidebar.checkbox("Use example dataset")

# Load Data
if use_example:
    df = sns.load_dataset('tips')
    df = df.dropna()
    st.success("Loaded sample dataset: 'tips'")
else:
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=['csv'])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.warning("Please upload a CSV file or use the example dataset")
        st.stop()


# Show Dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Data Preprocessing
st.subheader("Data Preprocessing")
