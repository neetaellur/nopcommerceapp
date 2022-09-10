from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time
from utilities.readProperties import ReadConfig

from pageObjects.loginpage import LogIn
from pageObjects.Addcustomerpage import AddCustomer
from utilities.customLogger import LogGen
import string
import random
from webdriver_manager.chrome import ChromeDriverManager
class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("***********Test_003_AddCustomer**********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LogIn(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***************log in sucessful*********")
        self.logger.info("*******start add customer test**************")
        self.addcust=AddCustomer(self.driver)
        time.sleep(5)
        self.addcust.clickoncustomermenu()
        time.sleep(2)
        self.addcust.clickoncustomermenuitem()
        time.sleep(2)
        self.addcust.clickonAddnew()
        self.logger.info("***********providing customer info***********")
        time.sleep(2)
        self.email=random_generator()+"@gmail.com"
        time.sleep(2)
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setcustomerrole("Guest")
        self.addcust.setManagerofvendor("Vendor 2")
        self.addcust.setgender("Male")
        self.addcust.setfirst_name("Neeta")
        self.addcust.setlast_name("Ellur")
        self.addcust.setdob("7/05/1987")
        self.addcust.setcompanyname("busyqa")
        self.addcust.setAdmincontent("testing")
        self.addcust.clickonsave()
        self.logger.info("********saving customer info **********")
        self.logger.info("***************add customer validation started*******")
        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*****add customere test passes***********")
        else:
            self.driver.save_screenshot(r".\\screensshots\\"+"test_addcustomer_scr.png")
            self.logger.error("*********add customer test failed*********")
            assert True == False
        self.driver.close()
        self.logger.info("**********ending add customer  test**********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
