from starlette_admin.contrib.sqla import Admin, ModelView

from ..db import async_engine
from ..models import *


class ExtendedModelView(ModelView):
    searchable_fields = ("name", )
    page_size = 50
    page_size_options = [50, 100, 200]


    def duplicate(self, instance):
        pass


class GroupView(ModelView):
    fields = ("id", "name")


class CategoryView(ExtendedModelView):
    fields = ("id", "name", "group")


class CurrencyView(ExtendedModelView):
    fields = ("id", "code", "name")


class AccountView(ExtendedModelView):
    fields = ("id", "name", "currency")


class ExpenseView(ExtendedModelView):
    model = Expense
    fields = ("id", "date", "description", "category", "account", "amount", "currency")
    searchable_fields = ("description", )

admins_view = Admin(async_engine, title="Expenses App: Admin")

admins_view.add_view(GroupView(Group))
admins_view.add_view(CategoryView(Category))
admins_view.add_view(CurrencyView(Currency))
admins_view.add_view(AccountView(Account))
admins_view.add_view(ExpenseView(Expense))
