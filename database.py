from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

# Koneksi ke database SQLite
engine = create_engine("sqlite:///app.db", echo=True)

# Base class untuk model
Base = declarative_base()

# Factory untuk membuat sesi database
Session = sessionmaker(bind=engine)

# Model User
class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Model Config
class Config(Base):
    __tablename__ = "configs"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    criteria = Column(String, nullable=False)

# Membuat tabel di database jika belum ada
Base.metadata.create_all(engine)

# Ekspor komponen untuk digunakan di modul lain
__all__ = ["User", "Config", "Session", "engine", "select"]

from sqlalchemy import select