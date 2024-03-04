from sqlalchemy import create_engine, MetaData, Table, select

# Create an engine to connect to your SQLite database
engine = create_engine('sqlite:///FinalDB.db')

# Reflect the database schema
metadata = MetaData()
metadata.reflect(bind=engine)

# Specify the table you want to query (replace 'ChicagoCrimeData' with the desired table name)
table_name = 'ChicagoCrimeData'
table = Table(table_name, metadata, autoload=True, autoload_with=engine)

# Specify the columns you want to select
columns = table.columns

# Construct a select query to get the top 5 rows from the table
query = select(columns).limit(5)

# Open a connection
with engine.connect() as connection:
    # Execute the query and fetch the results
    results = connection.execute(query).fetchall()

# Print the results
print(f"Top 5 rows from the '{table_name}' table:")
for row in results:
    print(row)
