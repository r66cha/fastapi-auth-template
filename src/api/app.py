"""FastAPI application instance."""

# -- Imports

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.middleware import CustomHeaderMiddleware
from .routers._0_main_router import main_router
from .description_app import title, description, version, contact

# --

# Application instance
app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
)

# Routers
app.include_router(main_router)

# Middlewares
app.add_middleware(
    middleware_class=CustomHeaderMiddleware,
)
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],  # Allow all origins — can be customized for production
)
