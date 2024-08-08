import pandas as pd
import json
from sensor.config import mongo_client  # Ensure mongo_client is correctly initialized

def dump_csv_file_to_mongodb_collection(file_path: str, database_name: str, collection_name: str) -> None:
    try:
        # Read CSV file into pandas DataFrame
        df = pd.read_csv(file_path)
        df.reset_index(drop=True, inplace=True)
        
        # Convert DataFrame to list of dictionaries
        json_records = df.to_dict(orient='records')
        
        # Insert the records into the MongoDB collection
        mongo_client[database_name][collection_name].insert_many(json_records)
        print("Data inserted successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
