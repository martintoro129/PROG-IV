# applogin/models.py
import reflex as rx
from typing import Optional
from sqlmodel import Field, Column, TEXT

class User(rx.Model, table=True):
    # MySQL necesita max_length para crear el índice UNIQUE
    username: str = Field(unique=True, max_length=50)
    password: str = Field(max_length=255)
    email: str = Field(unique=True, max_length=150)
    role: str = Field(default="Guest", max_length=20)
    is_admin: bool = Field(default=False)
