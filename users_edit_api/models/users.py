from sqlalchemy import Column, Integer, String

from users_edit_api.database import BaseDBModel


class User(BaseDBModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=True)
    group = Column(String(64), nullable=False)
    password = Column(String(128), nullable=False)
