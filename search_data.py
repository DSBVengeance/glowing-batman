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
        
##        print(temp)
        print(len(temp))
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))
        db.commit()
    
def search_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Status WHERE Status LIKE ?"
        Status = status_input()
        Status = '%'+Status+'%'
        values = (Status)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))

def search_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Type WHERE Type LIKE ?"
        Type = type_input()
        Type = '%'+Type+'%'
        values = (Type)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))

def search_bodice_type_data(db_name):
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
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))

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
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))

def search_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Appointment WHERE CustomerID = ? AND TypeID = ? AND Date = ? AND Time = ?"
        CustomerID, TypeID, Date, Time = appointment_input(db_name)
        values = (CustomerID,TypeID,Date,Time)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))

def search_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """SELECT * FROM Appointment WHERE BodiceTypeID = ? AND CustomerID = ? AND DressTypeID = ? AND
StatusID = ? AND ItemTypeID = ? AND Bridal = ? AND DateIn = ? AND DateRequired = ? AND Instructions = AND OtherRequirements = ?"""
        BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements = item_input(db_name)
        values = (BodiceTypeID,CustomerID,DressTypeID,StatusID,ItemTypeID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))

def search_appointment_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM AppointmentItem WHERE AppointmentID = ? AND ItemID = ?"
        AppointmentID, ItemID = appointment_item_input(db_name)
        values = (AppointmentID, ItemID)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))

def search_item_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM ItemType WHERE ItemType = ?"
        ItemType = item_type_input()
        values = (ItemType)
        cursor.execute(sql,values)
        temp = cursor.fetchall()
        db.commit()
        for n in range(len(temp)):
            print('{0:<5} {1}'.format(n+1,temp[n]))


            
##temp = search_customer_data('test.db')
##print(len(temp))
##print(len(temp[0]))
##print(temp)

        
