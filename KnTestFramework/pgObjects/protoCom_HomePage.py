import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#
# @pytest.mark.usefixtures("setup")
# class TestSubmitFormHomePg():                    # will have details that the driver needs to understand to link it to other pages
#     def __init__(self, driver):                # define a constructor here so driver can recognize that this class (HomePage) is one of the compartments of the train to be able to link it to other pages
#         self.driver = driver
#
#     def enterName(self):
#         self.driver.find_element(By.XPATH, "//div/input[@name='name']").send_keys("Kenzo")
#
#     def enterEmail(self):
#         self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("demoxgmail.com")
#
#     def enterPassword(self):
#         self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").clear()
#         self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("secretpassword")
#
#     def selectCheckbox(self):
#         self.driver.find_element(By.XPATH, "//div/input[@type='checkbox']").click()
#         dropdown = Select(self.driver.find_element(By.XPATH, "//select[@class='form-control']"))             #Select is a class that allows you to select from a dropdown menu (male / female)
#         dropdown.select_by_index(1)
#
#     def selectEmploymentStatus(self):
#         self.driver.find_element(By.ID, "inlineRadio1").click()
#
#     def enterDOB(self):
#         self.driver.find_element(By.CSS_SELECTOR, "input[type='date']").send_keys("05/13/2001")
#
#     def submitForm(self):
#         self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
#         time.sleep(3)