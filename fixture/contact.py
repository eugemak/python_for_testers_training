from model.contact_m import Contact
from selenium.webdriver.support.ui import WebDriverWait
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
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
        self.select_user_by_index(0)

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def init_edit_user(self, index):
        wd = self.app.wd
        self.home_page()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[" + str(index) + "]").click()

    def edit_user(self, add_user, index):
        wd = self.app.wd
        self.init_edit_user(index)
        self.fill_user_form(add_user)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.users_cache = None

    def delete_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        self.select_user_by_index(index)
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

    def get_user_from_table(self):
        wd = self.app.wd
        self.home_page()
        self.users_cache = []
        for element in wd.find_elements_by_name("entry"):
            user_id = element.find_element_by_name("selected[]").get_attribute("value")
            cells = element.find_elements_by_tag_name("td")
            firstname_field = cells[2].text
            lastname_field = cells[1].text
            # all_phones = cells[5].text.splitlines()
            all_phones = cells[5].text
            all_emails = cells[4].text
            self.users_cache.append(Contact(firstname=firstname_field, lastname=lastname_field, user_id=user_id,
                                            all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))

    def get_contacts_list(self):
        if self.users_cache is None:
            self.get_user_from_table()
        return list(self.users_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)

        user_id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(user_id=user_id, firstname=firstname, middlename=middlename, lastname=lastname,
                       nickname=nickname, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone,
                       email=email, email2=email2, email3=email3, homepage=homepage)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)
