from mechanisms import open_new_tab, slow_scroll


def visit(driver):
    driver.get("https://en.wikipedia.org")
    slow_scroll(driver, 1)
    open_new_tab(driver)