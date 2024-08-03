# app/data_processing.py
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def get_summary_statistics(df):
    return df.describe()

def search_ordinances(df, query):
    results = df[df['ordinance_text'].str.contains(query, case=False, na=False)]
    return results
