from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase, relationship


class BaseSQLModel(DeclarativeBase):
    id = Column(Integer, unique=True, primary_key=True)
    updated_at = Column(Integer)
    created_at = Column(Integer)


class Group(BaseSQLModel):
    __tablename__ = 'groups'

    name = Column(String, unique=True)
    categories = relationship('Category', back_populates='group')


class Category(BaseSQLModel):
    __tablename__ = 'categories'

    name = Column(String, unique=True)
    group_id = Column(ForeignKey('groups.id'))
    group = relationship('Group', back_populates='categories')


class Currency(BaseSQLModel):
    __tablename__ = 'currencies'

    name = Column(String, unique=True)
    code = Column(String, unique=True)
    accounts = relationship('Account', back_populates='currency')


class Account(BaseSQLModel):
    __tablename__ = 'accounts'

    name = Column(String, unique=True)
    currency_id = Column(ForeignKey('currencies.id'))
    currency = relationship('Currency', back_populates='accounts')


class Expense(BaseSQLModel):
    """Expenses model"""
    __tablename__ = 'expenses'

    description = Column(String)
    category_id = Column(ForeignKey('categories.id'), nullable=True)
    account_id = Column(ForeignKey('accounts.id'), nullable=True)
    amount = Column(Integer)
    currency_id = Column(ForeignKey('currencies.id'), nullable=True)
    date = Column(Date, nullable=True)

    category = relationship('Category', backref='expenses')
    account = relationship('Account', backref='expenses')
    currency = relationship('Currency', backref='expenses')


class Obj:

    def __init__(self, model):
        self._model = model

    def create(self):
        pass


    def update(self):
        pass

    def create_or_update(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass

    def get_all(self):
        pass

    def get_or_create(self):
        pass
