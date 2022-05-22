import pandas as pd
import matplotlib.pyplot as plt

data = {
  "calories": [420, 380, 390 , 330,222],
  "duration": [50, 40, 45, 35, 25]
}

datax={  "calories": 420,"duration": 50,}

df = pd.DataFrame(data,index = ["day1", "day2", "day3", "day4","day5"])

sf=pd.Series(datax)

print(sf,"\n")
print(df,"\n") 

print(df.loc["day1"],"\n")

print(df.iloc[2],"\n") 

df.to_csv('calories.csv')

File=pd.read_csv('calories.csv')

print(File)

File.plot( kind="scatter",x="duration",y="calories")

plt.show()