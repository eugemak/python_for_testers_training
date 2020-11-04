# -*- coding: utf-8 -*-
from model.contact_m import Contact
from model.group_m import Group
import random
import re


def clear(s):
    return re.sub("[() -]", "", s)


def test_move_user_to_group(app, db, orm):
    all_users = orm.get_contact_list()
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new_user(Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                            title="Driver", company="McLaren F1 Team", home_phone="000-000-00",
                                            mobile_phone="random_mobile_phone", work_phone="random_work_phone",
                                            secondary_phone="random_secondary_phone", email="random_email",
                                            email2="random_email2", email3="random_email3"))

    all_groups = orm.get_group_list()
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Тестовая группа для проверки метода обновления данных в группе",
                               header="Задание №9", footer="Футер задания №1"))

    # выбираем случайного пользователя
    random_user = random.choice(all_users)
    user_id = random_user.user_id

    random_group = random.choice(all_groups)
    group_id = random_group.group_id

    # Добавляем пользователя в группу
    app.contact.add_contact_to_group_by_id(user_id, group_id)

    contacts_in_group = db.get_contact_in_group(user_id, group_id) # Список пользователей в группах через PyMySql
    # contacts_in_group = orm.get_contacts_in_group(Group(group_id=group_id)) # Список пользователей в группах через ORM
    assert contacts_in_group


def test_delete_user_from_group(app, db, orm):
    # Проверка, что есть хотя бы один пользователь и есть группа. Если нет, то создаём. Добавляем пользователя в группу
    if len(db.get_all_users_in_all_groups()) == 0:

        all_users = orm.get_contact_list()
        if len(orm.get_contact_list()) == 0:
            app.contact.create_new_user(Contact(firstname="Carlos", middlename="Карлович", lastname="Sainz",
                                                title="Driver", company="McLaren F1 Team", home_phone="000-000-00",
                                                mobile_phone="random_mobile_phone", work_phone="random_work_phone",
                                                secondary_phone="random_secondary_phone", email="random_email",
                                                email2="random_email2", email3="random_email3"))

        all_groups = orm.get_group_list()
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="Тестовая группа для проверки метода обновления данных в группе",
                                   header="Задание №9", footer="Футер задания №1"))

        # выбираем случайного пользователя из существующих
        random_user = random.choice(all_users)
        user_id = random_user.user_id

        random_group = random.choice(all_groups)
        group_id = random_group.group_id

        # добавляем в группу
        app.contact.add_contact_to_group_by_id(user_id, group_id)

    # Получаем user_id и group_id из таблицы address_in_groups
    all_users_in_groups = db.get_all_users_in_all_groups()
    user_id = all_users_in_groups[0].user_id
    group_id = all_users_in_groups[0].group_id

    # Удаляем пользователя из группы
    app.contact.delete_user_from_group(user_id, group_id)

    contacts_in_group = db.get_contact_in_group(user_id, group_id) # Список пользователей в группах через PyMySql
    # contacts_in_group = orm.get_contacts_in_group(Group(group_id=group_id)) # Список пользователей в группах через ORM
    assert contacts_in_group == []
