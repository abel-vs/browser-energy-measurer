import drivers
import time
from mechanisms import slow_scroll
from selenium import webdriver

from scenarios import wikipedia, amazon, google, youtube
from mechanisms import open_new_tab, wait
from scenarios import wikipedia, soundcloud, amazon, google

driver = drivers.chrome_driver()

scenarios = [
     lambda: wikipedia.visit(driver),
     lambda: amazon.visit(driver),
     lambda: soundcloud.visit(driver),
     lambda: amazon.visit(driver),
     lambda: google.visit(driver)
]

for scenario in scenarios:
    scenario()
    open_new_tab(driver)

wait(10)
driver.quit()
