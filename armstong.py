n=int(input("Enter a number:"))
x=n
rn=0
while n>0 :
    temp = n%10 
    rn = rn + temp**3
    n=n//10

if x==rn:
    print(f'{x} is a armstrong')

else:
    print(f'{x} is not a armstrong')