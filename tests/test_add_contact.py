# -*- coding: utf-8 -*-
from model.contact_m import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), title=random_string("title", 10),
            company=random_string("company", 10), home_phone=random_string("company", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, contact):
    old_users = app.contact.get_contacts_list(second_iteration=False)
    app.contact.create_new_user(contact)
    assert len(old_users) + 1 == app.contact.count()
    new_users = app.contact.get_contacts_list(second_iteration=False)
    old_users.append(contact)
    assert sorted(old_users, key=Contact.user_id_or_max) == sorted(new_users, key=Contact.user_id_or_max)


# def test_add_user(app):
#     old_users = app.contact.get_contacts_list(second_iteration=False)
#     new_user = Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
#                        title="Driver", company="McLaren F1 Team", home_phone="000-000-00")
#     app.contact.create_new_user(new_user)
#     assert len(old_users) + 1 == app.contact.count()
#     new_users = app.contact.get_contacts_list(second_iteration=False)
#     old_users.append(new_user)
#     assert sorted(old_users, key=Contact.user_id_or_max) == sorted(new_users, key=Contact.user_id_or_max)


