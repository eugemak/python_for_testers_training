# -*- coding: utf-8 -*-
from model.group_m import Group


def test_add_group(app):
    app.group.create(Group(name="First", header="Задание №1", footer="Футер задания №1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
