from bibliography import *

import sys

def main_menu():
    print("""What would you like to do?

1. Create a Database

2. Insert Data (Under Construction)

3. Update Data (Under Construction)

4. Delete Data (Under Construction)

5. View Data (Under Construction)

6. Load Database

Please enter the number of your choice below (1-6)
Or press "Q" to quit""")
    choice = input()
    ##print(choice)
    return choice

def insert_menu():
    print("""What area would you like to insert data into?

1. Appointment

2. Customer

3. Item

4. Appointment Type

5. Item Status

Please enter the number of your choice below (1-5)
Or press "M" to return to the menu""")
    choice = input()
    ##print(choice)
    return choice

def update_menu():
    print("""What area would you like to update data in?

1. Appointment

2. AppointmentItem

3. Bodice Type

4. Customer

5. Dress Type

6. Item

7. Status

8. Type

Please enter the number of your choice below (1-8)
Or press "M" to return to the menu""")
    choice = input()
    ##print(choice)
    return choice

def delete_menu():
    print("""What area would you like to delete data from?

1. Appointment

2. AppointmentItem

3. Bodice Type

4. Customer

5. Dress Type

6. Item

7. Status

8. Type

Please enter the number of your choice below (1-8)
Or press "M" to return to the menu""")
    choice = input()
    ##print(choice)
    return choice

def view_menu():
    print("""Which area would you like to view?

1. Appointment

2. AppointmentItem

3. Bodice Type

4. Customer

5. Dress Type

6. Item

7. Status

8. Type

Please enter the number of your choice below (1-8)""")
    choice = input()
##    print(choice)
    return choice

def create_menu():
    print("""Please press "Enter" to carry on to the database creation

Else, press "M" to return to the main menu""")
    choice = input()
    return choice

if __name__ == "__main__":
    end = False
    print("Welcome!")
    while not end:
        choice = main_menu()
        if choice == "Q" or choice == "q":
            end = True
            sys.exit
        elif choice == "1":
            choice = create_menu()
            if choice == "m" or choice == "M":
                print()
                pass
            elif choice == "":
                create_database()
        elif choice == "2":
            choice = insert_menu()
            if choice == "m" or choice == "M":
                print()
                pass
            elif choice == "1":
                insert_appointment_data(db_name)
            elif choice == "2":
                insert_customer_data(db_name)
            elif choice == '3':
                insert_item_data(db_name)
            elif choice == '4':
                insert_type_data(db_name)
            elif choice == '5':
                insert_status_data(db_name)
        elif choice == '3':
            choice = update_menu()
            if choice == '1':
                update_appointment_data(db_name)
            elif choice == '2':
                update_appointmentItem_data(db_name)
            elif choice == '3':
                update_bodice_type_data(db_name)
            elif choice == '4':
                update_customer_data(db_name)
            elif choice == '5':
                update_dress_type_data(db_name)
            elif choice == '6':
                update_item_data(db_name)
            elif choice == '7':
                update_status_data(db_name)
            elif choice == '8':
                update_type_data(db_name)
        elif choice == '4':
            choice = delete_menu()
            if choice == '1':
                delete_appointment_data(db_name)
            elif choice == '2':
                delete_appointmentItem_data(db_name)
            elif choice == '3':
                delete_bodice_type_data(db_name)
            elif choice == '4':
                delete_customer_data(db_name)
            elif choice == '5':
                delete_dress_type_data(db_name)
            elif choice == '6':
                delete_item_data(db_name)
            elif choice == '7':
                delete_status_data(db_name)
            elif choice == '8':
                delete_type_data(db_name)
        elif choice == '5':
            choice = view_menu()
            if choice == "m" or choice == "M":
                print()
                pass
            else:
                select_data2(choice,db_name)
        elif choice == '6':
            db_name = db_name_input()
        else:
            print("""Please enter a valid option (1-6) or Q to quit.
""")
