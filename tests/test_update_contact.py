# -*- coding: utf-8 -*-
from model.contact_m import Contact
from random import randrange


def test_update_user(app):
    if app.contact.count() == 0:
        app.contact.create_new_user(Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                             title="Driver", company="McLaren F1 Team", home_phone="000-000-00"))

    # получаем список пользователей до редактирования
    old_users = app.contact.get_contacts_list(second_iteration=False)

    # данные для редактирования
    edit_user_data = Contact(firstname="Carlos (edit)", middlename="Карлович (edit)", lastname="Sainz (edit)",
                             title="Driver", company="Ferrari F1 Team (in 2021)", home_phone="000-000-00")

    # индекс = случайное число из общего количества пользователей
    index = randrange(1, len(old_users))
    print('   ' + str(index))
    # добавляем id редактируемого пользователя (index) в данные для редактирования
    edit_user_data.user_id = old_users[index].user_id

    # редактируем данные пользователя
    app.contact.edit_user(edit_user_data, index)
    assert len(old_users) == app.contact.count()

    # получаем данные после редактирования
    edited_users = app.contact.get_contacts_list(second_iteration=True)

    # присваиваем старой записи новые данные
    old_users[index] = edit_user_data

    # сортировка
    a = sorted(old_users, key=Contact.user_id_or_max)
    b = sorted(edited_users, key=Contact.user_id_or_max)
    assert a == b