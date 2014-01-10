import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exist, do you wish to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print('The existing table was kept')
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_appointment_table(db_name):
    table_name = "Appointment"
    sql = """create table Appointment
             (AppointmentID integer,
             CustomerID integer,
             TypeID integer,
             Date string,
             Time string,
             primary key (AppointmentID),
             foreign key (CustomerID) references Customer(CustomerID),
             foreign key (TypeID) references Type(TypeID))"""
    create_table(db_name,table_name,sql)
##    print("1")

def create_appointmentitem_table(db_name):
    table_name = "AppointmentItem"
    sql = """create table AppointmentItem
             (AppointmentItemID integer,
             AppointmentID integer,
             ItemID integer,
             primary key (AppointmentItemID),
             foreign key (AppointmentID) references Appointment(AppointmentID),
             foreign key (ItemID) references Item(ItemID))"""
    create_table(db_name,table_name,sql)
##    print("2")

def create_bodicetype_table(db_name):
    table_name = "BodiceType"
    sql = """create table BodiceType
             (BodiceTypeID integer,
             BodiceDetail string,
             BodiceFabric string,
             BodiceLength string,
             primary key (BodiceTypeID))"""
    create_table(db_name,table_name,sql)
##    print("3")

def create_customer_table(db_name):
    table_name = "Customer"
    sql = """create table Customer
             (CustomerID integer,
             FirstName string,
             Surname string,
             TelephoneNumber integer,
             primary key (CustomerID))"""
    create_table(db_name,table_name,sql)
##    print("4")

def create_dresstype_table(db_name):
    table_name = "DressType"
    sql = """create table DressType
             (DressTypeID integer,
             DressDetail string,
             DressFabric string,
             DressLength string,
             primary key (DressTypeID))"""
    create_table(db_name,table_name,sql)
##    print("5")

def create_item_table(db_name):
    table_name = "Item"
    sql = """create table Item
             (ItemID integer,
             BodiceTypeID integer,
             CustomerID integer,
             DressTypeID integer,
             StatusID integer,
             Bridal string,
             DateIn string,
             DateRequired string,
             Instructions string,
             OtherRequirements string,
             primary key (ItemID),
             foreign key (BodiceTypeID) references BodiceType(BodiceTypeID),
             foreign key (CustomerID) references Customer(CustomerID),
             foreign key (DressTypeID) references DressType(DressTypeID),
             foreign key (StatusID) references Status(StatusID))"""
    create_table(db_name,table_name,sql)
##    print("6")

def create_status_table(db_name):
    table_name = "Status"
    sql = """create table Status
             (StatusID integer,
             Status string,
             primary key (StatusID))"""
    create_table(db_name,table_name,sql)
##    print("7")

def create_type_table(db_name):
    table_name = "Type"
    sql = """create table Type
             (TypeID integer,
             Type string,
             primary key (TypeID))"""
    create_table(db_name,table_name,sql)
##    print("8")

def db_name_input():
    db_name = input("Please enter the name of your database: ")
    db_name = db_name + ".db"
    print(db_name)
    return db_name

def create_database():    
    db_name = db_name_input()
    create_bodicetype_table(db_name)
    create_customer_table(db_name)
    create_dresstype_table(db_name)
    create_status_table(db_name)
    create_type_table(db_name)
    create_appointment_table(db_name)
    create_item_table(db_name)
    create_appointmentitem_table(db_name)






#Appointment,AppointmentItem,BodiceType,Customer,DressType,Item,Status,Type
