from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data"

DATA_PATH.mkdir(exist_ok=True)

def query_duckdb(sql_code, parameters= None):
    with duckdb.connect(DATA_PATH / "restaurants.db") as conn:

        cursor = conn.execute(sql_code, parameters)

        sql_code = sql_code.strip().casefold()
        if sql_code.startswith(("select", "from", "desc", "pramga")):
            return cursor.df

def save_restaurants_to_db(restaurant_list):
    for res in restaurant_list:
        query_duckdb(
            """
            INSERT INTO resturants (name, type_of_food, price_level, rating, short_description, opening_hours, location)
            VALUES(?,?,?,?,?,?,?)
            """,

            (res.name, res.type_of_food, res.price_level, res.rating, res.short_description, res.opening_hours, res.location)
        )

    print (f"Saved {len(restaurant_list)} restaurants in database")