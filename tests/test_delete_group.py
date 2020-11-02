# -*- coding: utf-8 -*-
from model.group_m import Group
from random import randrange
import random

#
# def test_delete_some_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Тестовая группа для проверки метода удаления",
#                                header="Задание №9", footer="Футер задания №1"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     app.group.delete_group_by_index(index)
#
#     assert len(old_groups) - 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index:index+1] = []
#     assert old_groups == new_groups
#
#
# def test_delete_some_group_db_assert(app, db, check_ui):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="Тестовая группа для проверки метода удаления",
#                                header="Задание №9", footer="Футер задания №1"))
#     old_groups = db.get_group_list()
#     group = random.choice(old_groups)
#     app.group.delete_group_by_id(group.group_id)
#     assert len(old_groups) - 1 == app.group.count()
#     new_groups = db.get_group_list()
#     old_groups.remove(group)
#     assert old_groups == new_groups
#     if check_ui:
#         assert sorted(new_groups, key=Group.group_id_or_max) == sorted(app.group.get_group_list(), key=Group.group_id_or_max)


def test_delete_some_group_db_orm_assert(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Тестовая группа для проверки метода удаления",
                               header="Задание №9", footer="Футер задания №1"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.group_id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = orm.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.group_id_or_max) == sorted(app.group.get_group_list(), key=Group.group_id_or_max)
