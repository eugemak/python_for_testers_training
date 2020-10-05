from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class AddUserHelper:

    def __init__(self, app):
        self.app = app

    def go_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/"):
            wd.find_element_by_link_text("home").click()

    def init_new_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_user_form(self, add_user):
        wd = self.app.wd
        self.user_change_field("firstname", add_user.firstname)
        self.user_change_field("middlename", add_user.middlename)
        self.user_change_field("lastname", add_user.lastname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(add_user.title)
        self.user_change_field("company", add_user.company)
        self.user_change_field("home", add_user.home_phone)

    def user_change_field(self, user_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(user_field_name).click()
            wd.find_element_by_name(user_field_name).clear()
            wd.find_element_by_name(user_field_name).send_keys(text)

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
        self.select_user()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_home_page()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
