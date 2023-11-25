import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Data.csv')
plt.plot(df['name'],df['salary'])
plt.title('name vs salary')
plt.xlabel('name')
plt.ylabel('salary')
plt.show()