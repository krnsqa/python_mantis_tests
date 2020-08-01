

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        dw = self.app.dw
        self.app.open_home_page()
        dw.find_element_by_name("username").send_keys(username)
        dw.find_element_by_name("password").send_keys(password)
        dw.find_element_by_css_selector('input[type="Submit"]').click()


    def logout(self):
        dw = self.app.dw
        dw.find_element_by_link_text("Logout").click()
        #dw.find_element_by_name("user")


    def is_logged_in(self):
        dw = self.app.dw
        return len(dw.find_elements_by_link_text("Logout")) > 0


    def is_logged_in_as(self, username):
        dw = self.app.dw
        return self.get_logged_user() == username


    def get_logged_user(self):
        dw = self.app.dw
        return dw.find_element_by_css_selector("td.login-info-left span").text


    def ensure_logout(self):
        dw = self.app.dw
        if self.is_logged_in():
            self.logout()


    def ensure_login(self, username, password):
        dw = self.app.dw
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)


