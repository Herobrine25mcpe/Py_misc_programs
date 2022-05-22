str=str(input("Enter the string: "))

counter=0

for i in str:
    if i.isupper():
        counter= counter + 1
print("the number of upper letter is:",counter)