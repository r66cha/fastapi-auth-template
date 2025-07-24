from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.middleware import CustomHeaderMiddleware
from .routers._0_main_router import main_router
from .description_app import title, description, version, contact


app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
)

app.include_router(main_router)

app.add_middleware(
    middleware_class=CustomHeaderMiddleware,
)
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
)
