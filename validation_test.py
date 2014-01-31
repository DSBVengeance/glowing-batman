valid = False
while not valid:
    Firstname = input("Please enter the first name of the customer: ").strip()
    Firsttest = 0
    for n in range(len(Firstname)):
        if Firstname[n].isdigit() == True:
            Firsttest += 1        
    if Firsttest >= 1:
        valid = False
        print("Please enter a First Name, only using letters.")
        pass
    else:
        while not valid:
            Surname = input("Please enter the surname of the customer: ").strip()
            Surtest = 0
            for n in range(len(Surname)):
                if Surname[n].isdigit() == True:
                    Surtest += 1
                    print(Surtest)
            if Surtest >= 1:
                valid = False
                print("Please enter a Surname, using only letters.")
                pass
            else:
                while not valid:
                    Number = input("Please enter the contact number of the customer: ").strip()
                    Numtest = 0
                    for n in range(len(Number)):
                        if Number[n].isdigit() == False:
                            Numtest += 1
                    if Numtest >= 1:
                        print("Please enter a phone number")
                    else:
                        if len(Number) == 11:
                            valid = True
                        else:
                            print('Please enter a valid phone number (11 digits)')

print("return Firstname, Surname, Number")
