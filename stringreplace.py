str="Welcome to BIS hi there BIS class"

stf=""
i=0 

while i < len(str) :
    if (str[i]=="B" and str[i+1]=="I" and str[i+2]=="S"):
        if str[i+3]==" ":
            stf = stf + "BDA"
            i=i+3
              
    stf = stf +str[i]
    i=i+1
    
print(stf)