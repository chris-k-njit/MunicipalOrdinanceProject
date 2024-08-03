# app/data_processing.py
import pandas as pd

def load_data(file_path, file_type):
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'excel':
        return pd.read_excel(file_path)
    elif file_type == 'json':
        return pd.read_json(file_path)
    elif file_type == 'parquet':
        return pd.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file type")
    
def get_summary_statistics(df):
    return df.describe()

def search_ordinances(df, query):
    results = df[df['ordinance_text'].str.contains(query, case=False, na=False)]
    return results
