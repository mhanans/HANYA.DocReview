from database import Config, Session, select

def save_criteria(user_id: str, criteria: str):
    """Menyimpan kriteria review untuk pengguna tertentu."""
    with Session() as session:
        new_config = Config(user_id=user_id, criteria=criteria)
        session.add(new_config)
        session.commit()

def get_latest_criteria(user_id: str) -> str | None:
    """Mengambil kriteria review terbaru berdasarkan user_id."""
    with Session() as session:
        statement = select(Config).where(Config.user_id == user_id).order_by(Config.id.desc()).limit(1)
        result = session.execute(statement).scalars().first()
        return result.criteria if result else None