"""
https:://sites.google.com/a/chromium.org/chromedriver/downloads
PIP - package installer python - configured through pip are the modules in python.

chrome web driver
"""

from selenium import webdriver
PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
# driver.close() #closes the browser window.
print(driver.title) #get the title of the webpage that is open in the driver.
driver.quit() #quits and closes the whole browser.




