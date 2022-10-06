from itertools import count


list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
list2=["apple","mango","banana"]
print(list2)
# List Functions
list2.append("orange")
print(list2)
list2.remove("banana")
print(list2)
list3 = list1+list2
print(list3)
list1.pop()
print(list1)
list2.remove("mango")
print(list2)
list1.insert(10,11)
print(list1)