import pytest
from SMS import SMS
from encryption import *

@pytest.fixture
def sms_object():
    """Creates the sms object for use in tests"""
    sms = SMS()
    return sms

def test_add_user(sms_object):
    """Test for adding a new user"""
    assert "new_user" not in sms_object.users.keys()
    sms_object.add_user("new_user", "new_password")
    assert "new_user" in sms_object.users.keys()
    assert check_password("new_password", sms_object.users["new_user"])

def test_delete_user(sms_object):
    """Test for deleting a user"""
    assert "defaultadmin" in sms_object.users.keys()
    sms_object.delete_user("defaultadmin")
    assert "defaultadmin" not in sms_object.users.keys()
    assert "defaultadmin" not in sms_object.roles["admin"]

def test_assign_role(sms_object):
    assert "defaultteacher" in sms_object.roles["teacher"]
    assert "defaultteacher" not in sms_object.roles["student"]
    sms_object.assign_role("defaultteacher", "student")
    assert "defaultteacher" not in sms_object.roles["teacher"]
    assert "defaultteacher" in sms_object.roles["student"]

def test_get_users_role(sms_object):
    assert "defaultteacher" in sms_object.roles["teacher"]
    assert sms_object.get_users_role("default_student") == "student"