import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from tkinter import Tk, filedialog

# Open a file dialog to select the file
root = Tk()
root.withdraw()  # Hide the root window
file_path = filedialog.askopenfilename(title="Select Excel or CSV File", filetypes=[("Excel Files", "*.xlsx;*.xls"), ("CSV Files", "*.csv")])

if not file_path:
    print("No file selected. Exiting...")
    exit()

# Load the selected file
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

# Database connection details
DB_USER = "root"  # Change if necessary
DB_PASSWORD = ""  # Change to your actual password
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "supermarket_db"

# Create SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Define table name
table_name = "supermarket_sales"

# Insert data into SQL table
try:
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print("Data successfully inserted into the database!")
except Exception as e:
    print(f"Error inserting data: {e}")
