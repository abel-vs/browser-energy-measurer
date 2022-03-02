import drivers
import time
from mechanisms import slow_scroll
from selenium import webdriver

from scenarios import wikipedia, amazon, google, youtube
from mechanisms import open_new_tab, wait
from scenarios import wikipedia, soundcloud, amazon, google

driver = drivers.firefox_driver()

scenarios = [
     lambda: soundcloud.visit(driver),
     lambda: wikipedia.visit(driver),
     lambda: amazon.visit(driver),
     lambda: youtube.visit(driver),
     # lambda: google.visit(driver),
]

for scenario in scenarios:
    scenario()
    open_new_tab(driver)

time.sleep(1)
driver.quit()
