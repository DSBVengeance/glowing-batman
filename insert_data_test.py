import sqlite3

from bibliography import *

def insert_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Status (Status) values (?)"
        Status = status_input()
        values = (Status,)
        cursor.execute(sql,values)
        db.commit()

def insert_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Type (Type) values (?)"
        Type = type_input()
        values = (Type,)
        cursor.execute(sql,values)
        db.commit()

def insert_customer_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Customer (FirstName,Surname,TelephoneNumber) values (?,?,?)"
        Firstname, Surname, Number = customer_input()
        values = (Firstname, Surname, Number)
        cursor.execute(sql,values)
        db.commit()

def insert_bodice_type_data(db_name, Detail, Fabric, Length):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into BodiceType (BodiceDetail,BodiceFabric,BodiceLength) values (?,?,?)"
        values = (Detail, Fabric, Length)
        cursor.execute(sql,values)
        db.commit()

def insert_dress_type_data(db_name, Detail, Fabric, Length):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into DressType (DressDetail,DressFabric,DressLength) values (?,?,?)"
        values = (Detail,Fabric,Length)
        cursor.execute(sql,values)
        db.commit()

def insert_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Appointment (CustomerID,TypeID,Date,Time) values (?,?,?,?)"
        CustomerID, TypeID, Date, Time = appointment_input(db_name)
        values = (CustomerID,TypeID,Date,Time)
        cursor.execute(sql,values)
        db.commit()

def insert_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Item (BodiceTypeID, CustomerID, DressTypeID, StatusID, ItemTypeID, Bridal, DateIn, DateRequired,Instructions,OtherRequirements) values (?,?,?,?,?,?,?,?,?,?)"
        BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements = item_input(db_name)
        values = (BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements)
        cursor.execute(sql, values)
        db.commit()

def insert_appointment_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into AppointmentItem (AppointmentID,ItemID) values (?,?)"
        AppointmentID, ItemID = appointment_item_input(db_name)
        values = (AppointmentID,ItemID)
        cursor.execute(sql, values)
        db.commit()

def insert_item_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into ItemType (ItemType) values (?)"
        ItemType = item_type_input()
        values = (ItemType,)
        cursor.execute(sql, values)
        db.commit()

##if __name__ == "__main__":
##    db_name = ("test3.db")
##    insert_status_data(db_name)
##    insert_type_data(db_name)
##    insert_customer_data(db_name)
##    insert_bodice_type_data(db_name)
##    insert_dress_type_data(db_name)
##    insert_item_type_data(db_name)
