import pandas as pd
df=pd.read_csv('Data.csv')
mean=df.mean()
df.fillna(mean,inplace=True)
print(df)