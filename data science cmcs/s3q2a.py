import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='sepal_length', data=df)
plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='sepal_width', data=df)
plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='petal_length', data=df)
plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='petal_width', data=df)

plt.suptitle('Distribution of Iris Features Across Species')
plt.show()