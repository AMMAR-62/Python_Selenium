# 
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    # really easy to access and change elements.
    # locator = "q" #find the element with the value of q

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
    # don't worry about wait, hidden behind the scenes, we do not want to wait for that element
