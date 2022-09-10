from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import time
import openpyxl

from pageObjects.loginpage import LogIn
from utilities.customLogger import LogGen
class Test_002_ddt_LogIn:
    baseurl = ReadConfig.getApplicationURL()
    path=r".//testdata/datatest.xlsx"


    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("***test_002_ddt_login*******")
        self.logger.info("***********verify login  page title*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lg=LogIn(self.driver)

        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        print("num of rows:",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
           self.user= XLUtils.readData(self.path,"Sheet1",r,1)
           self.pwd = XLUtils.readData(self.path, "Sheet1", r, 2)
           self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
           self.lg.setusername(self.user)
           self.lg.setpassword(self.pwd)
           self.lg.clicklogin()
           time.sleep(2)

           act_title=self.driver.title
           exp_title="Dashboard / nopCommerce administration"
           if act_title==exp_title:
              if self.exp=="pass":
                self.logger.info("test is passed")
                self.lg.clicklogout()
                lst_status.append("pass")
              elif self.exp=="fail":
                self.logger.info("test is failed")
                self.lg.clicklogout()
                lst_status.append("fail")
           elif act_title != exp_title:
              if self.exp == "pass":
                self.logger.info("test is failed")

                lst_status.append("fail")
              elif self.exp == "fail":
                self.logger.info("test is passed")

                lst_status.append("pass")
        if "fail" not in lst_status:
            self.logger.info("***login ddt is passed****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********login dtt is failed********")
            self.driver.close()
            assert False
        print(lst_status)
