# -*- coding: utf-8 -*-
from model.add_user_m import AddUser


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.add_user.init_new_user()
    app.add_user.create_new_user(AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                              title="Driver", company="McLaren F1 Team", home_phone="000-000-00"))
    app.session.logout()


def test_edit_user(app):
    app.session.login(username="admin", password="secret")
    app.add_user.select_user()
    app.add_user.init_edit_user()
    app.add_user.edit_user(AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                   title="Driver", company="Ferrai F1 Team (in 2021)", home_phone="000-000-00"))
    app.session.logout()


def test_delete_user(app):
    app.session.login(username="admin", password="secret")
    app.add_user.select_user()
    app.add_user.delete_user()
    app.session.logout()
