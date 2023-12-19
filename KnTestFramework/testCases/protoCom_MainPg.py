from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from KnTestFramework.utilities import BaseClass


# @pytest.mark.usefixtures("setup") =>> no need for this if you create and call a base class that inherits the setup fixture in conftest
class TestHomePage(BaseClass):
    def test_protoHomePg(self):
        self.driver.find_element(By.XPATH, "//div/input[@name='name']").send_keys("Kenzo")
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("demoxgmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='email']").send_keys("secretpassword")
        self.driver.find_element(By.XPATH, "//div/input[@type='checkbox']").click()
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@class='form-control']"))
        dropdown.select_by_index(1)
        self.driver.find_element(By.ID, "inlineRadio1").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='date']").send_keys("05/13/2001")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.driver.implicitly_wait(3)


