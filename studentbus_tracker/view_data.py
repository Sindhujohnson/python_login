import sqlite3

# Connect to the database
conn = sqlite3.connect("database/tracker.db")

# Create a cursor
cursor = conn.cursor()

# Read all records from the institute table
cursor.execute("SELECT * FROM institute")

# Store all rows
rows = cursor.fetchall()

# Display each row
for row in rows:
    print(row)

# Close the database
conn.close() 