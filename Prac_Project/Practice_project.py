import json
import os

the_dict = {"First": "FirstValue", "Second": "SecondValue"}

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def export(export_thing):
    with open('notepad.json', 'w') as f:
        f.write(json.dumps(export_thing))

def importer():
    with open('notepad.json') as f:
        dict_one = f.read()
        dict_one = json.loads(dict_one)
        return dict_one

export(the_dict)
dict = importer()
print(dict)

dict["Third"] = "ThirdValue"
dict["Fourth"] = "FourthValue"

export(dict)
dict_1 = importer()
print(dict_1)

list = {"One": "1"}
export(list)
list_1 = importer()
print(list_1)

