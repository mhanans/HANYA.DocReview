from sqlmodel import Field, SQLModel, create_engine, Session, select
import uuid

engine = create_engine("sqlite:///app.db")

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex, primary_key=True)
    username: str = Field(unique=True)
    password: str  # Hashed password

class Config(SQLModel, table=True):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex, primary_key=True)
    user_id: str = Field(foreign_key="user.id")
    criteria: str = Field(default="")

SQLModel.metadata.create_all(engine)