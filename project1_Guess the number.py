
comparison = 10
count=0
num = True
while num == True:
    print("Enter a number to guess the required number =")
    user_input= int(input())
    if user_input > comparison:
        print("The guess number is greater than the required number.")
        print("Please Try again !")
        count=count+1
        
    elif user_input < comparison:
        print("The guess number is Smaller than the required number.")
        print("Please Try again !")
        count=count+1
        
    elif user_input == comparison:
        print ("Congratulations! You Guesses the right Number ")
        print("And the right Number is = ", comparison)
        num =False
        print("your wrong attempts are =",count)
    