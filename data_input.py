def customer_input():
    Firstname = input("Please enter the first name of the customer: ").strip()
    Surname = input("Please enter the surname of the customer: ").strip()
    Number = input("Please enter the contact number of the customer: ").strip()
    return Firstname, Surname, Number

def status_input():
    Status = input("Please enter the status of the item: ").strip()
    return Status

def type_input():
    Type = input("Please enter the type of appointment: ").strip()
    return Type

def bodice_type_input():
    Detail = input("Please enter the detail of the Bodice: ").strip()
    Fabric = input("Please enter the Fabric used on the bodice: ").strip()
    Length = input("Please enter the length of the bodice (cm): ").strip()
    return Detail, Fabric, Length

def dress_type_input():
    Detail = input("Please enter the detail of the Dress: ").strip()
    Fabric = input("Please enter the Fabric used on the Dress: ").strip()
    Length = input("Please enter the length of the Dress (cm): ").strip()
    return Detail, Fabric, Length

def item_type_input():
    ItemType = input("Please enter the type of item: ").strip()
    return ItemType

def appointment_input(db_name):
    Date = input("Please enter the time of appointment: ").strip()
    Time = input("Please enter the date of appointment: ").strip()
    Customer = choose_data(4, db_name)
    Type = choose_data(9, db_name)
    return Customer, Type, Date, Time

def item_input(db_name):
    BodiceType = choose_data(3,db_name)
    Customer = choose_data(4,db_name)
    DressType = choose_data(5,db_name)
    Status = choose_data(8,db_name)
    ItemType = choose_data(7, db_name)
    Bridal = input("Is this a bridal item?: ").strip()
    DateIn = input("Please enter the Date the item came in: ").strip()
    DateRequired = input("Please enter the date the item in required (if applicable): ").strip()
    Instructions = input("Please enter the instructions for the item: ").strip()
    OtherRequirements = input("Please enter any otger requirements: ").strip()

def appointment_item(db_name):
    Appointment = choose_data(1,db_name)
    Item = choose_data(6,db_name)
    return Appointment,Item
