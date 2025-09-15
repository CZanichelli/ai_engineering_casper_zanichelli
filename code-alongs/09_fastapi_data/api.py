from fastapi import FastAPI
from data_processing import DataExplorer


data_explorer = DataExplorer()

app = FastAPI()

@app.get("/api/sales")
async def read_sales():
    # Implement this code to return json data in this endpoint
    return data_explorer.json_response()

@app.get("/api/sales/summary")
async def read_summary_data():
    # show summary statistics of the data
    return data_explorer.summary().json_response()

@app.get("/api/sales/kpis")
async def read_kpis(country: str):
    # KPIs based on country
    return data_explorer.kpis(country=country) 