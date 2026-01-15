from pydantic import BaseModel, Field
from typing import List


class Restaurant(BaseModel):
    name: str
    type_of_food: str
    price_level: str
    rating: int = Field(gt=0, lt=6)
    short_description: str
    opening_hours: str
    location: str

class RestaurantList(BaseModel):
    restaurants: List[Restaurant]


class RestaurantSearch(BaseModel):
    location: str
    cuisine: str