import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from KnTestFramework.utilities.BaseClass import BaseClass
from KnTestFramework.pgObjects.proto_HomePg import TestProtoHomePg, TestCheckOutPage


# @pytest.mark.usefixtures("setup") =>> no need for this if you create and call a base class that inherits the setup fixture in conftest
# class TestHomePage(BaseClass):                          # end-to-end test
#     def test_protoHomePg(self):
#         testNameEntry = TestProtoHomePg(self.driver)
#         testNameEntry.enterName()
#         testEmailEntry = TestProtoHomePg(self.driver)
#         testEmailEntry.enterEmail()
#         testPasswordEntry = TestProtoHomePg(self.driver)
#         testPasswordEntry.enterPassword()
#         testCheckBox = TestProtoHomePg(self.driver)
#         testCheckBox.checkBox()
#         testMenu = TestProtoHomePg(self.driver)
#         testMenu.selectGender()
#         testEmpStatus = TestProtoHomePg(self.driver)
#         testEmpStatus.empStatus()
#         testDOB = TestProtoHomePg(self.driver)
#         testDOB.birthDay()
#         testSubmitBtn = TestProtoHomePg(self.driver)
#         testSubmitBtn.submitForm()
#         time.sleep(4)


class TestShopPage(BaseClass):

    def test_ShopPage(self):
        testShopBtn = TestCheckOutPage(self.driver)
        testShopBtn.shopBtn()
        phoneList = self.driver.find_elements(By.XPATH, "//button[@class='btn btn-info']")
        phoneList[0].click()
        phoneList[1].click()
        testCheckOutBtn = TestCheckOutPage(self.driver)
        testCheckOutBtn.checkOutBtn()
        self.driver.implicitly_wait(3)
        testCheckOutBtn2 = TestCheckOutPage(self.driver)
        testCheckOutBtn2.checkOutBtn2()
        # self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("United States")
        time.sleep(5)
        # wait = WebDriverWait(self.driver, 12)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='United States of America']"))).click()
        # self.driver.implicitly_wait(5)
        # self.driver.find_element(By.XPATH, "//div/label[@for='checkbox2']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[type*='submit']").click()
        # confirmMsg = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success alert-dismissible']").text
        # print(confirmMsg)
        # assert confirmMsg == "Success! Thank you! Your order will be delivered in next few weeks :-)."

