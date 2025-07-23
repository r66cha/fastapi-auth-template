from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.middleware import CustomHeaderMiddleware


app = FastAPI()

app.add_middleware(
    middleware_class=CustomHeaderMiddleware,
)
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origin=["*"],
)
