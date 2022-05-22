lt=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
count=0
flt=[]
for i in lt:
   if i!= 0:
      flt.append(i)
   else:
      count+=1

print(flt)
print(count)

while (count>0):
   flt.append(0)
   count= count - 1


print(flt)



   