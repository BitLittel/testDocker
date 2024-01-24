# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, BigInteger
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs
import hashlib
import main.config as config


def hash_password(password: str) -> str:
    h = hashlib.new('sha256')
    h.update(password.encode('utf-8'))
    return h.hexdigest()


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(length=30), nullable=False)
    gender = Column(String(length=40), nullable=False)
    role = Column(String(length=20), nullable=True)

print(config.DATABASE_USER, config.DATABASE_PASSWORD, config.DATABASE_IP, config.DATABASE_PORT, config.DATABASE_NAME)
engine = create_async_engine(
        f'postgresql+asyncpg://{config.DATABASE_USER}'
        f':{config.DATABASE_PASSWORD}'
        f'@{config.DATABASE_IP}:{config.DATABASE_PORT}'
        f'/{config.DATABASE_NAME}',
        echo=False,
        pool_recycle=300,
        query_cache_size=0,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=2,
        pool_use_lifo=True
    )

Session = async_sessionmaker(engine, expire_on_commit=False)
# alembic revision --autogenerate -m "..."
# alembic upgrade head
# async def start() -> None:
#     await query_execute(query_text='CREATE EXTENSION "uuid-ossp";', fetch_all=False, type_query='insert')
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     await query_execute(
#         query_text='insert into "Images" (content_type, file_name) '
#                    'values (\'image/jpeg\', \'default_img.jpg\')',
#         fetch_all=False,
#         type_query='insert'
#     )


async def query_execute(query_text: str, fetch_all: bool = False, type_query: str = 'read'):
    async with Session() as db:
        # print(query_text, fetch_all, type_query)
        query_object = await db.execute(text(query_text))
        if type_query == 'read':
            return query_object.fetchall() if fetch_all else query_object.fetchone()
        else:
            await db.execute(text('commit'))
            return True