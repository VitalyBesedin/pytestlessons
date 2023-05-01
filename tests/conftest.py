import pytest


@pytest.fixture()
def set_up():
    print("Login completed")
    yield
    print("Sign Out")

@pytest.fixture(scope="module")
def some():
    print("Start")
    yield
    print("End")