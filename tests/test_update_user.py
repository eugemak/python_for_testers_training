# -*- coding: utf-8 -*-
from model.add_user_m import AddUser


def test_update_user(app):
    if app.add_user.count() == 0:
        app.add_user.create_new_user(AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                             title="Driver", company="McLaren F1 Team", home_phone="000-000-00"))
    app.add_user.select_user()
    app.add_user.init_edit_user()
    app.add_user.edit_user(AddUser(firstname="Carlos (edit)", middlename="Карлович (edit)", lastname="Sainz (edit)",
                                   title="Driver", company="Ferrari F1 Team (in 2021)", home_phone="000-000-00"))
