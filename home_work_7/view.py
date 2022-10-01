def view_data(data):
    print(data)

def get_name():
    return input('Имя: ')

def get_surname():
    return input('Фамилия: ')

def get_number():
    return input('Номер телефона: ')

def get_comment():
    return input('Комментарий: ')

def get_record_from_phonebook():
    return input('Введите фамилию для поиска: ')

def get_action():
    return input("Для сохранения нового контакта введите 'добавить'.\
        Для поиска номера введите 'найти'.\
        Для просмотра списка контактов введите 'все контакты'.\
        Для удаления контакта введите 'удалить'. \n").lower()

def get_permission():
    return input("Хотите сделать что-то еще?(введите да или нет):\n").lower()
