from sqlalchemy import Column, Integer, String

from users_edit_api.database import BaseDBModel


class User(BaseDBModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    group = Column(String(64))
    password = Column(String(128))
