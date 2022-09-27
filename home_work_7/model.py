first_name = ''
sec_name = ''
phone_number = ''
comment_to_number = ''


def init(name, surname, number, comment):
    global first_name
    global sec_name
    global phone_number
    global comment_to_number

    first_name = name
    sec_name = surname
    phone_number = number
    comment_to_number = comment

def init_criteria(surname):
    global sec_name

    sec_name = surname

def connect_to_tuple(name, surname, number, comment):
    return (name, surname, number, comment)

# def phone_book(n_s, n_c):


