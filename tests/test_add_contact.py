# -*- coding: utf-8 -*-
from model.contact_m import Contact


def test_add_user(app):
    old_users = app.contact.get_contacts_list(second_iteration=False)
    new_user = Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                       title="Driver", company="McLaren F1 Team", home_phone="000-000-00")
    app.contact.create_new_user(new_user)
    assert len(old_users) + 1 == app.contact.count()
    new_users = app.contact.get_contacts_list(second_iteration=False)
    old_users.append(new_user)
    assert sorted(old_users, key=Contact.user_id_or_max) == sorted(new_users, key=Contact.user_id_or_max)
