import pandas as pd
import json
import os
from snowflake.connector import connect
import logging
import argparse

def main():
  # Setup logging
  logging.basicConfig(filename='upload.log', level=logging.INFO)
  logging.info('Starting upload...')

  try:
    parser = argparse.ArgumentParser(description='Upload data to Snowflake.')
    parser.add_argument('config_path', type=str, help='Path to the config.json file')
    args = parser.parse_args()

    # Use args.config_path as the path to the config.json file
    with open(args.config_path, 'r') as file:
        config = json.load(file)

    # Define the schema, table name, and file path for a specific CSV file
    schemaName = config['schema']
    tblName = config['database']

    file_path = 'dataset/items.csv'
    df = pd.read_csv(file_path, sep="|")

    # Print the first 5 rows to understand the structure
    print(df.dtypes)

    # Connection setup with error handling
    conn = connect(
        user=config['user'],
        password=config['password'],
        account=config['account'],
    )

    # After you log in, create a database, schema, and warehouse if they don’t yet exist
    conn.cursor().execute(f"CREATE WAREHOUSE IF NOT EXISTS {config['warehouse']}")
    conn.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
    conn.cursor().execute(f"USE DATABASE {config['database']}")
    conn.cursor().execute(f"CREATE SCHEMA IF NOT EXISTS {config['schema']}")

    conn.cursor().execute(f"USE WAREHOUSE {config['warehouse']}")
    conn.cursor().execute(f"USE DATABASE {config['database']}")
    conn.cursor().execute(f"USE SCHEMA {config['schema']}")

    # Define the CREATE TABLE statement
    create_table_stmt = f"""
    CREATE TABLE IF NOT EXISTS {config['testtable']} (
        pid INT,
        manufacturer INT,
        "group" STRING,
        content STRING,
        unit STRING,
        pharmForm STRING,
        genericProduct INT,
        salesIndex INT,
        category FLOAT,
        campaignIndex STRING,
        rrp FLOAT
    );
    """

    # Execute the CREATE TABLE statement
    conn.cursor().execute(create_table_stmt)

    # Define the CREATE FILE FORMAT statement
    create_file_format_stmt = """
    CREATE OR REPLACE FILE FORMAT my_file_format
    TYPE = 'CSV'
    FIELD_DELIMITER = '|'
    SKIP_HEADER = 1;
    """

    # Execute the CREATE FILE FORMAT statement
    conn.cursor().execute(create_file_format_stmt)


    copy_into_stmt = """
    COPY INTO testtable
    FROM @%testtable
    FILE_FORMAT = my_file_format;
    """
    conn.cursor().execute(copy_into_stmt)

    # Putting Data
    conn.cursor().execute("PUT file://Dataset/items.csv @%testtable")
    conn.cursor().execute("COPY INTO testtable")

  except Exception as e:
    logging.error(f'Error occurred: {e}')
    exit()

if __name__ == "__main__":
    main()