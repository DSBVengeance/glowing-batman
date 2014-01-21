from bibliography import *

import sqlite3

def delete_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Status WHERE Status = ?"
        Status = status_input()
        values = (Status, )
        cursor.execute(sql,values)
        db.commit()

def delete_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Type WHERE Type = ?"
        Type = type_input()
        values = (Type, )
        cursor.execute(sql,values)
        db.commit()

def delete_customer_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Customer WHERE FirstName = ? AND Surname = ? AND TelephoneNumber = ?"
        Firstname, Surname, Number = customer_input()
        values = (Firstname, Surname, Number)
        cursor.execute(sql, values)
        db.commit()

def delete_bodice_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM BodiceType WHERE BodiceDetail = ? AND BodiceFabric = ? AND BodiceLength = ?"
        Detail, Fabric, Length = bodice_type_input()
        values = (Detail, Fabric, Length)
        cursor.execute(sql,values)
        db.commit()

def delete_dress_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM DressType WHERE DressDetail = ? AND DressFabric = ? AND DressLength = ?"
        Detail, Fabric, Length = bodice_type_input()
        values = (Detail,Fabric,Length)
        cursor.execute(sql,values)
        db.commit()

def delete_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Appointment WHERE CustomerID = ? AND TypeID = ? AND Date = ? AND Time = ?"
        CustomerID, TypeID, Date, Time = appointment_input(db_name)
        values = (CustomerID,TypeID,Date,Time)
        cursor.execute(sql,values)
        db.commit()

def delete_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM BodiceType WHERE BodiceTypeID = ? AND CustomerID = ? AND DressTypeID = ? AND StatusID = ? AND Bridal = ? AND DateIn = ? AND DateRequired = ?"
        BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements = item_input(db_name)
        values = (BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements)
        cursor.execute(sql, values)
        db.commit()

def delete_appointmentItem_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM AppointmentItem WHERE AppointmentID = ? AND ItemID = ?"
        AppointmentID, ItemID = appointment_item_input(db_name)
        values = (AppointmentID,ItemID)
        cursor.execute(sql, values)
        db.commit()

def delete_item_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELTE FROM ItemType WHERE ItemType = ?"
        ItemType = item_type_input()
        values = (ItemType,)
        cursor.execute(sql, values)
        db.commit()

if __name__ == "__main__":
    db_name = ("test.db")
    delete_status_data(db_name)
    delete_type_data(db_name)
    delete_customer_data(db_name)
    delete_bodice_type_data(db_name)
    delete_dress_type_data(db_name)
    delete_appointment_data(db_name)
    delete_item_data(db_name)
    delete_appointmentItem_data(db_name)
    
