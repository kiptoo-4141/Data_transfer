# Supermarket Sales Data Importer

This Python script allows users to upload an Excel or CSV file containing supermarket sales data and insert it into a MySQL database.

## Features
- **File Selection Dialog**: Users can select an Excel (`.xlsx`, `.xls`) or CSV (`.csv`) file dynamically.
- **Automated Data Import**: The script automatically reads the selected file and inserts the data into a MySQL table.
- **Error Handling**: Provides feedback if an error occurs during file selection or database insertion.

## Prerequisites
Before running this script, ensure you have the following installed:

- **Python 3.7+**
- **MySQL Database**
- **Required Python Libraries**
  - `pandas`
  - `sqlalchemy`
  - `mysql-connector-python`
  - `tkinter`
  - `openpyxl` (for Excel file support)

You can install the necessary packages using:
```sh
pip install pandas sqlalchemy openpyxl mysql-connector-python
