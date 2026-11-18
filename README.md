# Pytest Training

A hands-on collection of small Python projects for learning pytest. Each numbered folder demonstrates a different testing concept and includes a `notes.txt` file summarizing its tests.

## Requirements

- Python 3
- pytest
- pytest-mock
- Flask
- Requests

Install the project dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, enable script execution for the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Course Structure

### 1. Basic Testing

Folder: `1-basic`

Introduces basic pytest assertions and exception tests with simple weather, addition, and division functions.

### 2. Fixture Setup

Folder: `2-fixures_setup`

Demonstrates a pytest fixture that creates a fresh `UserManager` instance for each test.

### 3. Fixture Teardown

Folder: `3-fixures_teardown`

Shows fixture setup and teardown with an in-memory database that is cleared after every test.

### 4. Parameterized Testing

Folder: `4-parameterized_testing`

Uses `pytest.mark.parametrize` to test multiple inputs against one test function.

### 5. Mocking

Folder: `5-mocks`

Covers mocking HTTP requests, SQLite connections, and service dependencies with pytest-mock.

### 6. API Testing

Folder: `6-api_testing`

Uses Flask's test client to test HTTP endpoints, successful responses, validation errors, and not-found responses.

## Running the Tests

Run all tests from the repository root:

```powershell
pytest
```

Run a specific lesson:

```powershell
pytest 1-basic
pytest 2-fixures_setup
pytest 3-fixures_teardown
pytest 4-parameterized_testing
pytest 5-mocks
pytest 6-api_testing
```

Run one test file:

```powershell
pytest 1-basic/test_main.py
```

Useful pytest options:

```powershell
pytest -v
pytest -q
pytest --collect-only
```
