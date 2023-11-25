import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv')

sns.scatterplot(x='petal_length', y='petal_width', data=df, hue='species', palette='viridis', s=70)
plt.title('Relationship between Petal Length and Petal Width')
plt.xlabel('Petal Length ')
plt.ylabel('Petal Width')
plt.legend()
plt.show()
