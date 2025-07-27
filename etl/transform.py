import pandas as pd

def transform_data(df):
    if df.empty:
        print("[WARNING] Empty DataFrame received. Skipping transformation.")
        return df

    # Example transformation: Create a 'is_fraud' column based on rules
    df['is_fraud'] = df['amount'].apply(lambda x: 1 if x > 10000 else 0)

    print(f"[INFO] Flagged {df['is_fraud'].sum()} suspicious transactions.")
    return df
