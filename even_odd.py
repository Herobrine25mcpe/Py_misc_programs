str = input("Enter String : ")

print("\nOriginal String :  ", str)

fstr = ""

for i in range(len(str)):
    
    if(i % 2 == 0):
        fstr = fstr + str[i]
        

print("Final String :     ", fstr)