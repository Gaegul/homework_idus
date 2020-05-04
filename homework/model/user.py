from sqlalchemy import Column, String, Enum

from homework.model import Base


class User(Base):
    __tablename__ = 'user'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    email = Column(String(100), primary_key=True)
    password = Column(String(100), nullable=True)
    phone_number = Column(String(20), nullable=True)
    name = Column(String(20), nullable=True)
    sex = Column(Enum('male', 'female', 'not_selected'), nullable=False)
    nickname = Column(String(30), nullable=True)
    refresh_token = Column(String(100), nullable=False)

