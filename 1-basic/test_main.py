import pytest
from main import get_weather, add, divide

def test_get_weather():
    assert get_weather(-5) == "It's freezing!"
    assert get_weather(10) == "It's cold."
    assert get_weather(25) == "It's warm."
    assert get_weather(35) == "It's hot!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)