from mechanisms import open_new_tab, slow_scroll
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def visit(driver):
    driver.get("https://google.com")
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/button[2]/div').click()

    time.sleep(2)
    search_box = driver.find_element_by_xpath("//*[@title='Search']")
    for char in "Delft University of Technology":
        search_box.send_keys(char)
        time.sleep(0.05)
    search_box.send_keys(Keys.ENTER)