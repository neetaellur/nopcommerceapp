import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class AddCustomer:
    lnkcustomers_menu_path="//a[@href='#']//p[contains(text(),'Customers')]"
    linkcustomers_menuitem_path="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath="//a[@class='btn btn-primary']"
    txtemail_path="//input[@id='Email']"
    txt_password_path="//input[@id='Password']"
    txt_firstname_xpath="//input[@id='FirstName']"
    txt_lastname_xpath="//input[@id='LastName']"
    male_id="//input[@id='Gender_Male']"
    female_id="//input[@id='Gender_Female']"
    Dob_xpath="//input[@id='DateOfBirth']"
    txt_companyname_xpath="//input[@id='Company']"
    select_tax_xpath="//input[@id='IsTaxExempt']"
    select_customer_roles="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    list_registered_xpath="//li[normalize-space()='Registered']"
    list_administraters_xpath="//li[normalize-space()='Administrators']"
    list_guest_xpath="//li[normalize-space()='Guests']"
    list_forummoderater_xpath="//li[normalize-space()='Forum Moderators']"
    list_guest_xpath="//li[normalize-space()='Guests']"
    list_vendor_xpath="//li[@id='81d32ecf-bebb-4fae-806a-112562f47f04']"
    drp_vendor_xpath="//select[@id='VendorId']"
    btnsave_xpath="//button[@name='save']"
    admincontent_xpath="//textarea[@id='AdminComment']"
    def __init__(self,driver):
        self.driver=driver

    def clickoncustomermenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_menu_path).click()
    def clickoncustomermenuitem(self):
        self.driver.find_element(By.XPATH,self.linkcustomers_menuitem_path).click()
    def clickonAddnew(self):
        self.driver.find_element(By.XPATH,self.btn_addnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtemail_path).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_password_path).send_keys(password)
    def setfirst_name(self,firstname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(firstname)
    def setlast_name(self,lastname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lastname)
    def setcustomerrole(self,role):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.select_customer_roles).click()
        if role =="Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.list_registered_xpath)
        elif role =="Administrators":
            self.listitem=self.driver.find_element(By.XPATH,self.list_administraters_xpath)
        elif role =="Guest":
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem=self.driver.find_element(By.XPATH,self.list_guest_xpath)
        elif role=="Vendors":
            self.listitem=self.driver.find_element(By.XPATH,self.list_vendor_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.list_guest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)
    def setManagerofvendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drp_vendor_xpath))
        drp.select_by_visible_text(value)
    def setgender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.male_id).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.female_id).click()
        else:
            self.driver.find_element(By.XPATH,self.male_id).click()
    def setdob(self,dob):
        self.driver.find_element(By.XPATH,self.Dob_xpath).send_keys(dob)
    def setcompanyname(self,comname):
        self.driver.find_element(By.XPATH,self.txt_companyname_xpath).send_keys(comname)
    def setAdmincontent(self,content):
        self.driver.find_element(By.XPATH,self.admincontent_xpath).send_keys(content)
    def clickonsave(self):
        self.driver.find_element(By.XPATH,self.btnsave_xpath).click()




