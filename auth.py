import hashlib
from database import User, Session, select

def hash_password(password: str) -> str:
    """Mengubah kata sandi menjadi hash SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str) -> str:
    """Mendaftarkan pengguna baru dan mengembalikan ID pengguna."""
    with Session() as session:
        hashed_password = hash_password(password)
        new_user = User(username=username, password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user.id

def login_user(username: str, password: str) -> str | None:
    """Memverifikasi kredensial pengguna dan mengembalikan ID jika valid."""
    with Session() as session:
        statement = select(User).where(User.username == username)
        user = session.execute(statement).scalars().first()
        if user and user.password == hash_password(password):
            return user.id
        return None