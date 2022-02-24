import drivers
import time
from mechanisms import slow_scroll
from selenium import webdriver

from scenarios import wikipedia, amazon, google, youtube

driver = drivers.chrome_driver()

scenarios = [
     lambda: wikipedia.visit(driver),
     lambda: amazon.visit(driver),
     # lambda: google.visit(driver),
     lambda: youtube.visit(driver)
]

for scenario in scenarios:
    scenario()

time.sleep(3)
driver.quit()
