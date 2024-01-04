import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()

# cls.driver = any drivers found in a class that calls this fixture "setup" will be set to the local driver that has been instantiated here
# thus request (keyword).cls.driver = driver (local driver) above




















