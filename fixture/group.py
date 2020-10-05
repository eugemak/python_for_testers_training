

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

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
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def update_first_group(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
