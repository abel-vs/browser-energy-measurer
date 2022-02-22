import drivers
import time

driver = drivers.chrome_driver()
time.sleep(10)
driver.quit()