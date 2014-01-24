import sqlite3

choice = 1
db_name = "test3.db"
def create_report(db_name,choice):
    if choice == 1:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            sql = """SELECT Customer.Firstname, Customer.Surname, Customer.TelephoneNumber, Appointment.Date, Appointment.Time FROM Appointment, Customer WHERE Appointment.Date = ? AND Customer.CustomerID = Appointment.CustomerID"""
            Date = input("Please enter the date of the day you wish to see: ")
            cursor.execute(sql,(Date,))
            temp = cursor.fetchall()
            
            print(temp)
            print('{0:^11} {1:^9} {2:^12} {3:^6} {4:^15}'.format('Firstname', 'Surname', 'Date','Time','Telephone No.'))
           
            
            for n in range(len(temp)):
                print('{0:^11} {1:^9} {2:^12} {3:^6} {4:^15}'.format(temp[n][0],temp[n][1],temp[n][3],temp[n][4],temp[n][2]))

    elif choice == 2:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            sql = "SELECT Customer.Firstname, Customer.Surname, Customer.TelephoneNumber, ItemType.ItemType, Item.DateIn, Item.Instructions, Item.DateRequired"
            DateIn = input("Please enter the date when the item came in: ")
            cursor.execute(sql,(DateIn,))
            temp = cursor.fetchall()
        


create_report(db_name,choice)
