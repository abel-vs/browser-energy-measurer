import time

from selenium.webdriver import Keys

def visit(driver):
    driver.get("https://www.youtube.com/")

    time.sleep(1)

    driver.execute_script("""
    var l = document.getElementsByClassName("v2-dialog style-scope ytd-consent-bump-v2-lightbox")[0];
    l.parentNode.removeChild(l);
    """)

    searchtext = "jump"

    # find the search bar using selenium find_element function
    driver.find_element_by_name("search_query").send_keys(searchtext)

    # clicking on the search button
    driver.find_element_by_css_selector(
    "#search-icon-legacy.ytd-searchbox").click()

    time.sleep(2)

    first_result_xpath = "//*[@id='video-title']"
    first_result = driver.find_elements_by_id("thumbnail")[1]


    url = first_result.get_attribute('href')
    print("###############", url)

    # driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[1])

    driver.get(url)

    time.sleep(1.3)

    driver.execute_script("""
    var l = document.getElementsByClassName("v2-dialog style-scope ytd-consent-bump-v2-lightbox")[0];
    l.parentNode.removeChild(l);
    """)

    time.sleep(2)

    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) #hits space

    time.sleep(15)

