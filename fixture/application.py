from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.dw = webdriver.Firefox()
        elif browser == "chrome":
            self.dw = webdriver.Chrome()
        elif browser == "ie":
            self.dw = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        #self.dw.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url


    def is_valid(self):
        try:
            self.dw.current_url
            return True
        except:
            return False


    def open_home_page(self):
        dw = self.dw
        dw.get(self.base_url)


    def destroy(self):
        self.dw.quit()
