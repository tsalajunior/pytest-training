import pytest
from services import UserService, APIClient  # assume this is in my_module.py


def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)  # create a mock api client

    # Mock get_user_data to return a fake user
    mock_api_client.get_user_data.return_value = {"id": 1, "name": "Stephane"}

    service = UserService(mock_api_client)  # inject mock api client

    result = service.get_username(1)  # call method that depends on the mock

    # Assertions
    assert result == "STEPHANE"  # check if processing was done correctly
    mock_api_client.get_user_data.assert_called_once_with(1)  # ensure correct api call
