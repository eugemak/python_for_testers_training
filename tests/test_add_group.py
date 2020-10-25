# -*- coding: utf-8 -*-
from model.group_m import Group


# def test_add_group(app, data_groups):
#     group = data_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     a = app.group.count()
#     assert len(old_groups) + 1 == a
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)


def test_add_group1(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
