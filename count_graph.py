import seaborn as sns
import numpy as np
with open('labels.csv', 'r') as f:
	f.readline() # get the labels off
	data = []
	for line in f.readlines():
		data.append(line.split(',')[1])
	ax= sns.countplot(x=data)
	sns.plt.show()