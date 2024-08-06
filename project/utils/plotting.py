import pandas as pd #for data manipulation
import matplotlib.pyplot as plt #plot the data in proper statistics visualization
import streamlit as st # for GUI
#pass data(DatFrame) and plot_type as argument and it will generate the plot as argument
def generate_plots(data, plot_type):
    
    fig, ax = plt.subplots()#used for subplot of the dataset
    if plot_type.lower() == 'histogram': # if ture it will plot histogram
        data.hist(ax=ax)
        ax.set_title("Histogram")
    elif plot_type.lower() == 'scatter matrix': # if ture it will plot scatter matrix
        pd.plotting.scatter_matrix(data, ax=ax)
        plt.suptitle("Scatter Matrix")
    elif plot_type.lower() == 'line plot':# if true it will plot line plot
        data.plot(ax=ax)
        ax.set_title("Line Plot")
    elif plot_type.lower() == 'box plot': #it use for check the outliers in the dataset
        data.plot(kind='box', ax=ax)
        ax.set_title("Box Plot")
    else:
        st.error(f"Plot type '{plot_type}' is not recognized. Please specify 'histogram', 'scatter matrix', 'line plot', or 'box plot'.")
        return
    plt.tight_layout() #automatically adjust subplot 
    st.pyplot(fig)
