# -*- coding: utf-8 -*-
from model.add_user_m import AddUser


def test_update_user(app):
    old_users = app.add_user.get_users_list()
    if app.add_user.count() == 0:
        app.add_user.create_new_user(AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                             title="Driver", company="McLaren F1 Team", home_phone="000-000-00"))

    edit_user_data = AddUser(firstname="Carlos (edit)", middlename="Карлович (edit)", lastname="Sainz (edit)",
                             title="Driver", company="Ferrari F1 Team (in 2021)", home_phone="000-000-00")
    edit_user_data.user_id = old_users[0].user_id

    # редактируем данные пользователя
    app.add_user.select_user()
    app.add_user.init_edit_user()
    app.add_user.edit_user(edit_user_data)

    # получаем данные после редактирования
    edited_user = app.add_user.get_users_list()
    assert len(old_users) == len(edited_user)
    old_users[0] = edit_user_data
    assert sorted(old_users, key=AddUser.user_id_or_max) == sorted(edited_user, key=AddUser.user_id_or_max)
