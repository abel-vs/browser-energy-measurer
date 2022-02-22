import drivers
import time

from mechanisms import slow_scroll

browser = drivers.chrome_driver()
browser.get("https://en.wikipedia.org")
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Immediate scroll
slow_scroll(browser, 10)
time.sleep(3)
browser.close()