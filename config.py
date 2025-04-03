from database import Config, Session, select

def save_criteria(user_id: str, criteria: str):
    with Session(engine) as session:
        config = Config(user_id=user_id, criteria=criteria)
        session.add(config)
        session.commit()

def get_latest_criteria(user_id: str) -> str | None:
    with Session(engine) as session:
        statement = select(Config).where(Config.user_id == user_id).order_by(Config.id.desc()).limit(1)
        result = session.exec(statement).first()
        return result.criteria if result else None