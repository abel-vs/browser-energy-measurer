from selenium.webdriver.common.keys import Keys

from mechanisms import random_wait, wait

def visit(driver):
    driver.get("https://soundcloud.com")
    random_wait()
    # Click on cookie banner
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    wait(2)
    # Click search bar
    searchbar = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/span/span/form/input")
    searchbar.click()
    searchbar.send_keys("Can't Stop")
    searchbar.send_keys(Keys.RETURN)
    wait(2)
    # Press play
    play = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/ul/li[2]/div/div/div/div[2]/div[1]/div/div/div[1]/a")
    play.click()
    # Let song play
    wait(5)
