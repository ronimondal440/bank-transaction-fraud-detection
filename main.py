from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    print("[INFO] Starting ETL pipeline...")

    df = extract_data()

    if df.empty:
        print("[ERROR] No data extracted. Pipeline aborted.")
        return

    transformed_df = transform_data(df)

    load_data(transformed_df)

    print("[INFO] ETL pipeline completed.")

if __name__ == "__main__":
    run_pipeline()
