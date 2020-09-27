# -*- coding: utf-8 -*-
from model.group_m import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="First", header="Задание №1", footer="Футер задания №1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    # app.group.check_group_is_true(Group(name="First", header="Задание №1", footer="Футер задания №1"))
    app.group.delete()
    app.session.logout()


def test_update_group(app):
    app.session.login(username="admin", password="secret")
    # app.group.check_group_is_true(Group(name="First", header="Задание №1", footer="Футер задания №1"))
    app.group.update(Group(name="First", header="Задание №7 update check", footer="Футер задания №7 update check"))
    app.session.logout()
