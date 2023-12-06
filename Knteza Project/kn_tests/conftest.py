# set up and tear down methods
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="class")                                              # in order to call this fixture (setup) at the class lever, it needs to be expressed here
def setup(request):                                                         # request must be passed as an argument in the fixture it will be used. it provides information of the requesting test function ie. test_homepageinfo in ProtoCommerce file
    service_obj = Service('/Users/kntez/Documents/FX/chromedriver.exe')
    driver: WebDriver = webdriver.Chrome(service=service_obj)               # this method (driver.) instantiates the driver...which will also need to be called in the test case file
    driver.get("https://rahulshettyacademy.com/angularpractice/")           # email: demoxgmail.com, PW: make one up
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver                                            # after driver is instantiatied above, we can now request this fixture at the class level of the requesting class that calls on this 'setup' fixture.
    yield
    driver.close()
