f=""
a="akdfhj123oaidsr098"
abc="abcdefghijklmnopqrstuvwxyz"
num="0123456789"

for n in num:
    for i in a: 
        if(n==i):
            f=f+i

for i in range(0,len(num)):
    for j in f: 
        if(num[i]==j):
            print(num[i])

"""for j in abc:
    for i in a:               
        if(j==i):
            f=f+i"""
print(f)

