import sqlite3

def update_status_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """UPDATE Status set
                 Status = ?
                 WHERE StatusID = ?"""
        statusID = int(input("Please enter the ID of the data you wish to change: "))
        status = input("Please enter the change you wish to make: ")
        if status == "":
            return
        values = (status,statusID)
        cursor.execute(sql,values)
        db.commit()

def update_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """UPDATE Type set
                 Type = ?
                 WHERE TypeID = ?"""
        TypeID = int(input("Please enter the ID of the data you wish to change: "))
        Type = input("Please enter the change you wish to make: ")
        if Type == "":
            return
        values = (Type,TypeID)
        cursor.execute(sql,values)
        db.commit()

def update_customer_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Customer WHERE CustomerID = ?"
        ID = int(input("Please enter the ID of the data you wish to change: "))
        cursor.execute(sql, (ID, ))
        temp = cursor.fetchall()
        sql = """UPDATE Customer set
                 FirstName = ?, Surname = ?, TelephoneNumber = ?
                 WHERE CustomerID = ?"""
        print("If no changes need to be made, leave space blank")
        Firstname = input("Please enter the change you wish to make: ")
        Surname = input("Please enter the change you wish to make: ")
        Number = input("Please enter the change you wish to make: ")
        if Firstname == "":
            Firstname = temp[0][1]
        if Surname == "":
            Surname = temp[0][2]
        if Number == "":
            Number = temp[0][3]
        values = (Firstname, Surname, Number, ID)
        cursor.execute(sql,values)
        db.commit()

def update_bodice_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM BodiceType WHERE BodiceTypeID = ?"
        ID = int(input("Please enter the ID of the data you wish to change: "))
        cursor.execute(sql, (ID, ))
        temp = cursor.fetchall()
        sql = """UPDATE BodiceType set
                 BodiceDetail = ?, BodiceFabric = ?, BodiceLength = ?
                 WHERE BodiceTypeID = ?"""
        print("If no changes need to be made, leave space blank")
        Detail = input("Please enter the change you wish to make: ")
        Fabric = input("Please enter the change you wish to make: ")
        Length = input("Please enter the change you wish to make: ")
        if Detail == "":
            Detail = temp[0][1]
        if Fabric == "":
            Fabric = temp[0][2]
        if Length == "":
            Length = temp[0][3]
        values = (Detail, Fabric, Length, ID)
        cursor.execute(sql,values)
        db.commit()

def update_dress_type_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM DressType WHERE DressTypeID = ?"
        ID = int(input("Please enter the ID of the data you wish to change: "))
        cursor.execute(sql, (ID, ))
        temp = cursor.fetchall()
        sql = """UPDATE DressType set
                 DressDetail = ?, DressFabric = ?, DressLength = ?
                 WHERE DressTypeID = ?"""
        print("If no changes need to be made, leave space blank")
        Detail = input("Please enter the change you wish to make: ")
        Fabric = input("Please enter the change you wish to make: ")
        Length = input("Please enter the change you wish to make: ")
        if Detail == "":
            Detail = temp[0][1]
        if Fabric == "":
            Fabric = temp[0][2]
        if Length == "":
            Length = temp[0][3]
        values = (Detail, Fabric, Length, ID)
        cursor.execute(sql,values)
        db.commit()

def update_appointment_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Appointment WHERE AppointmentID = ?"
        ID = int(input("Please enter the ID of the data you wish to change: "))
        cursor.execute(sql, (ID, ))
        temp = cursor.fetchall()
        sql = """UPDATE Appointment set
                 CustomerID = ?, TypeID = ?, Date = ?, Time = ?,
                 WHERE AppointmentID = ?"""
        print("If no changes need to be made, leave space blank")
        CustomerID = input("Please enter the change you wish to make: ")
        TypeID = input("Please enter the change you wish to make: ")
        Date = input("Please enter the change you wish to make: ")
        Time = input("Please enter the change you wish to make: ")
        if CustomerID == "":
            CustomerID = temp[0][1]
        if TypeID == "":
            TypeID = temp[0][2]
        if Date == "":
            Date = temp[0][3]
        if Time == "":
            Time = temp[0][4]
        values = (CustomerID,TypeID,Date,Time,ID)
        cursor.execute(sql,values)
        db.commit()

def update_item_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Appointment WHERE AppointmentID = ?"
        ID = int(input("Please enter the ID of the data you wish to change: "))
        cursor.execute(sql, (ID, ))
        temp = cursor.fetchall()
        sql = """UPDATE Appointment set
              BodiceTypeID = ?, CustomerID = ?, DressTypeID = ?, StatusID = ?, Bridal = ?, DateIn = ?, DateRequired = ?, Instructions = ?, OtherRequirements = ?,
              WHERE AppointmentID = ?"""
        print("If no changes need to be made, leave space blank")
        BodiceTypeID = input("Please enter the change you wish to make: ")
        CustomerID = input("Please enter the change you wish to make: ")
        DressTypeID = input("Please enter the change you wish to make: ")
        StatusID = input("Please enter the change you wish to make: ")
        Bridal = input("Please enter the change you wish to make: ")
        DateIn = input("Please enter the change you wish to make: ")
        DateRequired = input("Please enter the change you wish to make: ")
        Instructions = input("Please enter the change you wish to make: ")
        OtherRequirements = input("Please enter the change you wish to make: ")
        if BodiceTypeID == "":
            BodiceTypeID = temp [0][1]
        if CustomerID == "":
            CustomerID = temp [0][2]
        if DressTypeID == "":
            DressTypeID = temp [0][3]
        if StatusID == "":
            StatusID = temp [0][4]
        if Bridal == "":
            Bridal = temp [0][5]
        if DateIn == "":
            DateIn = temp [0][6]
        if DateRequired == "":
            DateRequired = temp [0][7]
        if Instructions == "":
            Instructions = temp [0][8]
        if OtherRequirements == "":
            OtherRequirements = temp [0][9]
        values = (BodiceTypeID,CustomerID,DressTypeID,StatusID,Bridal,DateIn,DateRequired,Instructions,OtherRequirements,ID)
        cursor.execute(sql,values)
        db.commit()

def update_appointmentItem_data(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM AppointmentItem WHERE AppointmentItemID = ?"
        ID = int(input("Please enter the ID of the data you wish to change: "))
        cursor.execute(sql, (ID, ))
        temp = cursor.fetchall()
        sql = """UPDATE AppointmentItem set
                 AppointmentID = ?, ItemID = ?
                 WHERE AppointmentItemID = ?"""
        print("If no changes need to be made, leave space blank")
        AppointmentID = input("Please enter the AppointmentID: ")
        ItemID = input("Please enter the ItemID: ")
        if AppointmentID == "":
            AppointmentID = temp[0][1]
        if ItemID == "":
            ItemID = temp[0][2]
        values = (AppointmentID,ItemID, ID)
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    db_name = ("test.db")
    update_status_data(db_name)
    update_type_data(db_name)
    update_customer_data(db_name)
    update_bodice_type_data(db_name)
    update_dress_type_data(db_name)
    update_appointment_data(db_name)
    update_item_data(db_name)
    update_appointmentItem_data(db_name)
    
