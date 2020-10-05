# -*- coding: utf-8 -*-
from model.group_m import Group


def test_add_group(app):
    app.group.create(Group(name="First", header="Задание №1", footer="Футер задания №1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


def test_delete_group(app):
    app.group.delete_first_group()


def test_update_group(app):
    app.group.update_first_group(Group(name="First", header="Задание №7 update check",
                                       footer="Футер задания №7 update check"))
