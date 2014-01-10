from search_data import *

def select_data(code,db_name):
    if code == 1:
        temp = search_customer_data(db_name)
    elif code == 2:
        temp = search_status_data(db_name)
    elif code == 3:
        temp = search_type_data(db_name)
    elif code == 4:
        temp = search_bodice_type_data(db_name)
    elif code == 5:
        temp = search_dress_type_data(db_name)
    elif code == 6:
        temp = search_appointment_data(db_name)
    elif code == 7:
        temp = search_item_data(db_name)
    elif code == 8:
        temp = search_appointment_item_data(db_name)
    for n in range(len(temp)):
       print(temp(n))
