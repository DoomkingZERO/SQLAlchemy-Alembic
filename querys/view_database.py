from sqlalchemy import create_engine, inspect

engine = create_engine('sqlite:///demo.db')
inspector = inspect(engine)

# Get a list of table names
tables = inspector.get_table_names()
print("Tables in the database:")
for table in tables:
    print(table)

# Get table metadata
for table_name in tables:
    print(f"\nTable: {table_name}")
    table = inspector.get_table(table_name)
    print(f"Columns: {', '.join(column.name for column in table.columns)}")

    # Print a few sample rows (if any)
    with engine.connect() as conn:
        rows = conn.execute(f"SELECT * FROM {table_name} LIMIT 3").fetchall()
        print(f"Sample rows:")
        for row in rows:
            print(row)
