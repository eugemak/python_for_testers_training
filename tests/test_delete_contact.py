# -*- coding: utf-8 -*-
from model.contact_m import Contact
from random import randrange
import random


# def test_delete_user(app):
#     new_user = Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
#                        title="Driver", company="McLaren F1 Team", home_phone="000-000-00")
#     if app.contact.count() == 0:
#         app.contact.create_new_user(new_user)
#     old_users = app.contact.get_contacts_list()
#     index = randrange(len(old_users))
#     app.contact.delete_user_by_index(index)
#     assert len(old_users) - 1 == app.contact.count()
#     new_users = app.contact.get_contacts_list()
#     old_users[index:index+1] = []
#     assert old_users == new_users


def test_delete_user_orm_check(app, orm, check_ui):
    new_user = Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                       title="Driver", company="McLaren F1 Team", home_phone="000-000-00")
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new_user(new_user)

    old_users = orm.get_contact_list()
    random_user = random.choice(old_users)
    app.contact.delete_user_by_id(random_user.user_id)
    assert len(old_users) - 1 == app.contact.count()
    new_users = orm.get_contact_list()
    old_users.remove(random_user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=Contact.user_id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.user_id_or_max)
