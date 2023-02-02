from fastapi import FastAPI
from Service2.app.api.zipcode_to_city_name import city
from app.api.db import metadata,  engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/city/openapi.json", docs_url="/api/v1/city/docs")


app.include_router(city, prefix='/api/v1/', tags=['city routers'])