from fastapi import APIRouter

city = APIRouter()

@city.get("/zipcode-to-city/{zip_code}")
async def zipcode_to_city(zip_code: str):
    # sample zip code 
    city_name = "sample city"
    return {"city_name": city_name, "zip_code": zip_code}
