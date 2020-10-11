# -*- coding: utf-8 -*-
from model.group_m import Group


def test_update_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Тестовая группа для проверки метода обновления данных в группе",
                               header="Задание №9", footer="Футер задания №1"))
    group = Group(name="Группа для проверки возможности изменения",
                  header="Задание №7 update check",
                  footer="Футер задания №7 update check")
    group.group_id = old_groups[0].group_id
    app.group.update_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
