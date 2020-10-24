# -*- coding: utf-8 -*-
from model.contact_m import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), title=random_string("title", 10),
            company=random_string("company", 10), home_phone=random_string("company", 10),
            mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            secondary_phone=random_string("secondary_phone", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, contact):
    old_users = app.contact.get_contacts_list()
    app.contact.create_new_user(contact)
    assert len(old_users) + 1 == app.contact.count()
    new_users = app.contact.get_contacts_list()
    old_users.append(contact)
    assert sorted(old_users, key=Contact.user_id_or_max) == sorted(new_users, key=Contact.user_id_or_max)
