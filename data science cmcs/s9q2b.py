import matplotlib.pyplot as plt

# Create two lists representing subject names and marks obtained
subjects = ['Math', 'English', 'Science', 'History']
marks = [90, 85, 88, 92]

# Pie chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title('Marks Distribution by Subject')
plt.show()
