import hashlib
from database import User, Session, select, engine  # Mengimpor engine dari database.py

# Fungsi untuk hashing kata sandi
def hash_password(password: str) -> str:
    """Mengubah kata sandi menjadi hash SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Fungsi untuk login pengguna
def login_user(username: str, password: str) -> str | None:
    """
    Memverifikasi kredensial pengguna dan mengembalikan ID pengguna jika valid.
    Mengembalikan None jika login gagal.
    """
    with Session(engine) as session:  # Menggunakan engine yang diimpor
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()
        if user and user.password == hash_password(password):
            return user.id
        return None