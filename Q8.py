import json
list1=["neelam","programer","24","2400",]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"] 
list5=["name","designation","age","salery"]
employ1={}
employ2={}
employ3={}
employ4={}
i=0
while i<len(list1):
    employ1[list5[i]]=list1[i]
    i=i+1
j=0
while j<len(list2):
    employ2[list5[j]]=list2[j]
    j=j+1
k=0
while k<len(list3):
    employ3[list5[k]]=list3[k]
    k=k+1
l=0
while l<len(list4):
    employ4[list5[l]]=list4[l]
    l=l+1
print(employ1,employ2,employ3,employ4)
dic1{}
b=employ1.update()