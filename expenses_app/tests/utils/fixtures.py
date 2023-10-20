import pytest

from expenses_app.models import BaseBDModel

TestSession =

@pytest.fixture()
def clear_database():
    BaseBDModel.metadata.create_all()
    yield
    BaseBDModel.metadata.drop_all()
