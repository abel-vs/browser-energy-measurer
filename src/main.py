import drivers
import time
from mechanisms import slow_scroll
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from scenarios import wikipedia

browser = drivers.chrome_driver()

scenarios = [
     lambda: wikipedia.visit(browser),
     lambda: wikipedia.visit(browser),
]


for scenario in scenarios:
    scenario()

time.sleep(3)
browser.close()
