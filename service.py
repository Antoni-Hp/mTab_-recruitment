from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Service():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')

    def website(self, website):
        self.driver.get(website)

    def getTitle(self):
        return self.driver.title

    def getFindElementbyId(self, id):
        return self.driver.find_element_by_id(id)

    def getFindElementbySelector(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def getFindElementbyName(self, name):
        return self.driver.find_element_by_name(name)

    def getFindElementsbyId(self, id):
        return self.driver.find_elemens_by_id(id)

    def getFindElementsbySelector(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    def getFindElementsbyName(self, name):
        return self.driver.find_elements_by_name(name)

    def getAkcept(self, value):
        return value.send_keys(Keys.RETURN)

    def onPage_source_not(self, value):
        assert value not in self.driver.page_source

    def onPage_source_is(self, value):
        assert value in self.driver.page_source

    def sesionClose(self):
        self.driver.close()