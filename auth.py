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

def hash_password(password: str) -> str:
    # Contoh fungsi untuk hashing password (sesuaikan dengan kebutuhan Anda)
    return password  # Ganti dengan algoritma hashing seperti bcrypt jika diperlukan

def register_user(username: str, password: str) -> str:
    """
    Mendaftarkan pengguna baru dengan username dan password.
    Mengembalikan ID pengguna yang baru dibuat.
    """
    with Session(engine) as session:
        # Hash password
        hashed_password = hash_password(password)
        # Buat pengguna baru
        new_user = User(username=username, password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user.id

def login_user(username: str, password: str):
    # Fungsi ini mungkin sudah ada di auth.py, pastikan tetap ada
    pass