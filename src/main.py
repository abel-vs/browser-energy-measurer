import drivers
import time
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