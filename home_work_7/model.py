first_name = ''
sec_name = ''
phone_number = ''
comment_to_number = ''
name_sername = ()
num_and_comm = ()
# phone_book = {}

def init(name, sername, number, comment):
    global first_name
    global sec_name
    global phone_number
    global comment_to_number

    first_name = name
    sec_name = sername
    phone_number = number
    comment_to_number = comment

def connect_to_tuple(name, sername, number, comment):
    return (name, sername, number, comment)

# def phone_book(n_s, n_c):


