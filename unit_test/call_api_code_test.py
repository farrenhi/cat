import requests
import requests_mock
import pytest
from .. import model

def test_call_api_code():
    '''Should get a list of 4 integers
    '''      
    # Create a context manager to intercept requests made using requests
    with requests_mock.Mocker() as mocker:
        # Configure a mock GET request
        url = "https://www.random.org/integers/?num=4&min=0&max=10&col=1&base=10&format=plain&rnd=new"
        body_text = "1\n2\n3\n4\n"
        mocker.get(url, status_code=200, text=body_text)
        
        # Make a call to some method/function that internally makes an HTTP request
        result = model.call_api_code(10)
    assert result == [1, 2, 3, 4]

def test_call_api_code_failure():
    '''Should handle API call failure gracefully
    '''
    with requests_mock.Mocker() as mocker:
        url = "https://www.random.org/integers/?num=4&min=0&max=10&col=1&base=10&format=plain&rnd=new"
        mocker.get(url, exc=requests.exceptions.RequestException("Mocked error"))
        
        with pytest.raises(requests.exceptions.RequestException):
            model.call_api_code(10)
