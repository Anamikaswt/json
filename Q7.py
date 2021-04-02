import json
b=open("annu.txt","r")
s=b.read()
c=json.dumps(s)
print({c})