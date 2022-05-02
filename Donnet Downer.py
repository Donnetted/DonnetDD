#Author : Donnet Downer
#Date created April 28, 2022
#Course: ITT103
#Purpose: This program is to calculate and state the commission received and groups they belong to 
#Name of Program: JamEx Limited Commission Report
def findComm():
    if sp_class == 1:
        if sales_amount == 1000 or sales_amount < 1000 and sales_amount > 0:
            #assigning the commission rate to the variable
            commission_rate=float(0.06)
            print("The commission rate is", commission_rate)
            #caluclate the commission
            commission=(sales_amount * commission_rate)
            print("The commission is", commission)
        elif sales_amount > 1000 and sales_amount < 2000:
                #assigning the commission rate to the variable
                commission_rate=float(0.07)
                print("The commission rate is", commission_rate)
                #caluclate the commission
                commission=(sales_amount * commission_rate)
                print("The commission is", commission)
        elif    sales_amount == 2000 or sales_amount > 2000:
                    #assigning the commission rate to the variable
                    commission_rate=float(0.1)
                    print("The commission rate is", commission_rate)
                    #caluclate the commission
                    commission=(sales_amount * commission_rate)
                    print("The commission is", commission)
    elif sp_class == 2:
        if sales_amount < 1000:
            #assigning the commission rate to the variable
            commission_rate=float(0.04)
            print("The commission rate is", commission_rate)
            #caluclate the commission
            commission=(sales_amount * commission_rate)
            print("The commission is", commission)
        elif sales_amount > 1000:
                #assigning the commission rate to the variable
                commission_rate=float(0.06)
                print("The commission rate is", commission_rate)
                #caluclate the commission
                commission=(sales_amount * commission_rate)
                print("The commission is", commission)
    elif sp_class == 3:
            #assigning the commission rate to the variable
            commission_rate=float(0.045)
            print("The commission rate is", commission_rate)
            #caluclate the commission
            commission=(sales_amount * commission_rate)
            print("The commission is", commission)
    else:
            #Say not valid
            print("An error occurred with the class")

val=int(5)
while val == 5:
    sales_person_name=input("What is the sales person name? ")
    sales_person_number=input("What is the sales person number? ")
    sales_amount=float(input("What is the sales amount? "))
    sp_class=int(input("What is the sales person class? "))
    findComm()
    val=int(input('To go again, enter the the number 5 '))
    
print("Done")
