__author__ = 'Dhaval Lad'


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import csv,json,random,pandas
from pandas.tools.plotting import parallel_coordinates
from BeautifulSoup import BeautifulSoup
import seaborn as sns

# import other file to use statistics function in hw4#123
funFile = __import__('hw4#123')


def data_statistics():
	"""
	This function calcualte the simple statistics.
	"""
	data = []
	with open('dataset.txt') as f:
		for line in f.readlines():
			items=[]
			for item in line.split(','):
				items.append(item)
			data.append(items)
	age = []
	age = [ int(items[0]) for items in data]
	print "------Summary of statistics--------"
	print "	Minimun Age, Maximum Age: %d, %d " %funFile.func_range(age)
	print "	Mean of Age: %f" %funFile.func_mean(age)
	print "	Median of Age: %f" %funFile.func_median(age)
	print "	Variance of Age: %f" %funFile.func_variance(age)
	print "	Standard Deviation of Age: %f" %funFile.func_std_dev(age)
	print "	Mean absolute deviation (MAD) of Age: %f" %funFile.func_MAD(age)



def plot_histogram():
	"""
	This function simply draw histogram for the what type of work most of people do.
	"""

	def tfword(w,data_dict):
		if w in data_dict:
			data_dict[w]+=1
		else:
			data_dict[w]=1

	data_dict={}
	data=[]
	with open('dataset.txt') as f:
		for line in f.readlines():
			items=[]
			for item in line.split(','):
				items.append(item)
			data.append(items)
	flt_data = [ [items[1]] for items in data]
	for item in flt_data:
		tfword(item[0],data_dict)

	data=[]
	for v in data_dict.values():
		data.append(int(v))


	yAxis = np.arange(len(data))
	plt.barh(yAxis, data,  align='center', alpha=0.4)
	plt.yticks(yAxis, data_dict.keys())
	plt.xlabel('Count')
	plt.title('What type work people do?')
	plt.show()

def scatterplot():
	"""
    This function draw the scatter plot for Age->Salary.
    """
	xAge=[]
	ySalary=[]

	reader = csv.reader(open('dataset.txt'), delimiter=",")
	for row in reader:
		xAge.append(row[0])
		ySalary.append(row[12])
	# print xAge     
	      
	     
	plt.scatter(xAge, ySalary, alpha=0.5)
	plt.xlabel('Age')
	plt.ylabel('Hours per Week')
	plt.title('Scatter Example - Age vs hours per week.')
	plt.show()


def boxplot():
	"""
    This function draw boxplot for Age.
    """
	data = []
	reader = csv.reader(open('dataset.txt'), delimiter=",")
	for row in reader:
	    data.append(int(row[0]))
	# print data
	
	# plt.figure()
	plt.boxplot(data,0,'rs',0,0.75)
	plt.title("Boxplot for Age")
	plt.xlabel("Age")
	plt.show()


if __name__ == '__main__':
     data_statistics()
     print "---Histogram----"
     plot_histogram()
     print "---Scatter Plot----"
     scatterplot()
     print "---Box Plot----"
     boxplot()