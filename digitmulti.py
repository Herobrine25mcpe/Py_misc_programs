
dig=[]

n=int(input("Enter the number of digit: "))

for i in range(0,n):
    x=int(input(": "))
    dig.append(x)


mul = 1

for i in range(0,n):

    mul = mul * dig[i]

print(mul)
