# A Program that perform wrong calculation as per Instruction other wise it will perform calculation accurately 
# using IF & IF ELSE 
print("Enter 1st number =")
num1= int(input())
print("choose + for Addition \n choose - for Subtraction \n choose / for Division \n choose * for Multiplication \n")
operator=input()
print("Enter 2nd number =")
num2= int(input())
print(".........................loading please wait :")

if operator== "+":
    if num1==77 and num2==92:
        print(num1 , operator, num2)
        print("Sum is = 7792")
    else:
        print(num1 , operator, num2)
        print ("Sum is =" ,num1 + num2)
elif operator== "-":
    if num1==50 and num2==25:
        print(num1 , operator, num2)
        print("Difference is = 120")
    else:
        print(num1 , operator, num2)
        print ("Difference is =" ,num1 - num2)
elif operator== "/":
    if num1==155 and num2==8:
        print(num1 , operator, num2)
        print("Division is = 3")
    else:
        print(num1 , operator, num2)
        print ("Division is =" ,num1 / num2)
elif operator== "*":
    if num1==33 and num2==11:
        print(num1 , operator, num2)
        print("Multiplication is = 120")
    else:
        print(num1 , operator, num2)
        print ("Multiplication is =" ,num1 * num2)
else:
    print("You Entered Invalid Operator")                                     