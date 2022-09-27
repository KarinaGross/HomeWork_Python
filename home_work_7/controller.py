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
    # view.view_data(result)

def find_number():
    surname = view.get_record_from_phonebook()
    model.init_criteria(surname)
    db.looking_data(surname)

