import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('FinalDB.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query to select the top 5 rows from the specified table
cursor.execute("SELECT * FROM ChicagoCrimeData LIMIT 5")

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Print the results
print("Top 5 rows from the 'ChicagoCrimeData' table:")
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
