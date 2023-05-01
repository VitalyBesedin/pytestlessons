import pytest

@pytest.fixture()
def set_up():
    print("Login completed")


def test_sending_mail_1(set_up):
    print("Mail sent")

def test_sending_mail_2(set_up):
    print("Mail sent")
#test_sending_mail_2()
