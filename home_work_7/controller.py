from urllib import request
import model
import view
import db


def main():
    action = view.get_action()
    model.init_action(action)

    if action == 'добавить':
        name = view.get_name()
        surname = view.get_surname()
        number = view.get_number()
        comment = view.get_comment()
        model.init(name, surname, number, comment)
        result = model.connect_to_tuple(name, surname, number, comment)
        db.saving_username(result)

    elif action == 'найти':
        surname = view.get_record_from_phonebook()
        model.init_criteria(surname)
        db.looking_data(surname)

    elif action == 'все контакты':
        db.looking_all()

    elif action == 'удалить':
        name = view.get_name()
        surname = view.get_surname()
        model.init_criteria(name, surname)
        db.delete_data(name, surname)

    else:
        view.view_data('Такой команды нет')
    
    answer = view.get_permission()
    model.init_action(answer)

    if answer == 'да':
        main()

    