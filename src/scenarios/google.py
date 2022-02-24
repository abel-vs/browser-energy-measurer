from mechanisms import open_new_tab, slow_scroll
from selenium.webdriver.common.keys import Keys
import time

def visit(driver):
    driver.get("https://google.com")
    time.sleep(2)
    search_box = driver.find_element_by_xpath("//*[@title='Search']")
    for char in "Delft University of Technology":
        search_box.send_keys(char)
        time.sleep(0.05)
    search_box.send_keys(Keys.ENTER)