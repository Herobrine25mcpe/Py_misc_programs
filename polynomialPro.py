import math

print(" Which degree of polynomial would you like to calculate\n 1. degree 2 \n 2. degree 3")
p=int(input("Enter choice 1 or 2: "))

if p==1:
    print("Enter the coefficients of the form ax^2 + bx + c\n")

    lst=[]
    arr=["a","b","c"]

    for i in range(0,3):

        a=int(input(f'Enter coefficient "{arr[i]}":')) 
        lst.append(a)

    x=int(input("""\nEnter the value of "x":"""))
    sum=0
    j=2

    for i in range(0,2):
        while(j>0):
            sum=sum+(lst[i]*math.pow(x,j))  
            break
        j=j-1
    sum=sum+lst[2] 
    print("\nThe value of the polynomial is:",sum)

else:
    print("Enter the coefficients of the form ax^3 + bx^2 + cx + d\n")

    lst=[]
    arr=["a","b","c","d"]

    for i in range(0,4):

        a=int(input(f'Enter coefficient "{arr[i]}":')) 
        lst.append(a)

    x=int(input("""\nEnter the value of "x":"""))
    sum=0
    j=3

    for i in range(0,3):
        while(j>0):
            sum=sum+(lst[i]*math.pow(x,j))  
            break
        j=j-1
    sum=sum+lst[3] 
    print("\nThe value of the polynomial is:",sum)

print("\nThank you! Abhay Tomer 20BCS3566")