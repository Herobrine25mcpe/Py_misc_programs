Birthdays ={"Albert Einstein": "14/3/1889",
                "Bill Gates": "28/10/1955",
                "Steve Jobs": "24/2/1955"}
print('Welcome to the birthday dictionary.')
print(Birthdays)

query = input("Who's birthday do you want to look up?")

for k,v in Birthdays.items():
    if k == query:
        str=v
        temp=str.split("/")
        date="-".join(temp)
        print(date)
        break



    
