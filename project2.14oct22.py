# you have to write a program in which:
#  you will take a variable and assign it an integer value i.e 123
#  and then write a logic that the program will print true if the reverse of value is same as the original value
#  i-e reverse of 121 is 121 so it is true else false
#  and if the variable has value less then or equal to zero it should also be false



print("Enter an integer number :")
user_input = input("Enter a number =")
reverse_user_input = user_input[::-1]
# print(reverse_user_input)
if user_input==reverse_user_input:
    print("TRUE")
elif int(user_input)<0 and int(user_input)==0 :
    print("FALSE")
else:
    print("FALSE")    
    
    