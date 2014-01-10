import sqlite3

def insert_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Status (Status) values (?)"
        status = input("Please enter the data you wish to add: ")
        print(status)
        values = (status, )
        cursor.execute(sql,values)
        db.commit()

def insert_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Type (Type) values (?)"
        Type = input("Please enter the data you wish to add: ")
        print(Type)
        values = (Type, )
        cursor.execute(sql,values)
        db.commit()

def insert_customer_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Customer (FirstName,Surname,TelephoneNumber) values (?,?,?)"
        Firstname = input("Please enter the First Name of the customer: ")
        Surname = input("Please enter the Surname of the customer: ")
        Number = input("Please enter the Telephone Number of the customer: ")
        values = (Firstname, Surname, Number)
        cursor.execute(sql,values)
        db.commit()

def insert_bodice_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into BodiceType (BodiceDetail,BodiceFabric,BodiceLength) values (?,?,?)"
        Detail = input("Please enter the detail of the Bodice: ")
        Fabric = input("Please enter the Fabric used on the bodice: ")
        Length = input("Please enter the length of the bodice (cm): ")
        values = (Detail,Fabric,Length)
        cursor.execute(sql,values)
        db.commit()

def insert_dress_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into DressType (DressDetail,DressFabric,DressLength) values (?,?,?)"
        Detail = input("Please enter the detail of the Dress: ")
        Fabric = input("Please enter the Fabric used on the Dress: ")
        Length = input("Please enter the length of the Dress (cm): ")
        values = (Detail,Fabric,Length)
        cursor.execute(sql,values)
        db.commit()

def insert_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Appointment (CustomerID,TypeID,Date,Time) values (?,?,?,?)"
        values = (CustomerID,TypeID,Date,Time)
        cursor.execute(sql,values)
        db.commit()

def insert_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into Item (BodiceTypeID, CustomerID, DressTypeID, StatusID, Bridal, DateIn, DateRequired) values (?,?,?,?,?,?,?)"
        values = (BodiceTypeID, CustomerID, DressTypeID, StatusID, Bridal, DateIn, DateRequired)
        cursor.execute(sql, values)
        db.commit()

def insert_appointment_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "INSERT into AppointmentItem (AppointmentID,ItemID) values (?,?)"
        values = (AppointmentID,ItemID)
        cursor.execute(sql, values)
        db.commit()

if __name__ == "__main__":
    db_name = ("test.db")
    #insert_status_data(db_name)
    #insert_type_data(db_name)
    #insert_customer_data(db_name)
    #insert_bodice_type_data(db_name)
    #insert_dress_type_data(db_name)
