import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestHomePage():
    def test_homepageinfo(self):
        # enter name
        # enter email address
        # enter password
        # Select check box
        # select gender from dropdown menu
        # Select employment status
        # enter date of birth
        # submit form
        time.sleep(3)


# self.driver: self keyword is always passed as an argument to a class function and is linked to the driver we requested in "setup" fixture








