from sqlmodel import create_engine, SQLModel, Session
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()


# database_url = "mysql+pymysql://root:password@localhost:3306/fastapidb"
engine_url = create_engine(settings.DATABASE_URL, echo=True)

def conn():
    # SQLModel을 상속받은 모든 클래스를 기반으로 데이터베이스에 테이블을 생성 
    SQLModel.metadata.create_all(engine_url)


def get_session():
    # Session => 데이터베이스와 상호작용(CRUD)을 관리하는 객체
    with Session(engine_url) as session:
        yield session

