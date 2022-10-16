from cgi import print_directory
from signal import SIGABRT


sabzi_list = ["aalu","bengan","bhindi","tamatar","karele","matar","gobhi","shaljam","kheerey"]
# WIFE :mian g aj ye sab na le k ana balky list me se ek chez chor k agli lana 
# HUSBAND : ok g 
#solution #1:
print("..........................solution 1...............")
i=0
for item in sabzi_list:
    if i%2==0:
        print(item)
    i+=1

print("..........................solution 2................")
 # HUSBAND : ok g 
#solution #2:  
for index,item in enumerate(sabzi_list) :
     if index%2 ==0 :
         print(f"Me ne {item} lelia hai ")
         
print("..............................")         
print("BEGUM KHUSH ME KHUSH")         
print("..............................") 