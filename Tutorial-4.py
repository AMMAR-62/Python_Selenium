from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# chain of actions, we do not need to perform it all at once
# we can use the .perform() method and perform it on conditions.

driver.implicitly_wait(5) #wait for five seconds before going to the next line.

cookie = driver.find_element_by_id("bigCookie") #this is for clicking on the cookie
cookie_count = driver.find_element_by_id("cookies") #this is for grabbing the current count.
items = [driver.find_element_by_id("productPrice"+ str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()
