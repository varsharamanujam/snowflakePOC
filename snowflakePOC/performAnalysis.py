import pandas as pd
import json
import os
from snowflake.connector import connect
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import logging 
import argparse

def main():
    # Setup logging
    logging.basicConfig(filename='analysis.log', level=logging.INFO)
    logging.info('Starting analysis...')

    # Connection setup with error handling
    try:
        parser = argparse.ArgumentParser(description='Perform analysis.')
        parser.add_argument('config_path', type=str, help='Path to the config.json file')
        args = parser.parse_args()

        # Read the config.json file
        with open(args.config_path, 'r') as file:
            config = json.load(file)
        conn = connect(
            user=config['user'],
            password=config['password'],
            account=config['account'],
        )

        conn.cursor().execute(f"USE WAREHOUSE {config['warehouse']}")
        conn.cursor().execute(f"USE DATABASE {config['database']}")
        conn.cursor().execute(f"USE SCHEMA {config['schema']}")

        # Define the SQL query to fetch the data from the table
        query = "SELECT * FROM " + config['testtable']

        # Execute the query and load the result into a DataFrame
        df = pd.read_sql(query, conn)

        # Close the connection
        conn.close()

        # Print the first 5 rows
        print(df.head())


        # 2. Perform Analyses

        # 2.1 Descriptive Statistics
        summary = df.describe()
        print(summary)

        # 2.2 Correlation Analysis
        correlation_matrix = df.corr()
        print(correlation_matrix)

        # 2.3 Clustering and Segmentation

        # Assuming you want to cluster into 3 groups
        kmeans = KMeans(n_clusters=3)
        df['cluster'] = kmeans.fit_predict(df[['MANUFACTURER', 'SALESINDEX', 'RRP']])
        df[['MANUFACTURER', 'SALESINDEX', 'RRP']].head()

        # 2.4 Visualization

        # Histogram for the Recommended Retail Price (rrp)
        plt.hist(df['RRP'], bins=20)
        plt.title('Distribution of Recommended Retail Prices')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()

        # 3. Potential predictive modeling scenario (example)

        # 3.1 Predicting Recommended Retail Price (RRP)

        # Selecting Features and Target
        X = df[['MANUFACTURER', 'GENERICPRODUCT', 'SALESINDEX', 'CATEGORY']].fillna(0) # Example features
        y = df['RRP']

        # Splitting data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Creating the model
        model = LinearRegression()

        # Training the model
        model.fit(X_train, y_train)

        # Making predictions on the test set
        predictions = model.predict(X_test)

        # Evaluating the model using R^2 score and Mean Absolute Error
        r2 = r2_score(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)

        print(r2, mae)

    except Exception as e:
        logging.error(f'Error occurred: {e}')
        exit()

if __name__ == "__main__":
   main()