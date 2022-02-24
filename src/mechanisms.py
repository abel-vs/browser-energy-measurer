from random import randint
import time


def slow_scroll(driver, speed):
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, speed):
        driver.execute_script("window.scrollTo(0, {});".format(i))

def immediate_scroll(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

def open_new_tab(driver):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1]) # Switch focus to newest tab

def wait(duration):
    time.sleep(duration)

# Waits a random time between and 3 and 5 seconds, to avoid bot detection.
def random_wait():
    time.sleep(randint(1,2))