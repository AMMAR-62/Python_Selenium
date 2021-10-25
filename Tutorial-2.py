"""
1) Search for the search bar.
2) Search for something in it.
3) Grab the search results and the changes in the page we notice.
"""
# we can search the element with the help of id, class, name or tag.
# the general hierarchy is id> name> class> tag.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #this is for the support of keys
from selenium.webdriver.common.by import By #this is to get elements by id, class, tag, etc.
from selenium.webdriver.support.ui import WebDriverWait #this is to apply some conditions and wait to check if those conditions exists or not.
from selenium.webdriver.support import expected_conditions as EC #this is to make some conditions and check if epxected conditions are met.
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
# print(driver.title)
search = driver.find_element_by_name("s") #finding the element by name of the element which is s
search.send_keys("test") # equivalent to typing "test" in the search bar.
search.send_keys(Keys.RETURN) # equivalent to pressing the enter key.

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text) #printing the main
    articles  = main.find_elements_by_tag_name("article")
    for article in articles:
        header_summary = article.find_element_by_class_name("entry-summary")
        print(header_summary.text, end="\n\n")
    time.sleep(5)
except:
    driver.quit()


# print(driver.page_source) #equivalent to printing the page_source code in the terminal.
# main = driver.find_element_by_id("main")