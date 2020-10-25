import random
import string
import jsonpickle
import os.path
import getopt
import sys
from model.contact_m import Contact


# добавляем возможность использовать опции в командной строке для генерации данных
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# фунция для создания случайной последовательности значений
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# форма для создания объекта (тестовые данные) на основе рандомного значения
testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), title=random_string("title", 10),
            company=random_string("company", 10), home_phone=random_string("company", 10),
            mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            secondary_phone=random_string("secondary_phone", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(3)
]

# Запись данных в json файл data/contacts.json
root_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(root_path, "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
