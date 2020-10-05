# -*- coding: utf-8 -*-
from model.group_m import Group


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Тестовая группа для проверки метода обновления данных в группе",
                               header="Задание №9", footer="Футер задания №1"))
    app.group.update_first_group(Group(name="Группа для проверки возможности изменения",
                                       header="Задание №7 update check",
                                       footer="Футер задания №7 update check"))


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Тестовая группа для проверки метода обновления данных в группе",
                               header="Задание №9", footer="Футер задания №1"))
    app.group.update_first_group(Group(header="Изменили только header"))
