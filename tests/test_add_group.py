# -*- coding: utf-8 -*-
from model.group_m import Group


# # Загрузка при использовании данных из отдельного модуля
# def test_add_group(app, data_groups):
#     group = data_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     a = app.group.count()
#     assert len(old_groups) + 1 == a
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
#
#
# # Загрузка при использовании данных из сгенерированного json-файла
# def test_add_group_from_json(app, json_groups):
#     group = json_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
#
#
# # Сравнение с данными из БД
# def test_add_group_db_assert(app, db, json_groups):
#     group = json_groups
#     old_groups = db.get_group_list()
#     app.group.create(group)
#     new_groups = db.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)


# Сравнение с данными из БД через ORM
def test_add_group_db_orm_assert(app, orm, check_ui, json_groups):
    group = json_groups
    old_groups = orm.get_group_list()
    app.group.create(group)
    new_groups = orm.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.group_id_or_max) == sorted(app.group.get_group_list(), key=Group.group_id_or_max)
