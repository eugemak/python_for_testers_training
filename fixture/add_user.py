from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class AddUserHelper:

    def __init__(self, app):
        self.app = app

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def init_new_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_user_form(self, add_user):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(add_user.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(add_user.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(add_user.lastname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(add_user.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(add_user.company)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(add_user.home_phone)

    def create_new_user(self, add_user):
        wd = self.app.wd
        self.init_new_user()
        self.fill_user_form(add_user)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.go_to_home_page()

    def select_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def init_edit_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def edit_user(self, add_user):
        wd = self.app.wd
        self.fill_user_form(add_user)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.go_to_home_page()

    def delete_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_home_page()
