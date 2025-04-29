from sqlalchemy import create_engine, Integer, Boolean, String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, unique=True, index=True)
    name: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True, ForeignKey="users.id")
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String, default="")
    completed: Mapped[bool] =  mapped_column(Boolean, default=False)
