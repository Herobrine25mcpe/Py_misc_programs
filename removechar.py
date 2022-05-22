st=str(input("enter the string: "))

key=str(input("Enter key character: "))

for i in range(0,len(st)):
   if st[i]== key:
      print( st[i], end="")
