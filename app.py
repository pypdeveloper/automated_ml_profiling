import streamlit as st
import pandas as pd
import os
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report 

with st.sidebar:
    # st.image("./logo.png", width=170)
    st.title("Automated Dataset Profiling")
    choice = st.radio("Navigation", ["Upload", "Profiling"])

if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

if choice == "Upload":
    st.title("Upload your dataset")
    file = st.file_uploader("Upload your dataset here:")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Profiling")
    profile_report = df.profile_report()
    st_profile_report(profile_report)
    profile_report.to_file("Analysis.html")
    st.download_button('Download Profile', "./Analysis.html", file_name="Profile.html")