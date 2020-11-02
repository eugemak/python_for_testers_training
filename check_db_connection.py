# import pymysql.cursors
from fixture.orm import ORMFixture
from model.group_m import Group
from model.contact_m import Contact
from pymysql.converters import decoders

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     l = db.get_contacts_in_group(Group(group_id="181"))
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

# try:
#     l = db.get_group_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass
