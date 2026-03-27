## Here is my data cleaning code:
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import time
import os

# 1. Connection Setup
raw_password = "ADITYA04@Nn"
safe_password = urllib.parse.quote_plus(raw_password)
engine = create_engine(f"mysql+pymysql://root:{safe_password}@localhost/AIIMS_Health_Analytics")

print("🚀 Step 1: Loading 30 Lakh Rows from SQL...")
start_time = time.time()

# 2. Data ko direct uthana (No chunks needed for CSV save)
df = pd.read_sql('SELECT * FROM View_AIIMS_Master', engine)

print(f" Data Loaded. Total rows: {len(df)}")

# 3. Quick Cleaning
print(" Cleaning Data...")
df['Gender'] = df['Gender'].astype(str).str.upper()
df['City'] = df['City'].fillna('UNKNOWN').astype(str).str.upper()
df['Visit_Date'] = pd.to_datetime(df['Visit_Date'], errors='coerce')

# 4. Saving to CSV (This is the Magic Step!)
file_path = os.path.join(os.path.expanduser("~"), "Downloads", "Cleaned_AIIMS_Data.csv")
print(f"Saving to CSV at: {file_path}")

df.to_csv(file_path, index=False)

print(f"SUCCESS! Total {len(df)} rows saved in {round(time.time() - start_time, 2)}s")