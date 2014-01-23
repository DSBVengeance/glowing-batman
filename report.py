import sqlite3

choice = 1
db_name = "test3.db"
if choice == 1:
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """SELECT Customer.Firstname, Customer.Surname, Customer.TelephoneNumber, Appointment.Date, Appointment.Time FROM Appointment, Customer WHERE Appointment.Date = ? AND Customer.CustomerID = Appointment.CustomerID"""
        Date = input("Please enter the date of the day you wish to see: ")
        cursor.execute(sql,(Date,))
        temp = cursor.fetchall()
        
        print(temp)
        print('{0:>7} {1:>8} {2:>5} {3:>5} {4:>12}'.format('Customer Firstname', 'Customer Surname', 'Date','Time','Customer Telephone No.'))
       
        
        for n in range(len(temp)):
            print('{0:>7} {1:>8} {2:>5} {3:>5} {4:>12}'.format(temp[n][0],temp[n][1],temp[n][3],temp[n][4],temp[n][2]))
    

