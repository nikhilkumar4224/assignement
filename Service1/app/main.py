from fastapi import FastAPI
from app.api.city_name_to_zipcode import city
from app.api.db import metadata,  engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/city_name/openapi.json", docs_url="/api/v1/city_name/docs")


app.include_router(city, prefix='/api/v1/', tags=['city routers'])