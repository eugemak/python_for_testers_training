
import pymysql.cursors
from model.group_m import Group
from model.contact_m import Contact


class DbFixture:

    def __init__(self, host=None, database=None, user=None, password=None):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(group_id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated = 0")
            for row in cursor:
                (user_id, firstname, lastname) = row
                list.append(Contact(user_id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    # cursor.execute("select id, firstname, middlename, lastname, company, title, home, mobile, work, \
    #                            email, email2, email3 from addressbook")
    # for row in cursor:
    #     (user_id, firstname, middlename, lastname, title, company, home, mobile, work, email, email2, email3) = row
    #     list.append(Contact(user_id=id, firstname=firstname, middlename=middlename,
    #                         lastname=lastname, title=title, company=company, home_phone=home,
    #                         mobile_phone=mobile, work_phone=work,
    #                         email=email, email2=email2, email3=email3))

    def destroy(self):
        self.connection.close()
