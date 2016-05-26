from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://wwww.facebook.com")

    def test_login(self):
        fb_uname = "Your Email Here"
        fb_upasee = "Your Password Here"

        emailFieldID = "email"
        passFieldID = "pass"
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoXpath = "(//a[contains(@href, 'logo')])[1]"

        emailFieldElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(fb_uname)

        passFieldElement.clear()
        passFieldElement.send_keys(fb_upasee)

        loginButtonElement.click()
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()








