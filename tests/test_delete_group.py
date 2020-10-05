# -*- coding: utf-8 -*-
from model.group_m import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Тестовая группа для проверки метода удаления",
                               header="Задание №9", footer="Футер задания №1"))
    app.group.delete_first_group()
