from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    # for each element, define some class, locate the GO_BUTTON
    locator = "q"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()
    # this is creating a descriptor.


    def is_title_matches(self):
        return ("Python" in self.driver.title)
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON) #unpacking the tuple
        element.click()
    
class SearchResultPage(BasePage):
    
    def is_results_found(self):
        return ("No results found." not in self.driver.page_source)
