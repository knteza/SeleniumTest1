from selenium.webdriver.common.by import By


class TestCheckOutPg:
    def __init__(self, driver):
        self.driver = driver

    clickShopBtn = (By.XPATH, "//li/a[@href='/angularpractice/shop']")

    def shopBtn(self):
        self.driver.find_element(*TestCheckOutPg.clickShopBtn).click()

