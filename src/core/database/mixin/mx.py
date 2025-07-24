"""
Module containing mixins for SQLAlchemy ORM models.

These mixins are designed to extend database models with common fields and behaviors.
"""

# SQLAlchemy imports for asynchronous DATABASE work
from sqlalchemy.orm import Mapped, mapped_column


class IdIntPkMixin:
    """Mixin with the 'id' field as an integer primary key."""

    id: Mapped[int] = mapped_column(primary_key=True)
