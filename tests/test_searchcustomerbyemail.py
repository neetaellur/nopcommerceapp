from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time
from utilities.readProperties import ReadConfig

from pageObjects.loginpage import LogIn
from pageObjects.Addcustomerpage import AddCustomer
from utilities.customLogger import LogGen
from pageObjects.searchcustomer import SearchCustomer
class Test_004_SearchCustomerByEmail:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    @pytest.mark.regression
    def test_searchcustomeby_email(self,setup):
        self.logger.info("**************searchbyemail_004*********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LogIn(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***********login sucessfull*************")
        self.logger.info("*********search customer by email*************")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomermenuitem()
        self.logger.info("*********searching customer by id*************")
        searchcust=SearchCustomer(self.driver)
        searchcust.setemail("victoria_victoria@nopCommerce.com")
        searchcust.clicksearch()
        time.sleep(5)
        status=searchcust.searchcustomerbyemail("victoria_victoria@nopCommerce.com")

        assert True==status
        self.logger.info("********testcase_search by email finished***")


