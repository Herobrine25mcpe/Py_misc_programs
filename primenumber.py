flag = False 
def primenumber(n):
    for i in range(2,int((n/2)+1)):
        if (n%i==0):
            flag=True
            break

num = int(input("Enter a number"))

primenumber(num)

if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} the not prime number")