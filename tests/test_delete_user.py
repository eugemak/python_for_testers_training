# -*- coding: utf-8 -*-
from model.add_user_m import AddUser


def test_delete_user(app):
    if app.add_user.count() == 0:
        app.add_user.create_new_user(AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                             title="Driver", company="McLaren F1 Team", home_phone="000-000-00"))
    app.add_user.delete_user()
