import sqlite3

##choice = 3
##db_name = "test3.db"

def create_report(db_name,choice):
    if choice == 1:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            sql = """SELECT Customer.Firstname, Customer.Surname, Customer.TelephoneNumber, Appointment.Date, Appointment.Time FROM Appointment, Customer WHERE Appointment.Date = ? AND Customer.CustomerID = Appointment.CustomerID"""
            Date = input("Please enter the date of the day you wish to see: ")
            cursor.execute(sql,(Date,))
            temp = cursor.fetchall()
            print('{0:^11} {1:^9} {2:^12} {3:^7} {4:^15}'.format('Firstname', 'Surname', 'Date','Time','Telephone No.'))
            for n in range(len(temp)):
                print('{0:^11} {1:^9} {2:^12} {3:^7} {4:^15}'.format(temp[n][0],temp[n][1],temp[n][3],temp[n][4],temp[n][2]))
                
    elif choice == 2:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            sql = "SELECT Customer.Firstname, Customer.Surname, Customer.TelephoneNumber, ItemType.ItemType, Item.DateIn, Item.Instructions, Item.DateRequired FROM Customer, Item, ItemType WHERE Customer.CustomerID = Item.CustomerID AND ItemType.ItemTypeID = Item.ItemTypeID AND Item.DateIn = ?"
            DateIn = input("Please enter the date when the item came in: ")
            cursor.execute(sql,(DateIn,))
            temp = cursor.fetchall()
            print('{0:^11} {1:^9} {2:^15} {3:^15} {4:^18} {5:^12} {6:^15}'.format('Firstname', 'Surname', 'Telephone No.', 'Item','Instructions','Date In', 'Date Required'))
            for n in range(len(temp)):
                print('{0:^11} {1:^9} {2:^15} {3:^15} {4:^18} {5:^12} {6:^15}'.format(temp[n][0], temp[n][1], temp[n][2], temp[n][3], temp[n][5], temp[n][4], temp[n][6]))          

    elif choice == 3:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            sql = "SELECT StatusID FROM Status WHERE Status = ?"
            Status = "In Progress"
            cursor.execute(sql,(Status,))
            Statusid = cursor.fetchall()
            Statusid = Statusid[0][0]
            sql = "SELECT Customer.Firstname, Customer.Surname, Customer.TelephoneNumber, ItemType.ItemType, Item.DateIn, Item.Instructions, Item.DateRequired FROM Customer, Item, ItemType, Status WHERE Customer.CustomerID = Item.CustomerID AND ItemType.ItemTypeID = Item.ItemTypeID AND Status.StatusID = Item.StatusID AND Status.StatusID = ?"
            cursor.execute(sql,(Statusid,))
            temp = cursor.fetchall()
            print('{0:^11} {1:^9} {2:^15} {3:^15} {4:^18} {5:^12} {6:^15}'.format('Firstname', 'Surname', 'Telephone No.', 'Item','Instructions','Date In', 'Date Required'))
            for n in range(len(temp)):
                print('{0:^11} {1:^9} {2:^15} {3:^15} {4:^18} {5:^12} {6:^15}'.format(temp[n][0], temp[n][1], temp[n][2], temp[n][3], temp[n][5], temp[n][4], temp[n][6]))          
##create_report(db_name,choice)
