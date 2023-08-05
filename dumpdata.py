import mysql.connector
import pandas as pd
import argparse
import sys
def parse_arguments():
    parser = argparse.ArgumentParser(description='Process CSV file')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the CSV file.')
    args = parser.parse_args()
    if args.file:
        file_path = args.file
        return file_path
    else:
        print("[-] Please provide the csv file!")
        sys.exit(1)
argument = parse_arguments()
data = pd.read_csv(argument)

connection = mysql.connector.connect(
 host='localhost',
 user='root',
 password='toor',
 database='nopl'
)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS used_bikes (
 bike_name VARCHAR(255),
 price INT,
 city VARCHAR(255),
 kms_driven INT,
 owner VARCHAR(255),
 age INT,
 power INT,
 brand VARCHAR(255)
);
"""
cursor.execute(create_table_query)

insert_query = f"INSERT INTO used_bikes ({', '.join(data.columns)}) VALUES ({', '.join(['%s'] *
len(data.columns))});"

for index, row in data.iterrows():
 values = tuple(row)
 cursor.execute(insert_query, values)
  
connection.commit()
cursor.close()
connection.close()
