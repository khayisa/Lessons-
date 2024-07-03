import pytest 
import requests 
import functions.service as service
import unittest.mock as mock 


@mock.patch("functions.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Khanyi"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Khanyi"

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_reponse = mock.Mock()
    mock_reponse.status_code = 200
    mock_reponse.json.return_value = {"id": 1,"name": "John Doe"}
    mock_get.return_value = mock_reponse
    data = service.get_users()
    assert data ==  {"id" :1,"name": "John Doe"}
    

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_reponse = mock.Mock()
    mock_reponse.status_code = 400
    mock_get.return_value = mock_reponse
    with pytest.raises(requests.HTTPError):
        service.get_users()
     

