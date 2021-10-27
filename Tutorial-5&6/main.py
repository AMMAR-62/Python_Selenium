import unittest
from selenium import webdriver
import page
# for separating the test cases, we create a new test case.
class PythonOrgSearch(unittest.TestCase): 
    PATH="C:\Program Files (x86)\chromedriver.exe"
    # some things are inherited, which will give some methods which helps us to perform some test cases.
    def setUp(self):
        # for each test case it runs one time, so we make the initial setup instructions here.
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("http://www.python.org")

    def test_example(self):
        # this will run when we run the unit test.
        print("test")
        assert True #whether this test case failed or passed.
    
    # def test_title(self):
    #     mainPage = page.MainPage()
    #     assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    
    def tearDown(self):
        # once everything is done, then run this.
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
