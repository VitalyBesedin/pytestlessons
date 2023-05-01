import pytest

@pytest.fixture()
def set_up():
    print("Login completed")


def test_sending_mail_1():
    print("Mail sent")

def test_sending_mail_2():
    print("Mail sent")

