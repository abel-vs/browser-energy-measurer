from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def safari_driver():
    return webdriver.Safari()

def chrome_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def chromium_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

def edge_driver():
    return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

def firefox_driver():
    return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    

