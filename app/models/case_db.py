from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Case(Base):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(100))
    error_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    description: Mapped[str] = mapped_column(Text)
