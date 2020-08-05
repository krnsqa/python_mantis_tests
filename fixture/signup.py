import re


class SignupHelper:

    def __init__(self, app):
        self.app = app


    def new_user(self, username, email, password):
        dw = self.app.dw
        dw.get(self.app.base_url + "/signup_page.php")
        dw.find_element_by_name("username").send_keys(username)
        dw.find_element_by_name("email").send_keys(email)
        dw.find_element_by_css_selector('input[type="Submit"]').click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        dw.get(url)
        dw.find_element_by_name("password").send_keys(password)
        dw.find_element_by_name("password_confirm").send_keys(password)
        dw.find_element_by_css_selector('input[value="Update User"]').click()


    def extract_confirmation_url(self, text):
        return re.search('http://.*$', text, re.MULTILINE).group(0)
