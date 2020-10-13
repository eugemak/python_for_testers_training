# -*- coding: utf-8 -*-
from model.add_user_m import AddUser
from random import randrange


def test_update_user(app):
    if app.add_user.count() == 0:
        app.add_user.create_new_user(AddUser(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                             title="Driver", company="McLaren F1 Team", home_phone="000-000-00"))

    # получаем список пользователей до редактирования
    old_users = app.add_user.get_users_list()

    # данные для редактирования
    edit_user_data = AddUser(firstname="Carlos (edit)", middlename="Карлович (edit)", lastname="Sainz (edit)",
                             title="Driver", company="Ferrari F1 Team (in 2021)", home_phone="000-000-00")

    # индекс = случайное число из общего количества пользователей
    index = randrange(1, len(old_users))

    # добавляем id редактируемого пользователя (index) в данные для редактирования
    edit_user_data.user_id = old_users[index].user_id

    # редактируем данные пользователя
    app.add_user.edit_user(edit_user_data, index)
    assert len(old_users) == app.add_user.count()

    # получаем данные после редактирования
    edited_users = app.add_user.get_users_list()

    # присваиваем старой записи новые данные
    old_users[index] = edit_user_data

    # сортировка
    a = sorted(old_users, key=AddUser.user_id_or_max)
    b = sorted(edited_users, key=AddUser.user_id_or_max)
    assert a == b
