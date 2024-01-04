from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestProtoHomePg:
    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "//div/input[@name='name']")
    email = (By.CSS_SELECTOR, "input[name*='email']")
    clearEntryBox = (By.CSS_SELECTOR, "input[name*='email']")
    enterPW = (By.CSS_SELECTOR, "input[type$='password']")
    markBox = (By.XPATH, "//div/input[@type='checkbox']")
    # dropdownMenu = (By.XPATH, "//select[@class='form-control']")
    employmentStatus = (By.ID, "inlineRadio1")
    dob = (By.CSS_SELECTOR, "input[type='date']")
    submitBtn = (By.CSS_SELECTOR, "input[type='submit']")

    def enterName(self):
        self.driver.find_element(*TestProtoHomePg.name).send_keys("Kenzo")

    def enterEmail(self):
        self.driver.find_element(*TestProtoHomePg.email).send_keys("kenzo123@gmail.com")

    def enterPassword(self):
        # self.driver.find_element(*TestProtoHomePg.clearEntryBox).clear()
        # self.driver.implicitly_wait(2)
        self.driver.find_element(*TestProtoHomePg.enterPW).send_keys("secretSauce")

    def checkBox(self):
        self.driver.find_element(*TestProtoHomePg.markBox).click()

    def selectGender(self):
        # self.driver.find_element(*TestProtoHomePg.dropdownMenu)
        self.driver.find_element(By.XPATH, "//div/input[@type='checkbox']").click()
        dropdown = Select(self.driver.find_element(By.XPATH,"//select[@class='form-control']"))  # Select is a class that allows you to select from a dropdown menu (male / female)
        dropdown.select_by_index(1)

    def empStatus(self):
        self.driver.find_element(*TestProtoHomePg.employmentStatus).click()

    def birthDay(self):
        self.driver.find_element(*TestProtoHomePg.dob).send_keys("05/13/2001")

    def submitForm(self):
        self.driver.find_element(*TestProtoHomePg.submitBtn).click()


class TestCheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    clickShopBtn = (By.XPATH, "//li/a[@href='/angularpractice/shop']")
    # selectPhone = (By.XPATH, "//button[@class='btn btn-info']")
    clickCheckOutBtn = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")
    clickCheckOutBtn2 = (By.CSS_SELECTOR, "button[class*='btn btn-success']")

    def shopBtn(self):
        self.driver.find_element(*TestCheckOutPage.clickShopBtn).click()

    # def listOfPhones(self):
    #     phoneList = self.driver.find_elements(*TestCheckOutPg.selectPhone)
    #     phoneList[0].click()
    #     phoneList[1].click()

    def checkOutBtn(self):
        self.driver.find_element(*TestCheckOutPage.clickCheckOutBtn).click()

    def checkOutBtn2(self):
        self.driver.find_element(*TestCheckOutPage.clickCheckOutBtn2).click()





