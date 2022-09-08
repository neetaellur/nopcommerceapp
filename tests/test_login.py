from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from utilities.readProperties import ReadConfig

from pageObjects.loginpage import LogIn
from utilities.customLogger import LogGen
class Test_001_LogIn:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        self.logger.info("***********Test_001_LogIn*********")
        self.logger.info("***********verify home page title*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title=self.driver.title
        if actual_title=="Your store. Login":
            self.driver.close()
            self.logger.info("********home page title test is passed********")
            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\"+"test_home.png")
            self.driver.close()
            self.logger.error("********home page title test is failed********")
            assert False


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***********verify login  page title*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lg=LogIn(self.driver)
        self.lg.setusername(self.username)
        self.lg.setpassword(self.password)
        self.lg.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("********login test is passed*******")

            assert True
        else:
            self.driver.save_screenshot(r".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("******login test is failed********")

            assert False

