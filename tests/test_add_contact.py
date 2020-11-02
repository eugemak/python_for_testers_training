# -*- coding: utf-8 -*-
from model.contact_m import Contact


# загрузка данных из отдельного модуля
def test_add_user(app, data_contacts):
    contact = data_contacts
    old_users = app.contact.get_contacts_list()
    app.contact.create_new_user(contact)
    assert len(old_users) + 1 == app.contact.count()
    new_users = app.contact.get_contacts_list()
    old_users.append(contact)
    assert sorted(old_users, key=Contact.user_id_or_max) == sorted(new_users, key=Contact.user_id_or_max)


# загрузка данных из json-файла
def test_add_user2(app, json_contacts):
    contact = json_contacts
    old_users = app.contact.get_contacts_list()
    app.contact.create_new_user(contact)
    assert len(old_users) + 1 == app.contact.count()
    new_users = app.contact.get_contacts_list()
    old_users.append(contact)
    assert sorted(old_users, key=Contact.user_id_or_max) == sorted(new_users, key=Contact.user_id_or_max)


# сравнение через данные из бд
def test_add_user_orm_check(app, orm, check_ui, json_contacts):
    contact = json_contacts
    old_users = orm.get_contact_list()
    app.contact.create_new_user(contact)
    assert len(old_users) + 1 == app.contact.count()
    new_users = orm.get_contact_list()
    old_users.append(contact)
    assert sorted(old_users, key=Contact.user_id_or_max) == sorted(new_users, key=Contact.user_id_or_max)
    if check_ui:
        assert sorted(new_users, key=Contact.user_id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.user_id_or_max)
