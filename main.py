documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
help = """

p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – команда, которая спросит номер документа и вывpедет номер полки, на которой он находится;
l – команда, которая выведет список всех документов в формате passport “2207 876234” “Василий Гупкин”;
a – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;

"""
print(help)


def return_owner():
    number = input("Введите номер и серию документа через пробел: \n")
    for document in documents:
        if document["number"] == number:
            return print(f'Владелец документа: {document["name"]}\n')
    print('Указанного номера в базе нет\n')


def return_shelf():
    doc_number = input("Введите номер и серию документа через пробел: \n")
    search = False
    for directory, docs in directories.items():
        if doc_number in docs:
            search = True
            print(f"Документ на полке №{directory}\n")
            break
    if not search:
        print("Введенный документ отсутствует!\n")


def return_full_list():
    print()
    for document in documents:
        print(f'{document["type"]} \"{document["number"]}\" \"{document["name"]}\"')
        print()


def add_document():
    doc_type = input("Введите тип документа: ")
    doc_number = input("Введите серию номер документа через пробел: \n")
    owner = input("Введите владельца документа: ")
    documents.append({"type": doc_type, "number": doc_number, "name": owner})

    shelf_search = False
    while not shelf_search:
        dir_number = input("Введите номер полки: \n")
        if dir_number in directories:
            directories[dir_number].append(doc_number)
            print("Документ успешно добавлен!\n")
            shelf_search = True
        else:
            print(f'''Такой полки не существует! Необходимо указать номер из списка:
{', '.join(list(directories.keys()))} ''')


def form():
    command = input("Введите символ поиска (p, s, l, a): ").lower()
    if command == "p":
        return_owner()
    elif command == "s":
        return_shelf()
    elif command == "l":
        return_full_list()
    elif command == "a":
        add_document()
    else:
        print("Измените символ поиска!")


while True:
    form()