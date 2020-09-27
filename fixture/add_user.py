

class AddUserHelper:

    def __init__(self, app):
        self.app = app

    def init_new_user(self, app):
        app.wd.find_element_by_link_text("add new").click()

    def create_new_user(self, app, add_user):
        app.wd.find_element_by_name("firstname").click()
        app.wd.find_element_by_name("firstname").clear()
        app.wd.find_element_by_name("firstname").send_keys(add_user.firstname)
        app.wd.find_element_by_name("middlename").click()
        app.wd.find_element_by_name("middlename").clear()
        app.wd.find_element_by_name("middlename").send_keys(add_user.middlename)
        app.wd.find_element_by_name("lastname").click()
        app.wd.find_element_by_name("lastname").clear()
        app.wd.find_element_by_name("lastname").send_keys(add_user.lastname)
        app.wd.find_element_by_name("title").clear()
        app.wd.find_element_by_name("title").send_keys(add_user.title)
        app.wd.find_element_by_name("company").click()
        app.wd.find_element_by_name("company").clear()
        app.wd.find_element_by_name("company").send_keys(add_user.company)
        app.wd.find_element_by_name("home").click()
        app.wd.find_element_by_name("home").clear()
        app.wd.find_element_by_name("home").send_keys(add_user.home_phone)
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
