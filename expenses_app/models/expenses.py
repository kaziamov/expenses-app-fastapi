from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase, relationship


class BaseBDModel(DeclarativeBase):
    id = Column(Integer, unique=True, primary_key=True)
    updated_at = Column(Integer)
    created_at = Column(Integer)


class Group(BaseBDModel):
    __tablename__ = 'groups'

    name = Column(String, unique=True)
    categories = relationship('Category', back_populates='group')


class Category(BaseBDModel):
    __tablename__ = 'categories'

    name = Column(String, unique=True)
    group_id = Column(ForeignKey('groups.id'))
    group = relationship('Group', back_populates='categories')


class Currency(BaseBDModel):
    __tablename__ = 'currencies'

    name = Column(String, unique=True)
    code = Column(String, unique=True)
    accounts = relationship('Account', back_populates='currency')


class Account(BaseBDModel):
    __tablename__ = 'accounts'

    name = Column(String, unique=True)
    currency_id = Column(ForeignKey('currencies.id'))
    currency = relationship('Currency', back_populates='accounts')


class Expense(BaseBDModel):
    __tablename__ = 'expenses'

    description = Column(String)
    category_id = Column(ForeignKey('categories.id'))
    account_id = Column(ForeignKey('accounts.id'))
    amount = Column(Integer)
    currency_id = Column(ForeignKey('currencies.id'))
    date = Column(Date)

    category = relationship('Category', backref='expenses')
    account = relationship('Account', backref='expenses')
    currency = relationship('Currency', backref='expenses')
