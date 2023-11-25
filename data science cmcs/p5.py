import pandas as pd
df=pd.read_csv('Data.csv')
print(df.head(2))
print(df.tail(2))
print(df.sample(2))