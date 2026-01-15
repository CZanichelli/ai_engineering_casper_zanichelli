from utils import query_duckdb

query_duckdb("""
    CREATE TABLE IF NOT EXISTS restaurants(
             name TEXT,
             type_of_food TEXT,
             price_level TEXT,
             rating INTEGER,
             short_description TEXT,
             opening_hours TEXT,
             location TEXT
    );
""")