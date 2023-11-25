import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Iris.csv')

species_count=df['species'].value_counts()

plt.pie(species_count,labels=species_count.index,autopct='%1.1f%%')
plt.title("distribution")
plt.show()