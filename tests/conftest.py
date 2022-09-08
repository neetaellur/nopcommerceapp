import xdist
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def setup(browser):
    srv=Service(r"C:\Users\sande\Desktop\webdevlopment\chromedriver.exe")
    driver=webdriver.Chrome(service=srv)
    if browser=="chrome":
     return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['project name'] ='nop commerce'
    config._metadata['module name'] ='customers'
    config._metadata['tester']= 'neeta'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)