
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
    Customer = search_customer_data(db_name)
    Customer = Customer[0]
    Type = search_type_data(db_name)
    Type = Type[0]
    return Customer, Type, Date, Time

def item_input(db_name):
    BodiceType = search_bodice_type_data(db_name)
    BodiceType = BodiceType[0]
    Customer = search_customer_data(db_name)
    Customer = Customer[0]
    DressType = search_dress_type_data(db_name)
    DressType = DressType[0]
    Status = search_status_data(db_name)
    Status = Status[0]
    ItemType = search_item_type_data
    ItemType = ItemType[0]
    Bridal = input("Is this a bridal item?: ").strip()
    DateIn = input("Please enter the Date the item came in: ").strip()
    DateRequired = input("Please enter the date the item in required (if applicable): ").strip()
    Instructions = input("Please enter the instructions for the item: ").strip()
    OtherRequirements = input("Please enter any otger requirements: ").strip()

def appointment_item(db_name):
    Appointment = search_appointment_data(db_name)
    Appointment = Appointment[0]
    Item = search_item_data(db_name)
    Item = Item[0]
    return Appointment,Item
