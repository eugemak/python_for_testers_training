
from model.group_m import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.init_new_group()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        wd.implicitly_wait(1)
        self.group_cache = None

    def init_new_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()

    def fill_group_form(self, group):
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, group_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(group_field_name).click()
            wd.find_element_by_name(group_field_name).clear()
            wd.find_element_by_name(group_field_name).send_keys(text)

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.return_to_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def update_first_group(self, group):
        self.update_group_by_index(group, index=0)

    def update_group_by_index(self, group, index):
        wd = self.app.wd
        self.return_to_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.return_to_group_page()
            wd.implicitly_wait(1)
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, group_id=group_id))
        return list(self.group_cache)
