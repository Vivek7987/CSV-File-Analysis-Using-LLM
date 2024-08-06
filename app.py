'''Here imported all the required python file '''

import pandas as pd  # it is use for data manipulations
import streamlit as st # for creating the GuI 
from utils.data_processing import read_csv # imported from utils.data_processing to read the csv file
from utils.statistical_analysis import basic_statistics 
from utils.plotting import generate_plots 
from utils.llm_interaction import ask_llama2

# Streamlit app layout
st.title("The CSV file  Analysis and Question & Answering(Using  Prompt)")

uploaded_csv_file = st.file_uploader("Choose a CSV file from your Device", type="csv")

if uploaded_csv_file:
    csvData = read_csv(uploaded_csv_file)
    
    if csvData is not None:
        st.title("Basic Statistics of Dataset:")
        stats = basic_statistics(csvData)
        for key, value in stats.items():
            st.write(f"**{key.capitalize()} Statistics:**")
            for stat_key, stat_value in value.items():
                st.write(f"{stat_key.capitalize()}: {stat_value}")
        
        st.title("Data Visualizations ")
        plot_type = st.selectbox("Select ploting type:", ['Histogram', 'Scatter Matrix', 'Line Plot', 'Box Plot'])
        if st.button("Now Generate Plot"):
            generate_plots(csvData, plot_type)
        st.title("Prompt ")
        query = st.text_input("Enter your query about the data:")
        if query:
            context = csvData.describe().to_dict()
            answer = ask_llama2(query, context)
            st.write(f"**Answer:** {answer}")
            
            # Check if the question asks for a specific plot
            plot_keywords = ["histogram", "scatter matrix", "line plot", "box plot"]
            for keyword in plot_keywords:
                if keyword in query.lower():
                    st.write(f"Generating {keyword} as requested:")
                    generate_plots(csvData, keyword)
                    break
