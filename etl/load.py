import pandas as pd
import os

def load_data(df, output_path="data/processed_transactions.csv"):
    if df.empty:
        print("[WARNING] Empty DataFrame received. Skipping loading.")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Data successfully saved to {output_path}")
