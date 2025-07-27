"""Logging setup module."""

# -- Imports

import logging
from src.core.config import settings


# --


logging.basicConfig(
    format=settings.logging.log_format,
    level=settings.logging.log_level_value,
)
log = logging.getLogger(__name__)

__all__ = ["log"]
