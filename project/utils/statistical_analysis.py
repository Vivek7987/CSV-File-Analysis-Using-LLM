import pandas as pd # for data manipulation
#pass the Dataframe as input and if column is numeric return mean,median,mode etc
def basic_statistics(data):
    
    stats = {}
    for col in data.columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            stats[col] = {
                "mean": data[col].mean(),
                "median": data[col].median(),
                "mode": data[col].mode().iloc[0], #in iloc we pass column as index not as column name
                "std_dev": data[col].std(),
                "correlation": data.corr()[col].to_dict(),
            }
    return stats
