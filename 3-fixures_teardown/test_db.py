import pytest
from db import Database

@pytest.fixture
def db():
    """provides a fresh database instance for each test"""
    database = Database()
    yield database # provide the fixture instance
    database.data.clear() # teardown: clear the database after test

def test_add_user(db):
    db.add_user("1", "Stephane")
    assert db.get_user("1") == "Stephane"

def test_add_duplicate_user(db):
    db.add_user("1", "Stephane")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user("1", "Boska")

def test_delete_user(db):
    db.add_user(2, "Boska")
    db.delete_user(2)
    assert db.get_user(2) is None