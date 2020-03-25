from selenium import webdriver
import time
import os


class jobChecker:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def navigate(self, link):
        self.driver.get(link)
        # self.driver.switch_to().alert().sendKeys("Text")

    def emailLogin(self):

        emailInput = self.driver.find_element_by_xpath(
            '//*[@id="defaultControl_ctl00_segment1372_ctl00_place34_ctl00_PreLoginUserName"]'
        )
        emailInput.send_keys("zmcdo66@eq.edu.au")
        loginButton = self.driver.find_element_by_xpath('//*[@id="btnDummyNext"]')
        loginButton.click()

    def login(self):
        passwordInput = self.driver.find_element_by_id(
            "defaultControl_ctl00_segment1372_ctl00_place34_ctl00_Password"
        )
        passwordInput.send_keys("n9C9BN7Xjkot")


nelson = jobChecker()

nelson.navigate("https://www.nelsonnet.com.au/login")
time.sleep(10)
nelson.emailLogin()
time.sleep(5)

nelson.login()
