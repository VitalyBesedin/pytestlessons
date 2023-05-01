import pytest


@pytest.fixture()
def set_up():
    print("Login completed")
    yield
    print("Sign Out")
