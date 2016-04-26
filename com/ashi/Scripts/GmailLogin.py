from com.ashi.PageRepo.Locators import *

class GmailLogin(LoginPageLocators):
    loginPageLocators = LoginPageLocators()
    def test_gmailLogin(cls):
        cls.loginPageLocators.enterMailId()
        cls.loginPageLocators.clickNextBtn()
        cls.loginPageLocators.enterPassword()
        cls.loginPageLocators.clickCheckBox()
        cls.loginPageLocators.clickSignIn()
