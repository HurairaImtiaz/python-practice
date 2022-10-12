x = 'hello worlds'
y =[]
for i in x:
    y.append(i)

print(y)
z="".join(y)
print (z)
for a in range(1,4):
    print ("enter a number=")
    n=int(input())
    list.append(n)
print("Your final list is : ", list)
# convert a sentence of string type into List
sentence = input("Enter a sentence:")
list_var=sentence.split()
print(list_var)
# convert multiple strings  into one  List
list1=[]
for b in range (1,4):
    print("write the name of a fruit:")
    m=input()
    list1.append(m)
print(list1)
# convert list into one string using join function

str2=" ".join(list1)
print(str2)