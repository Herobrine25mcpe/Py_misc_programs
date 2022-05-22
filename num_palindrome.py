
n=int(input("Enter a number:"))
x=n
rn=0
while n>0 :
    temp = n%10 
    rn = rn*10 + temp
    n=int(n/10)

if x==rn:
    print(f'{x} is  a palindrome')

else:
    print(f'{x} is not a palindrome')

