from com.ashi.GenericLib.Initilization import *
import time

class LoginPageLocators(Initilization):

    driver = Initilization.driver

    def enterMailId(cls):
        emailIdTxtBox = cls.driver.find_element_by_id('Email')
        emailIdTxtBox.send_keys('ashish12psitsrivastava@gmail.com')
        time.sleep(2)

    def clickNextBtn(cls):
        NextBtn = cls.driver.find_element_by_id('next')
        NextBtn.click()
        time.sleep(2)

    def enterPassword(cls):
        pswrdTxtBox = cls.driver.find_element_by_id('Passwd')
        pswrdTxtBox.send_keys('jai$sri$ram')
        time.sleep(2)

    def clickSignIn(cls):
        signInBtn = cls.driver.find_element_by_id('signIn')
        signInBtn.click()
        time.sleep(2)

    def clickCheckBox(cls):
        signedInCheckBox = cls.driver.find_element_by_name('PersistentCookie')
        signedInCheckBox.click()
        time.sleep(2)

class InboxPageLocators(Initilization):
    driver = Initilization.driver
    def getUnreadSubjects(cls):
        unreadSubjects = cls.driver.find_elements_by_xpath('//tbody/tr/td[6]//span/b')
