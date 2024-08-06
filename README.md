# CSV File Analysis and Question Answering Application

## Objective

The project's primary aim is to create an interactive application that performs CSV file statistical analysis, generates various types of plots, and answers user questions by employing a Large Language Model (LLM).

## Technologies Used

- **Python**: The primary programming language for the entire project.
- **Pandas**: Used for data manipulation and analysis.
- **Matplotlib**: Generates various plots.
- **Streamlit**: Utilized for building an interactive web application.
- **Transformers**: For integrating LLM model that answers questions (Google’s Flan-T5).

## Architecture

The project follows several modules which include:

- **Main Application (`app.py`)**: Coordinates with other functions including user interaction.
- **Data Processing Module (`utils/data_processing.py`)**: Focuses on reading and parsing CSV files.
- **Statistical Analysis Module (`utils/statistical_analysis.py`)**: Performs simple statistical calculations.
- **Plotting Module (`utils/plotting.py`)**: Creates and displays various plots.
- **LLM Interaction Module (`utils/llm_interaction.py`)**: Interacts with the LLM model to answer user questions.

## Methodology

### 1. Reading CSV Files

- The application allows users to upload CSV files. The `read_csv` function in the `utils/read_csv.py` module reads and parses the file using pandas.

### 2. Statistical Analysis

- Fundamental statistics are calculated via the `basic_statistics` feature of the application. Mean, median, mode, standard deviation, and correlation are the primary metrics.

### 3. Plot Generation

- Users can create different types of plots such as histograms, scatter matrices, line plots, and box plots using the `generate_plots` function. The Matplotlib library is employed to generate these plots, which are displayed in the Streamlit app.

### 4. Question Answering

- The application uses an LLM model to answer questions about the data. The `ask_llama2` function takes user questions and context (statistical summaries) to generate answers using the `transformers` library.

## Challenges and Solutions

- **Handling Large Files**: Efficient data handling methods were applied to manage sizable CSV files without compromising performance.
- **Improved Plotting**: Plot generation functions have been enhanced to offer more interactivity and customization to users.

## Future Enhancements

- **More Plot Types**: Incorporating additional plot types and providing further customization.
- **Advanced Statistics**: Implementing advanced statistical techniques.
- **Performance Optimization**: Improving the efficiency of the application to handle larger datasets and more complex queries.
