from fastapi import APIRouter

city = APIRouter()

@city.get("/city-to-zipcode/{city_name}")
async def city_to_zipcode(city_name: str):
    # sample zip code 
    zip_code = "12345"
    return {"city_name": city_name, "zip_code": zip_code}
