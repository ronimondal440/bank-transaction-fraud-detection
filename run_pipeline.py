from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    print("[START] Bank Transaction Fraud Detection Pipeline")

    # Step 1: Extract
    df = extract_data()

    # Step 2: Transform
    transformed_df = transform_data(df)

    # Step 3: Load
    load_data(transformed_df)

    print("[END] Pipeline Execution Complete")

if __name__ == "__main__":
    main()
