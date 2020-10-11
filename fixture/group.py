
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
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.return_to_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def update_first_group(self, group):
        wd = self.app.wd
        self.return_to_group_page()
        self.select_first_group()
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.return_to_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.return_to_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            group_id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, group_id=group_id))
        return groups
