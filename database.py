from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Membuat engine untuk koneksi ke database SQLite
engine = create_engine("sqlite:///app.db", echo=True)

# Membuat base class untuk model
Base = declarative_base()

# Membuat session factory
Session = sessionmaker(bind=engine)

# Definisi model User
class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Membuat tabel di database jika belum ada
Base.metadata.create_all(engine)

# Mengekspor komponen yang akan digunakan di modul lain
__all__ = ["User", "Session", "engine", "select"]

# Jika Anda menggunakan SQLAlchemy 2.0+, Anda juga perlu mengimpor select
from sqlalchemy import select