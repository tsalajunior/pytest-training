def get_weather(temp):
    if temp < 0:
        return "It's freezing!"
    elif 0 <= temp < 20:
        return "It's cold."
    elif 20 <= temp < 30:
        return "It's warm."
    else:
        return "It's hot!"

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b