def customer_input():
    Firstname = input("Please enter the first name of the customer: ")
    Surname = input("Please enter the surname of the customer: ")
    Number = input("Please enter the contact number of the customer: ")
    return Firstname, Surname, Number

def status_input():
    Status = input("Please enter the status of the item: ")
    return Status

def type_input():
    Type = input("Please enter the type of appointment: ")
    return Type

def bodice_type_input():
    Detail = input("Please enter the detail of the Bodice: ")
    Fabric = input("Please enter the Fabric used on the bodice: ")
    Length = input("Please enter the length of the bodice (cm): ")
    return Detail, Fabric, Length

def dress_type_input():
    Detail = input("Please enter the detail of the Dress: ")
    Fabric = input("Please enter the Fabric used on the Dress: ")
    Length = input("Please enter the length of the Dress (cm): ")
    return Detail, Fabric, Length

def item_type_input():
    ItemType = input("Please enter the type of item: ")
    return ItemType

def appointment_input(db_name):
    Date = input("Please enter the time of appointment: ")
    Time = input("Please enter the date of appointment: ")
    Customer = select_data(4, db_name)
    Type = select_data(9, db_name)
    return Customer, Type, Date, Time

def item_input(db_name):
    BodiceType = select_data(3,db_name)
    Customer = select_data(4,db_name)
    DressType = select_data(5,db_name)
    Status = select_data(8,db_name)
    ItemType = select_data(7, db_name)
    Bridal = input("Is this a bridal item?: ")
    DateIn = input("Please enter the Date the item came in: ")
    DateRequired = input("Please enter the date the item in required (if applicable): ")
    Instructions = input("Please enter the instructions for the item: ")
    OtherRequirements = input("Please enter any otger requirements: ")

def appointment_item(db_name):
    Appointment = select_data(1,db_name)
    Item = select_data(6,db_name)
    return Appointment,Item
