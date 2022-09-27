import model
import view
import db

def add_number():
    name = view.get_name()
    surname = view.get_surname()
    number = view.get_number()
    comment = view.get_comment()
    model.init(name, surname, number, comment)
    result = model.connect_to_tuple(name, surname, number, comment)
    db.saving_username(result)


def find_number():
    surname = view.get_record_from_phonebook()
    model.init_criteria(surname)
    db.looking_data(surname)

def save_or_search():
    action = view.get_action()
    model.init_action(action)
    if action == 'добавить':
        add_number()
    elif action == 'найти':
        find_number()
    else:
        view.view_data('Такой команды нет')

