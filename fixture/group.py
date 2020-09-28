

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.init_new_group()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        self.fill_the_group(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def init_new_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()

    def fill_the_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    # def check_group_is_true(self, group):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("groups").click()
    #     try:
    #         # wd.find_element_by_name("selected[]").click()
    #         wd.find_elements_by_name("selected[]").click()
    #     except NoSuchElementException:
    #         self.create(group)

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def update(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        self.fill_the_group(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
