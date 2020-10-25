import random
import string
import jsonpickle
import os.path
import getopt
import sys
from model.group_m import Group


# добавляем возможность использовать опции в командной строке для генерации данных
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# + string.punctuation
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]

# сохранение тестовых данных в файл. настройки указываются в командной строке или
# в pycharm -> edit configurations -> parametrs ->
# -n 3 -f data/your_file.json
# по умолчанию файл будет f = "data/groups.json"

root_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(root_path, "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
