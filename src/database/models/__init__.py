from sqlalchemy import String, Integer, Column, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.database.db import Base
import uuid
from datetime import datetime
from src.utils import format_datetime
from passlib.hash import sha256_crypt as hasher


def hex_id():
    return str(uuid.uuid4().hex)


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=hex_id)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __init__(self, password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = kwargs.get("username").lower()
        self.password = hasher.hash(password)

    # verify password
    def verify_password(self, password):
        return hasher.verify(password, self.password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": format_datetime(self.created_at),
        }
