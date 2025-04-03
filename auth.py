import hashlib
from database import User, Session, select

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str) -> str:
    with Session(engine) as session:
        hashed_password = hash_password(password)
        user = User(username=username, password=hashed_password)
        session.add(user)
        session.commit()
        return user.id

def login_user(username: str, password: str) -> str | None:
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()
        if user and user.password == hash_password(password):
            return user.id
        return None