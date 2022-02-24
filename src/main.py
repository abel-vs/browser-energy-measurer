import drivers
import time
from scenarios import wikipedia, instagram

driver = drivers.chrome_driver()

scenarios = [
     lambda: instagram.visit(driver),
]

for scenario in scenarios:
    scenario()

time.sleep(3)
driver.quit()
