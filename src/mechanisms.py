
def slow_scroll(driver, speed):
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, speed):
        driver.execute_script("window.scrollTo(0, {});".format(i))