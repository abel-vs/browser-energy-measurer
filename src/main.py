import drivers
from mechanisms import open_new_tab, wait
from scenarios import wikipedia, soundcloud, amazon, google

driver = drivers.chrome_driver()

scenarios = [
     lambda: wikipedia.visit(driver),
     lambda: amazon.visit(driver),
     lambda: google.visit(driver),
     lambda: soundcloud.visit(driver)
]

for scenario in scenarios:
    scenario()
    open_new_tab()

wait(3)
driver.quit()
