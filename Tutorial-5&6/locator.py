# any way that we locate an element, it is easy to change the id, class or something.
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass
