# -*- coding: utf-8 -*-
from model.add_user_m import AddUser


def test_add_user(app):
    old_users = app.add_user.get_users_list()
    new_user = AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                       title="Driver", company="McLaren F1 Team", home_phone="000-000-00")
    app.add_user.create_new_user(new_user)
    new_users = app.add_user.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(new_user)
    assert sorted(old_users, key=AddUser.user_id_or_max) == sorted(new_users, key=AddUser.user_id_or_max)
