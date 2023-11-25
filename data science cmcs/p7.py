import numpy as np
import matplotlib.pyplot as plt
arr=np.random.randint(0,100,50)

#line chart
plt.subplot(2,2,1)
plt.plot(arr,color='blue', linestyle='--')
plt.title('line chart')

#scatter chart
plt.subplot(2,2,2)
plt.scatter(range(len(arr)),arr,color='green')
plt.title('scatter chart')

#histogram
plt.subplot(2,2,3)
plt.hist(arr,width=4,edgecolor='red',facecolor='blue')
plt.title('Histogram')

#box plot
plt.subplot(2,2,4)
plt.boxplot(arr,vert=False)
plt.show()