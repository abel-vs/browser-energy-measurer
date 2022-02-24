import drivers
import time
from scenarios import wikipedia

driver = drivers.chrome_driver()

scenarios = [
     lambda: wikipedia.visit(driver),
     lambda: wikipedia.visit(driver),
]


for scenario in scenarios:
    scenario()

time.sleep(3)
driver.quit()