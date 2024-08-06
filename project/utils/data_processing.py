import pandas as pd # for data load /data manipulation
import streamlit as st # for creating the gui
#pass the path of dataset  and it  return you DataFrame
def read_csv(file):
    try:
        data = pd.read_csv(file)
        return data
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        return None
