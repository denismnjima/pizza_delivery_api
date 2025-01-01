from database import Base
from sqlalchemy import Column,Integer,String,Text,Boolean,ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    username = Column(String(50),unique=True)
    email = Column(String(50),unique=True)
    password = Column(Text)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'


class Order(Base):

    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    )
    PIZZA_SIZE = (
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE', "large")
    )
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer,nullable=True)
    order_status = Column(ChoiceType(choices= ORDER_STATUS), default='PENDING')
    pizza_size = Column(ChoiceType(choices = PIZZA_SIZE))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')