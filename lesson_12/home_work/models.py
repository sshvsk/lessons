
from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    purchases = relationship("Purchases", back_populates="user", uselist=False)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    purchases = relationship("Purchase", back_populates="product")


class Purchase(Base):
    __tablename__ = "purchase"

    user_id = Column(ForeignKey("user.id"), primary_key=True)
    product_id = Column(ForeignKey("product.id"), primary_key=True)
    count = Column(Integer)

    user = relationship("User", back_populates="purchases")
    product = relationship("Product", back_populates="purchases")