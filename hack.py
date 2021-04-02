def time(s):
    list=["01","02","03","04","05","06","07","08","09","10","11","12"]
    list1=[13,14,15,16,17,18,19,20,21,22,23,24]
    a=s[0:2]
    b=s[2:10]
    if "pm" in s:
        i=0
        while i<len(list):
            if list[i]==a:
                print(str(list1[i])+b)
            i=i+1
    else:
        print(s)
time(input().lower())