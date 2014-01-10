import sqlite3

def delete_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Status WHERE Status = ?"
        Status = input("Please enter the Status you wish to remove: ")
        values = (Status, )
        cursor.execute(sql,values)
        db.commit()

def delete_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Type WHERE Type = ?"
        Type = input("Please enter the Type you wish to remove: ")
        values = (Type, )
        cursor.execute(sql,values)
        db.commit()

def delete_customer_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Customer WHERE FirstName = ?, Surname = ?, TelephoneNumber = ?"
        Firstname = input("Please enter the Forename you wish to delete: ")
        Surname = input("Please enter the Surname you wish to delete: ")
        Number = input("Please enter the Telephone Number you wish to delete: ")
        cursor.execute(sql, (Firstname,Surname,Number))
        db.commit()

def delete_bodice_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM BodiceType WHERE BodiceDetail = ?, BodiceFabric = ?, BodiceLength = ?"
        Detail = input("Please enter the Detail you wish to delete: ")
        Fabric = input("Please enter the Fabric you wish to delete: ")
        Length = input("Please enter the Length you wish to make: ")
        cursor.execute(sql, (Detail,Fabric,Length))
        db.commit()

def delete_dress_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM DressType WHERE DressDetail = ?, DressFabric = ?, DressLength = ?"
        Detail = input("Please enter the Detail you wish to delete: ")
        Fabric = input("Please enter the Fabric you wish to delete: ")
        Length = input("Please enter the Length you wish to make: ")
        cursor.execute(sql, (Detail,Fabric,Length))
        db.commit()

def delete_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM Appointment WHERE CustomerID = ?, TypeID = ?, Date = ?, Time = ?"
        CustomerID = input("Please enter the CustomerID you wish to delete: ")
        TypeID = input("Please enter the TypeID you wish to delete: ")
        Date = input("Please enter the Date you wish to delete: ")
        Time = input("Please enter the Time you wish to delete: ")
        values = (CustomerID,TypeID,Date,Time)
        cursor.execute(sql,values)
        db.commit()

def delete_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM BodiceType WHERE BodiceTypeID = ?, CustomerID = ?, DressTypeID = ?, StatusID = ?, Bridal = ?, DateIn = ?, DateRequired = ?"
        BodiceTypeID = input("Please enter the BodiceTypeID you wish to delete: ")
        CustomerID = input("Please enter the CustomerID you wish to delete: ")
        DressTypeID = input("Please enter the DressTypeID you wish to delete: ")
        StatusID = input("Please enter the StatusID you wish to delete: ")
        Bridal = input("Please enter the Bridal you wish to delete: ")
        DateIn = input("Please enter the Date the item you wish to delete was taken in: ")
        DateRequired = input("Please enter the Date the item is required: ")
        values = (BodiceTypeID,CustomerID,DressTypeID,StatusID,Bridal,DateIn,DateRequired)
        cursor.execute(sql,values)
        db.commit()

def delete_appointmentItem_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "DELETE FROM AppointmentItem WHERE AppointmentID = ?, ItemID = ?"
        AppointmentID = input("Please enter the AppointmentID: ")
        ItemID = input("Please enter the ItemID: ")
        values = (AppointmentID,ItemID)
        cursor.execute(sql,values)
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
    
