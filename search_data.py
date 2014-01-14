import sqlite3

from bibliography import *

def search_customer_data(db_name):
    print('test3')
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Customer WHERE FirstName = ? AND Surname = ? AND TelephoneNumber = ?"
        Firstname, Surname, Number = customer_input()
        values = (Firstname, Surname, Number)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        print('test4')
        return temp

    
def search_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Status WHERE Status = ?"
        Status = status_input()
        values = (Status)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp

def search_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Type WHERE Type = ?"
        Type = type_input()
        values = (Type)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp

def search_bodice_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM BodiceType WHERE BodiceDetail = ? AND BodiceFabric = ? AND BodiceLength = ?"
        Detail, Fabric, Length = bodice_type_input()
        values = (Detail, Fabric, Length)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp

def search_dress_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM DressType WHERE DressDetail = ? AND DressFabric = ? AND DressLength = ?"
        Detail, Fabric, Length = bodice_type_input()
        values = (Detail, Fabric, Length)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp

def search_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Appointment WHERE CustomerID = ? AND TypeID = ? AND Date = ? AND Time = ?"
        CustomerID, TypeID, Date, Time = appointment_input(db_name)
        values = (CustomerID,TypeID,Date,Time)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp

def search_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """SELECT * FROM Appointment WHERE BodiceTypeID = ? AND CustomerID = ? AND DressTypeID = ? AND
StatusID = ? AND Bridal = ? AND DateIn = ? AND DateRequired = ? AND Instructions = AND OtherRequirements = ?"""
        BodiceTypeID,CustomerID,DressTypeID,StatusID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements = item_input(db_name)
        values = (BodiceTypeID,CustomerID,DressTypeID,StatusID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp

def search_appointment_item(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM AppointmentItem WHERE AppointmentID = ? AND ItemID = ?"
        AppointmentID, ItemID = appointment_item_input(db_name)
        values = (AppointmentID, ItemID)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        return temp
    
##temp = search_customer_data('test.db')
##print(len(temp))
##print(len(temp[0]))
##print(temp)

        
