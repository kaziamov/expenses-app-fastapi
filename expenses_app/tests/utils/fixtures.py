import pytest

from expenses_app.models import BaseSQLModel

TestSession =

@pytest.fixture()
def clear_database():
    BaseSQLModel.metadata.create_all()
    yield
    BaseSQLModel.metadata.drop_all()
