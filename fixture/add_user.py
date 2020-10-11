from model.add_user_m import AddUser
from selenium.webdriver.support.ui import WebDriverWait


class AddUserHelper:

    def __init__(self, app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
        # if not wd.current_url.endswith("/"):
        #     wd.get("http://localhost/addressbook/")
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
        self.home_page()
        self.users_cache = None

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
        self.home_page()
        self.users_cache = None

    def delete_user(self):
        wd = self.app.wd
        self.home_page()
        self.select_user()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        WebDriverWait(wd, 5)
        self.home_page()
        self.users_cache = None

    def count(self):
        wd = self.app.wd
        self.home_page()
        return len(wd.find_elements_by_name("selected[]"))

    users_cache = None

    def get_users_list(self):
        if self.users_cache is None:
            wd = self.app.wd
            self.home_page()
            wd.get("http://localhost/addressbook/")
            wd.implicitly_wait(1)
            self.users_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                user_id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname_field = element.find_element_by_css_selector("tr[name='entry'] > td:nth-of-type(2)").text
                firstname_field = element.find_element_by_css_selector("tr[name='entry'] > td:nth-of-type(3)").text
                self.users_cache.append(AddUser(user_id=user_id, firstname=firstname_field, lastname=lastname_field))
        return list(self.users_cache)
