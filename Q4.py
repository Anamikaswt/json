import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
dic={}
b=sorted(a.keys())
for i in b:
    dic[i]=a[i]
jsondata=json.dumps(dic)
print(jsondata)
print(type(jsondata))




