import matplotlib.pyplot as plt 

# defining labels 
activities = ['eat', 'sleep', 'Work', 'Entertainment',"Cleaning"] 

# portion covered by each label 
slices = [3, 5, 6, 4,3] 

# color for each label 
colors = ['r', 'y', 'g', 'b','c'] 

# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors, 
		startangle=90, explode = (0, 0.3, 0.4, 0.2,0.1), 
		radius = 1.2, autopct = '%1.0f%%') 

# plotting legend a
plt.legend() 

# showing the plot 
plt.show() 
