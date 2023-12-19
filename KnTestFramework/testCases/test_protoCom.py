import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from KnTestFramework.utilities import BaseClass


# @pytest.mark.usefixtures("setup")
class TestShopPage(BaseClass):
    def test_ShopPage(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/shop")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        phoneList = self.driver.find_elements(By.XPATH, "//button[@class='btn btn-info']")
        phoneList[0].click()
        phoneList[1].click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn btn-success']").click()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("United States")
        wait = WebDriverWait(self.driver, 12)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='United States of America']"))).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//div/label[@for='checkbox2']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type*='submit']").click()
        confirmMsg = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success alert-dismissible']").text
        print(confirmMsg)
        assert confirmMsg == "Success! Thank you! Your order will be delivered in next few weeks :-)."






