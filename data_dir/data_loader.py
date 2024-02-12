# Data loader

# load data from sql database

import os
import sqlite3
import pandas as pd


# create a database named "data.db" and insert data into it.
# I have a file data_setup.sql which contains the queries to insert data.
def create_database():
    conn = sqlite3.connect("./data_dir/data.db")

    # SQL commands to create tables if they do not exist
    create_tables_sql = """
    CREATE TABLE IF NOT EXISTS source_category (
        source_category_id INTEGER PRIMARY KEY,
        category_name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS functional_category (
        functional_category_id INTEGER PRIMARY KEY,
        functional_category_name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS sources (
        source_id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_name TEXT NOT NULL,
        source_url TEXT NOT NULL,
        source_category_id INTEGER NOT NULL,
        functional_category_id INTEGER NOT NULL,
        class_name TEXT NOT NULL,
        checkcolumn TEXT NOT NULL,
        FOREIGN KEY (source_category_id) REFERENCES source_category (source_category_id),
        FOREIGN KEY (functional_category_id) REFERENCES functional_category (functional_category_id)
    );
    """
    cursor = conn.cursor()

    # Execute the SQL commands to create tables
    conn.executescript(create_tables_sql)
    conn.commit()

    # Insert data into the tables
    with open("./data_dir/data_setup.sql", "r") as file:
        cursor.executescript(file.read())
    conn.commit()
    return conn


# load data from the database
def read_data_to_dataframe(table_name, conn):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    return df


# main function
def main():
    # call create_database function to create a database and insert data into it if data.db does not exist
    if not os.path.exists("./data_dir/data.db"):
        conn = create_database()
    else:
        conn = sqlite3.connect("./data_dir/data.db")
    # read data from the table "sources"
    sources_df = read_data_to_dataframe("sources", conn)
    print(f"Data from the table 'sources':")
    print(sources_df.head())

    # read data from the table "source_category"
    source_category_df = read_data_to_dataframe("source_category", conn)
    print(f"Data from the table 'source_category':")
    print(source_category_df.head())

    # read data from the table "functional_category"
    functional_category_df = read_data_to_dataframe("functional_category", conn)
    print(f"Data from the table 'functional_category':")
    print(functional_category_df.head())


if __name__ == "__main__":
    main()
