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

        self.driver.find_element(By.XPATH, "//div/input[@name='name']").send_keys("Simba")
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("demoxgmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("secretpassword")
        # Check box, select gender from dropdown menu
        self.driver.find_element(By.XPATH, "//div/input[@type='checkbox']").click()
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@class='form-control']"))             #Select is a class that allows you to select from a dropdown menu
        dropdown.select_by_index(1)
        # Select employment status, enter date of birth and click submit
        self.driver.find_element(By.ID, "inlineRadio1").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='date']").send_keys("05/13/2001")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(3)


# self.driver: self keyword is always passed as an argument to a class function and is linked to the driver we requested in "setup" fixture








