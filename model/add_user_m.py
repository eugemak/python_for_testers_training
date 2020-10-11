from sys import maxsize


class AddUser:

    def __init__(self, user_id=None, firstname=None, middlename=None, lastname=None,
                 title=None, company=None, home_phone=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.company = company
        self.home_phone = home_phone
        self.user_id = user_id

    def __repr__(self):
        return "%s:%s:%s" % (self.user_id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.user_id is None or other.user_id is None or self.user_id == other.user_id) and \
               self.firstname == other.firstname and self.lastname == other.lastname

    def user_id_or_max(self):
        if self.user_id:
            return int(self.user_id)
        else:
            return maxsize
