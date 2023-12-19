import time
import pytest


class TestHomePage:
    def test_homepageinfo(self):
        hp = SubmitFormHomePg(self.driver)
        # enter name
        hp.enterName("Kimuli")
        # enter email address
        hp.enterEmail("demox@gmail.com")
        # enter password
        hp.enterPassword("secretpassword")
        # Select check box
        hp.selectCheckbox.click()
        # select gender from dropdown menu
        # Select employment status
        hp.selectEmploymentStatus.click()
        # enter date of birth
        hp.enterDOB("05/13/2001")
        # submit form
        hp.submitForm.click()





# self.driver: self keyword is always passed as an argument to a class function and is linked to the driver we requested in "setup" fixture








