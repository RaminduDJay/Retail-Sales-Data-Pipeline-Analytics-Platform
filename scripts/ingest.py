import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read env variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
CSV_PATH = os.path.join("data", "sales_data.csv")

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sales_raw (
                date DATE,
                store_id INTEGER,
                product_id INTEGER,
                product_name TEXT,
                category TEXT,
                region TEXT,
                quantity_sold INTEGER,
                unit_price NUMERIC,
                total_sales NUMERIC
            );
        """)
        conn.commit()
        print("Table 'sales_raw' ensured.")

def insert_data(conn, df):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO sales_raw (
                    date, store_id, product_id, product_name, category, region,
                    quantity_sold, unit_price, total_sales
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))
        conn.commit()
        print(f"Inserted {len(df)} rows.")

def main():
    print("Starting ingestion...")
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded {len(df)} rows from CSV.")

    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )

    create_table(conn)
    insert_data(conn, df)

    conn.close()
    print("Ingestion complete!")

if __name__ == "__main__":
    main()
