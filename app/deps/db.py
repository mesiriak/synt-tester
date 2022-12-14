from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import create_engine
from ..config import get_settings

settings = get_settings()

DBase = declarative_base()

engine = create_engine(settings.DB_URL, echo=True, future=False)
Session = sessionmaker(engine, expire_on_commit=False)


def init_db():
    DBase.metadata.create_all(engine)


def get_session():
    with Session() as session:
        return session

