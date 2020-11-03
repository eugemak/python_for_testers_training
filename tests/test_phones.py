from model.contact_m import Contact
from random import randrange
import re
from random import randrange


def test_phones_on_home_page(app):
    # получаем случайное значение для индекса
    all_contacts = app.contact.count()
    index = randrange(0, all_contacts)
    # print('    '+str(index))
    # index = 1

    # contact_from_home_page = app.contact.get_contacts_list(second_iteration=False)[index]
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def test_phones_on_home_page_orm_check(app, orm):

    # Получаем данные из интерфейса и бд
    contacts_from_home_page = app.contact.get_contacts_list()
    contacts_from_db = orm.get_contact_list_extended()
    assert contacts_from_home_page

    # Данные по телефонам смёрживаем в одну ячейку
    for item in contacts_from_db:
        item.all_phones_from_home_page = merge_phones_like_on_home_page_from_db(item)

    # Данные по емейлам смёрживаем в одну ячейку
    for item in contacts_from_db:
        item.all_emails_from_home_page = merge_emails_like_on_home_page_from_db(item)

    # Создаём очищенный список для контактов из бд
    clean_contacts_db = []
    for item in contacts_from_db:
        a = (item.user_id, item.firstname, item.lastname, item.all_emails_from_home_page, item.all_phones_from_home_page)
        clean_contacts_db.append(a)

    # Создаём очищенный список для контактов из интерфейса
    clean_contacts_ui = []
    for item in contacts_from_home_page:
        a = (item.user_id, item.firstname, item.lastname, item.all_emails_from_home_page, item.all_phones_from_home_page)
        clean_contacts_ui.append(a)

    assert sorted(clean_contacts_db) == sorted(clean_contacts_ui)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page_from_db(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page_from_db(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
