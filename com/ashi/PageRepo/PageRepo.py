from com.ashi.Locators import *

class LoginPage(LoginPageLocators):

    def enterMailId(self):
        EmailIdTxtBox.send_keys('ashi.sri.18@gmail.com')
        NextBtn.click()
