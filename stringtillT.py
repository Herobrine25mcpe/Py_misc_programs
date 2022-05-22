
str=input("Enter the strings: ")

for i in range(0,len(str)):
    if (str[i] == "t"):
        print("t encountered")
        break
    print(str[i])