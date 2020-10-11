# -*- coding: utf-8 -*-
from model.group_m import Group
from random import randrange


def test_update_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Тестовая группа для проверки метода обновления данных в группе",
                               header="Задание №9", footer="Футер задания №1"))
    group = Group(name="Группа для проверки возможности изменения",
                  header="Задание №7 update check",
                  footer="Футер задания №7 update check")
    index = randrange(len(old_groups))
    group.group_id = old_groups[index].group_id
    app.group.update_group_by_index(group, index)

    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
