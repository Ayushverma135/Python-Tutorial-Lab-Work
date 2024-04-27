'''combo=input("enter the combo:")
if(combo == "veg"):
    veg=int(input("enter the number of plate for veg:"))
    total_item=120*veg
else:
    non_veg=int(input("enter the number of plate for non veg:"))
    total_item=150*veg
n=int(input("enter the distance:"))
if(n<=3):
    total_item=total_item
    print("your total bill is",total_item)
elif(3<n<=6):
    total_item=total_item+(n-3)*3
    print("your total bill is",total_item)
else:
    total_item=total_item+3*3+(n-6)*6
    print("your total bill is",total_item)'''
if(len(str(account_number)) == 4 and str(account_number)=='1'):
        if(account_balance >= 100000):
            if(salary > 25000):
                
            if(loan_type == "Car"):
                eligible_loan_amount = 500000
                if(loan_amount_expected <= eligible_loan_amount):
                    
                else:
                    print("The customer is not eligible for the loan")
            elif(loan_type == "House"):
                eligible_loan_amount = 6000000
                if(loan_amount_expected <= eligible_loan_amount):
                    
                else:
                    print("The customer is not eligible for the loan")
            elif(loan_type == "Business"):
                eligible_loan_amount = 7500000
                if(loan_amount_expected <= eligible_loan_amount):
                    
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")
            
         

