import pandas as pd

def extract_data(file_path="data/transactions.csv"):
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully loaded {len(df)} records.")
        return df
    except FileNotFoundError:
        print("[ERROR] Data file not found.")
        return pd.DataFrame()
