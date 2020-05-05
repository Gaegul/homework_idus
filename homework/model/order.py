from sqlalchemy import Column, String, DATETIME, ForeignKey

from homework.model import Base


class Order(Base):
    __tablename__ = 'order'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    order_id = Column(String(12), primary_key=True)
    product_name = Column(String(100), nullable=True)
    payment = Column(DATETIME, nullable=True)
    order_user = Column(String(100), ForeignKey("user.email"), nullable=True)
