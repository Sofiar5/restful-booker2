import requests
import pytest
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking service')
@allure.suite('Ping Tests')
@allure.title('Health Check Test')
@allure.description('This test checks if the health endpoint is reachable and returns the expected status code.')
@allure.severity('BLOCKER')
def test_health_check():
    with allure.step('Send GET request to health check endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step('Verify the response status code is 201'):
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"