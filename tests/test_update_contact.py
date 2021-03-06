# -*- coding: utf-8 -*-
from model.contact_m import Contact
from random import randrange
import random

# def test_update_user(app):
#     if app.contact.count() == 0:
#         app.contact.create_new_user(Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
#                                             title="Driver", company="McLaren F1 Team", home_phone="000-000-00",
#                                             mobile_phone="random_mobile_phone", work_phone="random_work_phone",
#                                             secondary_phone="random_secondary_phone", email="random_email",
#                                             email2="random_email2", email3="random_email3"))
#
#     # получаем список пользователей до редактирования
#     old_users = app.contact.get_contacts_list()
#
#     # данные для редактирования
#     edit_user_data = Contact(firstname="Carlos (edit)", middlename="Карлович (edit)", lastname="Sainz (edit)",
#                              title="Driver", company="Ferrari F1 Team (in 2021)", home_phone="000-000-00",
#                              mobile_phone="random_mobile_phone", work_phone="random_work_phone",
#                              secondary_phone="random_secondary_phone", email="random_email",
#                              email2="random_email2", email3="random_email3")
#
#     # индекс = случайное число из общего количества пользователей
#     index = randrange(1, len(old_users))
#     print('   ' + str(index))
#
#     # добавляем id редактируемого пользователя (index) в данные для редактирования
#     edit_user_data.user_id = old_users[index-1].user_id
#
#     # редактируем данные пользователя
#     app.contact.edit_user(edit_user_data, index)
#     assert len(old_users) == app.contact.count()
#
#     # получаем данные после редактирования
#     edited_users = app.contact.get_contacts_list()
#
#     # присваиваем старой записи новые данные
#     old_users[index-1] = edit_user_data
#
#     # сортировка
#     a = sorted(old_users, key=Contact.user_id_or_max)
#     b = sorted(edited_users, key=Contact.user_id_or_max)
#     assert a == b


def test_update_user_orm_check(app, orm, check_ui):
    # получаем список пользователей до редактирования
    old_users = orm.get_contact_list()
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new_user(Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                            title="Driver", company="McLaren F1 Team", home_phone="000-000-00",
                                            mobile_phone="random_mobile_phone", work_phone="random_work_phone",
                                            secondary_phone="random_secondary_phone", email="random_email",
                                            email2="random_email2", email3="random_email3"))

    # данные для редактирования
    edit_user_data = Contact(firstname="Carlos (edit)", middlename="Карлович (edit)", lastname="Sainz (edit)",
                             title="Driver", company="Ferrari F1 Team (in 2021)", home_phone="000-000-00",
                             mobile_phone="random_mobile_phone", work_phone="random_work_phone",
                             secondary_phone="random_secondary_phone", email="random_email",
                             email2="random_email2", email3="random_email3")

    # выбираем случайного пользователя
    random_user = random.choice(old_users)
    edit_user_data.user_id = random_user.user_id

    # редактируем данные пользователя
    app.contact.edit_user_by_id(edit_user_data, random_user.user_id)

    # получаем данные после редактирования
    edited_users = orm.get_contact_list()
    assert edited_users
    # присваиваем старой записи новые данные
    for item in old_users:
        if item.user_id == random_user.user_id:
            item.firstname = edit_user_data.firstname
            item.lastname = edit_user_data.lastname

    # сортировка
    a = sorted(old_users, key=Contact.user_id_or_max)
    b = sorted(edited_users, key=Contact.user_id_or_max)
    assert a == b
