import sqlite3

from bibliography import *

def search_customer_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Customer WHERE FirstName LIKE ? AND Surname LIKE ? AND TelephoneNumber LIKE ?"
        Firstname, Surname, Number = customer_input()
        Firstname = '%'+Firstname+'%'
        Surname = '%'+Surname+'%'
        Number = '%'+Number+'%'
        values = (Firstname, Surname, Number)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp
    
def search_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Status WHERE Status LIKE ?"
        Status = status_input()
        Status = '%'+Status+'%'
        values = (Status,)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def search_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Type WHERE Type LIKE ?"
        Type = type_input()
        Type = '%'+Type+'%'
        values = (Type,)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def search_bodice_type_data(db_name,):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM BodiceType WHERE BodiceDetail LIKE ? AND BodiceFabric LIKE ? AND BodiceLength LIKE ?"
        Detail, Fabric, Length = bodice_type_input()
        Detail = '%'+Detail+'%'
        Fabric = '%'+Fabric+'%'
        Length = '%'+Length+'%'
        values = (Detail, Fabric, Length)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def search_dress_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM DressType WHERE DressDetail LIKE ? AND DressFabric LIKE ? AND DressLength LIKE ?"
        Detail, Fabric, Length = dress_type_input()
        Detail = '%'+Detail+'%'
        Fabric = '%'+Fabric+'%'
        Length = '%'+Length+'%'
        values = (Detail, Fabric, Length)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def search_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Appointment WHERE CustomerID = ? AND TypeID = ? AND Date LIKE ? AND Time LIKE ?"
        CustomerID, TypeID, Date, Time = appointment_input(db_name)
        Date = "%"+Date+"%"
        Time = "%"+Date+"%"
        values = (CustomerID,TypeID,Date,Time)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def search_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """SELECT * FROM Appointment WHERE BodiceTypeID = ? AND CustomerID = ? AND DressTypeID = ? AND
StatusID = ? AND ItemTypeID = ? AND Bridal LIKE ? AND DateIn LIKE ? AND DateRequired LIKE ? AND Instructions = AND OtherRequirements LIKE ?"""
        BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements = item_input(db_name)
        Bridal = "%"+Bridal+"%"
        DateIn = "%"+DateIn+"%"
        DateRequired = "%"+DateRequired+"%" 
        Instructions = "%"+Instructions+"%"
        OtherRequirements = "%"+OtherRequirements+"%"
        values = (BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def search_appointment_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM AppointmentItem WHERE AppointmentID = ? AND ItemID = ?"
        AppointmentID, ItemID = appointment_item_input(db_name)
        values = (AppointmentID, ItemID)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def search_item_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM ItemType WHERE ItemType LIKE ?"
        ItemType = item_type_input()
        ItemType = "%"+ItemType+"%"
        values = (ItemType,)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        if len(temp) > 1:
            temp = data_selection(temp)
        db.commit()
        return temp

def data_selection(data):
    choice = 0
    if len(data) > 1:
        for n in range(len(data)):
            print('{0:<5} {1}'.format(n+1,data[n][1:]))
        choice = int(input('Please choose the number of the Customer listed (1-{0}): '.format(n+1)))
        choice -= 1
    return data[choice]
        
#Data input

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
    Date = input("Please enter the date of appointment: ").strip()
    Time = input("Please enter the time of appointment: ").strip()
    Customer = search_customer_data(db_name)
    Customer = data_selection(Customer)
    Customer = Customer[0]
    Type = search_type_data(db_name)
    Type = data_selection(Type)
    Type = Type[0]
    return Customer, Type, Date, Time

def item_input(db_name):
    Customer = search_customer_data(db_name)
    Customer = data_selection(Customer)
    Customer = Customer[0]
    Status = search_status_data(db_name)
    Status = data_selection(Status)
    Status = Status[0]
    ItemType = search_item_type_data(db_name)
    ItemType = data_selection(ItemType)
    ItemType = ItemType[0]
    Bridal = input("Is this a bridal item? (yes/no): ").strip().upper()
    if Bridal == "NO" or Bridal == "N":
        BodiceType = 1
        DressType = 1
    elif Bridal == "YES" or Bridal == "Y":
        BodiceType = search_bodice_type_data(db_name)
        BodiceType = data_selection(BodiceType)
        BodiceType = BodiceType[0]
        DressType = search_dress_type_data(db_name)
        DressType = data_selection(DressType)
        DressType = DressType[0]
    DateIn = input("Please enter the Date the item came in: ").strip()
    DateRequired = input("Please enter the date the item in required (if applicable): ").strip()
    Instructions = input("Please enter the instructions for the item: ").strip()
    OtherRequirements = input("Please enter any otger requirements: ").strip()
    return BodiceType,Customer,DressType,Status,ItemType,Bridal,DateIn,DateRequired,Instructions,OtherRequirements

def appointment_item(db_name):
    Appointment = search_appointment_data(db_name)
    Appointment = data_selection(Appointment)
    Appointment = Appointment[0]
    Item = search_item_data(db_name)
    Item = data_selection(Item)
    Item = Item[0]
    return Appointment,Item


            
##temp = search_customer_data('test.db')
##print(len(temp))
##print(len(temp[0]))
##print(temp)

        
