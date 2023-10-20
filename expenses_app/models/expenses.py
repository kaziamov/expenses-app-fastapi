from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, relationship


class BaseBDModel(DeclarativeBase):
    id = Column(Integer, unique=True, primary_key=True)
    created_at = Column(Integer)
    updated_at = Column(Integer)


class Group(BaseBDModel):
    __tablename__ = 'groups'

    name = Column(String, unique=True)


class Category(BaseBDModel):
    __tablename__ = 'categories'

    name = Column(String, unique=True)
    group_id = Column(ForeignKey('groups.id'))

    group = relationship('Group', backref='categories')


class Currency(BaseBDModel):
    __tablename__ = 'currencies'

    name = Column(String, unique=True)
    code = Column(String, unique=True)


class Account(BaseBDModel):
    __tablename__ = 'accounts'

    name = Column(String, unique=True)
    currency_id = Column(ForeignKey('currencies.id'))

    currency = relationship('Currency', backref='accounts')


class Expense(BaseBDModel):
    __tablename__ = 'expenses'

    description = Column(String)
    category_id = Column(ForeignKey('categories.id'))
    account_id = Column(ForeignKey('accounts.id'))
    amount = Column(Integer)
    currency_id = Column(ForeignKey('currencies.id'))

    category = relationship('Category', backref='expenses')
    account = relationship('Account', backref='expenses')
    currency = relationship('Currency', backref='expenses')
