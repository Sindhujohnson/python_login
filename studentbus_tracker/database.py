import sqlite3
import os

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

# Connect to database
conn = sqlite3.connect("database/tracker.db")

# Create cursor
cursor = conn.cursor()

# Create institute table
cursor.execute("""
CREATE TABLE IF NOT EXISTS institute(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    institute_name TEXT,
    email TEXT,
    password TEXT
)
""")

# Save and close
conn.commit()
conn.close()

print("Database and Institute table created successfully!")