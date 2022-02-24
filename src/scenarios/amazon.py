from mechanisms import open_new_tab, slow_scroll
from selenium.webdriver.common.keys import Keys
import time

def visit(driver):
    driver.get("https://amazon.com")
    time.sleep(2)
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    for char in "Game of Thrones":
        search_box.send_keys(char)
        time.sleep(0.05)
    search_box.send_keys(Keys.ENTER)

    driver.get("https://www.amazon.com/A-Game-of-Thrones-audiobook/dp/B0001DBI1Q/ref=sr_1_6?crid=3VSDCECUKF87A&keywords=game+of+thrones&qid=1645707808&sprefix=game+of+throne%2Caps%2C193&sr=8-6")