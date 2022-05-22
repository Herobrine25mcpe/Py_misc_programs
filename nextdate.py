import datetime
from datetime import timedelta 
 
d=int(input("Enter Day : "))
 
m=int(input("Month : "))
 
y=int(input("Year : "))
     
 
date = datetime.datetime(y, m, d) 
print("Given date is: ", date) 
    

next = date + timedelta(days = 1) 
print("Next date will be : ", next) 