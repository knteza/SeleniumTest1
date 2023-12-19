# set up and tear down methods
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
                                # ProtoCommerce Site #
# in order to call this fixture (setup) at the class lever, it needs to be expressed here
                                                                    # request must be passed as an argument in the fixture it will be used. it provides information of the requesting test function ie. test_homepageinfo in ProtoCommerce file
# def test_homePg():
# service_obj = Service('/Users/kntez/Documents/FX/chromedriver.exe')
# driver: WebDriver = webdriver.Chrome(service=service_obj)               # this method (driver.) instantiates the driver...which will also need to be called in the test case file
# driver.get("https://rahulshettyacademy.com/angularpractice/")           # email: demoxgmail.com, PW: make one up
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH, "//div/input[@name='name']").send_keys("Kenzo")
# driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("demoxgmail.com")
# driver.find_element(By.CSS_SELECTOR, "input[name*='email']").clear()
# driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("secretpassword")
# driver.find_element(By.XPATH, "//div/input[@type='checkbox']").click()
# dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))             #Select is a class that allows you to select from a dropdown menu (male / female)
# dropdown.select_by_index(1)
# driver.find_element(By.ID, "inlineRadio1").click()
# driver.find_element(By.CSS_SELECTOR, "input[type='date']").send_keys("05/13/2001")
# driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
# driver.implicitly_wait(3)
# driver.get("https://rahulshettyacademy.com/angularpractice/shop")
# driver.maximize_window()
# driver.implicitly_wait(3)
# phoneList = driver.find_elements(By.XPATH, "//button[@class='btn btn-info']")
# phoneList[0].click()
# phoneList[1].click()
# driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
# driver.implicitly_wait(3)
# driver.find_element(By.CSS_SELECTOR, "button[class*='btn btn-success']").click()
# driver.find_element(By.XPATH, "//input[@id='country']").send_keys("United States")
# wait = WebDriverWait(driver, 12)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='United States of America']"))).click()
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "//div/label[@for='checkbox2']").click()
# driver.find_element(By.CSS_SELECTOR, "input[type*='submit']").click()
# confirmMsg = driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success alert-dismissible']").text
# print(confirmMsg)
# assert confirmMsg == "Success! Thank you! Your order will be delivered in next few weeks :-)."