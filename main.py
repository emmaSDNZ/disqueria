from fastapi import FastAPI
from routers.album_route import album

app = FastAPI()

app.include_router(album)