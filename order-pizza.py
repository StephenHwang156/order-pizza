import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://ginospizza.webordering.ca/")
  
username = browser.find_element_by_id("email user")
password = browser.find_element_by_id("pass")

# submit   = browser.find_element_by_id("loginbutton")
  
username.send_keys(config.USR)
password.send_keys(config.PW)

"""
results = browser.find_element_by_tag_name('button')
for x in results:
    print(results[x])

"""
password.send_keys(Keys.RETURN)
wait = WebDriverWait(browser, 5)

browser.find_elements_by_class("btn green").click()


try:
    page_loaded = wait.until_not(
    lambda browser: browser.current_url == login_page
    )
except TimeoutException:
    self.fail( "Loading timeout expired" )
  
self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)
