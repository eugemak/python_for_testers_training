# -*- coding: utf-8 -*-
from model.add_user_m import AddUser


def test_delete_user(app):
    new_user = AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                       title="Driver", company="McLaren F1 Team", home_phone="000-000-00")
    if app.add_user.count() == 0:
        app.add_user.create_new_user(new_user)
    old_users = app.add_user.get_users_list()
    app.add_user.delete_user()
    assert len(old_users) - 1 == app.add_user.count()
    new_users = app.add_user.get_users_list()
    old_users[0:1] = []
    assert old_users == new_users
