import sqlite3
import pandas as pd

# Create database
conn = sqlite3.connect("ecommerce.db")

# Load dataset
df = pd.read_csv("../data/processed/ecommerce_master_dataset.csv")

# Store into SQLite
df.to_sql(
    "ecommerce",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

conn.close()