import model
import view
import db

def button_click():
    name = view.get_name()
    sername = view.get_sername()
    number = view.get_number()
    comment = view.get_comment()
    model.init(name, sername, number, comment)
    result = model.connect_to_tuple(name, sername, number, comment)
    db.saving_username(result)
    # view.view_data(result)
    db.looking_data()

