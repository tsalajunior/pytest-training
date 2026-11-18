import pytest
from api import app  # import the flask app


@pytest.fixture
def client():
    """provides a test client for the flask app"""
    app.config["TESTING"] = True  # enable testing mode
    with app.test_client() as client:
        yield client  # provides the test client instance


def test_add_user(client):
    """Test adding a new user"""
    response = client.post("/users", json={"id": 1, "name": "Stephane"})

    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Stephane"}


def test_get_user(client):
    """test retrieving a user"""
    # first add a user
    client.post("/users", json={"id": 2, "name": "Boska"})

    # then retrieve the user
    response = client.get("/users/2")

    assert response.status_code == 200
    assert response.json == {"id": 2, "name": "Boska"}


def test_user_not_found(client):
    """test retrieving a non existant user"""
    response = client.get("/users/98")

    assert response.status_code == 404
    assert response.json == {"Error": "User not found!"}


def test_add_duplicate_user(client):
    """Test adding a duplicate user"""
    client.post("/users", json={"id": 3, "name": "Junior"})
    response = client.post("/users", json={"id": 3, "name": "Junior"})

    assert response.status_code == 400
    assert response.json == {"Error": "User already exists!"}
