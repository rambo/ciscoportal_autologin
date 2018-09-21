#!/usr/bin/env python3
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# wait fors stolen from http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html
def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise RuntimeError(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )

class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded)


def login(username, password):
    driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
    driver.get("http://www.google.com")

    if 'Google' in driver.title:
        # Connection ok
        print("Not captured, returning early")
        driver.close()
        return True

    print("Logging in")
    username_input = driver.find_element_by_name("username")
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(password)
    with wait_for_page_load(driver):
        password_input.send_keys(Keys.RETURN)

    ok = False
    if 'Google' in driver.title:
        # Connection ok
        print("Login OK")
        ok = True
    else:
        print("Something went wrong, saving screenshot")
        driver.save_screenshot('screenshot.png')

    driver.close()
    return ok


def usage(name):
    print(""""
USage:

    xvfb-run {} "username" "password"
""")

if __name__ == '__main__'
    if len(sys.argv) < 3:
        usage(__file__)
        sys.exit(1)
    if not login(sys.argv[1], sys.argv[2]):
        sys.exit(1)
    sys.exit(0)
