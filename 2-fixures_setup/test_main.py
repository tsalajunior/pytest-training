import pytest
from main import UserManager

@pytest.fixture
def user_manager():
    """create a UserManager instance before testing"""
    return UserManager()

def test_add_user(user_manager):
    """test adding a user"""
    assert user_manager.add_user("john_doe", "john.doe@example.com") == True
    assert user_manager.get_user("john_doe") == "john.doe@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john.doe@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")