import drivers
import time

browser = drivers.chrome_driver()
browser.get("https://en.wikipedia.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
browser.close()