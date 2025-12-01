import time
#----------------------------------------------
#EXPENCE TRACKER
#---------------------------------------------

expenceList = [] #list of all expence catogeries

print("Welcome to Expence Tracker")

while True:
    print("=-=-=-=-=- MENU -=-=-=-=-=")
    print("1. ADD EXPENCES")
    print("2. VIEW ALL EXPENSES")
    print("3. VIEW TOTAL SPENDING")
    print("4. EXIT")

    choice = input("Enter numbers from 1 to 4 to choose the option :") 

    #1.Add expenses

    if choice == "1":
        date = input("Enter date in dd/mm/yyyy format :")
        category = input("Enter category of your expense (eg. FOOD, CLOTHES, EDUCATION, MEDICATION) :")
        description = input("Enter short description :") 
        amount = float(input("Enter amount (₹ only): ")) 

        expence = {
            "Date :" : date,
            "Category :" : category,
            "Description :" : description,
            "Amount :" : amount 
        }

        expenceList.append(expence)
        print("\n Expence added successfully !!")

    elif choice == "2":
        #viewing expences
        if len(expenceList) == 0:
            print("No expences are recorded !! Add one and try again later")
        else:
            print("\n Here are all your expenses") 
            i = 1
            for spending in expenceList:
                print(f"{i}. {spending["Date :"]}, {spending["Category :"]}, {spending["Description :"]}, {spending["Amount :"]}")
                i += 1
            print("------------------------------------------------------------")

    elif choice == "3":
        #viewing total spending 
        total = 0
        for spend in expenceList:
            total += spend["Amount :"]
        print(f"\n TOTAL SPENDING = ₹ {total}")

    elif choice == "4":
        #exit 
        print("\n Quitting app ", end=" ")
        print(".")
        time.sleep(1)
    else:
        print("Invalid choice. please try again.")
    
