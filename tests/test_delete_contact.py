# -*- coding: utf-8 -*-
from model.contact_m import Contact
from random import randrange


def test_delete_user(app):
    new_user = Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                       title="Driver", company="McLaren F1 Team", home_phone="000-000-00")
    if app.contact.count() == 0:
        app.contact.create_new_user(new_user)
    old_users = app.contact.get_contacts_list(second_iteration=False)
    index = randrange(len(old_users))
    app.contact.delete_user_by_index(index)
    assert len(old_users) - 1 == app.contact.count()
    new_users = app.contact.get_contacts_list(second_iteration=False)
    old_users[index:index+1] = []
    assert old_users == new_users
