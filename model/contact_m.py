from sys import maxsize


class Contact:

    def __init__(self, user_id=None, firstname=None, middlename=None, lastname=None,
                 title=None, company=None, nickname=None,
                 home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None,
                 email=None, email2=None, email3=None, homepage=None, deprecated=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.company = company
        self.nickname = nickname
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.user_id = user_id
        self.deprecated = deprecated
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.user_id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.user_id is None or other.user_id is None or self.user_id == other.user_id and self.firstname == other.firstname and self.lastname == other.lastname

    def user_id_or_max(self):
        if self.user_id:
            return int(self.user_id)
        else:
            return maxsize
