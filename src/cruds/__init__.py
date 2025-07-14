from src.database.models import User
from src.database.db import async_session
from src.logger import logger
from sqlalchemy import select
from quart_jwt_extended import get_jwt_identity


async def create_user(username, password):
    async with async_session() as session:
        user = User(username=username, password=password)
        session.add(user)
        await session.commit()
        return user


# username exists
async def get_user_by_username(username):
    logger.info(f"Get user by username: {username}")
    async with async_session() as session:
        result = await session.execute(select(User).where(User.username == username))
        return result.scalars().first()


# get current user from get_jwt_identity
async def get_current_user():
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.id == get_jwt_identity())
        )
        return result.scalars().first()
