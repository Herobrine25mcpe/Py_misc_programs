
S= "girl you know i want your love your love was handmade for somebody like me Come on now follow my lead Come come on now follow my lead"

d= dict()

word= S.split()

for n in word:
    if n in d:
        d[n]+=1 # new entry in the dict
    else:
        d[n] = 1 # updating the dict
    
print (d)