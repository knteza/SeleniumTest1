import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
service_obj = Service('/Users/kntez/Documents/FX/chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")                            # email: demoxgmail.com, PW: make one up
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//div/input[@name='name']").send_keys("Simba")
driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("demoxgmail.com")
driver.find_element(By.CSS_SELECTOR, "input[name*='email']").clear()
driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("rahulshetty")
driver.find_element(By.XPATH, "//div/input[@type='checkbox']").click()
dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))             #Select is a class that allows you to select from a dropdown menu
dropdown.select_by_index(1)
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "input[type='date']").send_keys("05/13/2001")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(3)








