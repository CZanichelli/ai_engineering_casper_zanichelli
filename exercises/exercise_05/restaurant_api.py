from pydantic_ai import Agent
from dotenv import load_dotenv
from data_models import RestaurantList
from data_models import RestaurantSearch
from fastapi import FastAPI
from utils import save_restaurants_to_db
from utils import query_duckdb

load_dotenv()

# Create Agent
restaurant_agent = Agent(
    "google-gla:gemini-2.5-flash",
    output_type=RestaurantList,
    system_prompt="You are a helpful travel guide. Your task is to suggest exactly 5 restaurants based on the location the user enters. If you don't know of any real restaurants in the location, it's okay to come up with credible alternatives.",
)

app = FastAPI()

@app.post("/recommendations")
async def get_recommendations(search: RestaurantSearch):
    prompt = f"Find restaurants i {search.location} that serves {search.cuisine}"
    result = await restaurant_agent.run(prompt)

    save_restaurants_to_db(result.data.restaurants)

    return result.data


@app.get("/restaurants")
async def list_restaurants():
    df = query_duckdb("SELECT * FROM restaurants")

    data = df.to_dict(orient="records")

    return data