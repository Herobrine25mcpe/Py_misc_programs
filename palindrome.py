
s = (input("Enter a number:"))
flag=True

for i in range(0, int(len(s)/2)):
    if s[i] != s[len(s)-i-1]:
        flag=False

if flag==False:
    print(f'{s} is not a palindrome')

else:
    print(f'{s} is a palindrome')




