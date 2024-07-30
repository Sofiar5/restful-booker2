import allure
import pytest
import requests
import test_2_booking_post

@allure.feature('Booking Feature')
@allure.suite('Get Booking Suite')
@allure.title('Test Getting All Bookings')
@allure.description('This test retrieves all bookings and checks the response status and content.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_all():
    with allure.step('Send GET request to retrieve all bookings'):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step('Verify the response contains a non-empty list'):
        assert len(response.json()) > 0, "The list should not be empty"

@allure.feature('Booking Feature')
@allure.suite('GET Booking Suite')
@allure.title('Test Getting Booking By ID')
@allure.description('This test retrieves a booking by ID and checks the response status and content.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_by_id():
    with allure.step('Send request to get booking by ID'):
        response = requests.get(f"https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}")

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify the response contains "firstname"'):
        assert 'firstname' in response_data, "The response should have 'firstname'"

    with allure.step('Verify the response contains "lastname"'):
        assert 'lastname' in response_data, "The response should have 'lastname'"

    with allure.step('Verify the response contains "totalprice"'):
        assert 'totalprice' in response_data, "The response should have 'totalprice'"

    with allure.step('Verify the response contains "depositpaid"'):
        assert 'depositpaid' in response_data, "The response should have 'depositpaid'"

    with allure.step('Verify the response contains "bookingdates"'):
        assert 'bookingdates' in response_data, "The response should have 'bookingdates'"

    with allure.step('Verify the response contains "checkin"'):
        assert 'checkin' in response_data['bookingdates'], "The bookingdates should have 'checkin'"

    with allure.step('Verify the response contains "checkout"'):
        assert 'checkout' in response_data['bookingdates'], "The bookingdates should have 'checkout'"

    with allure.step('Verify the response contains "additionalneeds"'):
        assert 'additionalneeds' in response_data, "The response should have 'additionalneeds'"

    with allure.step('Verify the value of "depositpaid" is boolean'):
        assert response_data['depositpaid'] is True or response_data['depositpaid'] is False, 'ERRORRR depositpaid'

    with allure.step('Verify the value of "totalprice" is a number'):
        assert isinstance(response_data['totalprice'], (int, float)), 'Total price should be a number'

    with allure.step('Printing response'):
        allure.attach(response.text,'Response',allure.attachment_type.JSON)