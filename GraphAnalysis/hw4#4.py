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

def density_map():
	"""
    This function draw to ouptut.svg about avg age of Unites States regions.
    """
	average_age = {}
	zipcode_list  = json.loads(open('zip.txt','r').read())
	min_value = 100; max_value = 0
	reader = csv.reader(open('dataset.txt'), delimiter=",")
	for row in reader:
	    try:	      
	        pincode = random.choice(zipcode_list)
	        avgAge = int(row[0])
	        average_age[str(pincode)] = avgAge
	        zipcode_list.remove(pincode)
	        if avgAge > max_value:
	            max_value = avgAge
	        if avgAge < min_value:
	            min_value = avgAge
	    except:
	        pass
	# Colours List
	colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
	
	# Load the SVG map
	svg = open('USA_Counties_with_FIPS_and_names.svg', 'r').read()
	soup = BeautifulSoup(svg)
	paths = soup.findAll('path')

	# Change colors accordingly
	path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
	for p in paths:
	    
	    if p['id'] not in ["State_Lines", "separator"]:
	        
	        try:
	            avgAge = average_age[p['id']]
	        except:
	            continue
	            
	        if avgAge > 50:
	            color_class = 5
	        elif avgAge > 40:
	            color_class = 4
	        elif avgAge > 30:
	            color_class = 3
	        elif avgAge > 20:
	            color_class = 2
	        elif avgAge > 10:
	            color_class = 1
	        else:
	            color_class = 0


	        color = colors[color_class]
	        p['style'] = path_style + color
	# Write to output.svg file        
	with open('output.svg', 'w') as file_:
	    file_.write(soup.prettify())


def parallel_coordinate():
	"""
    This function draw to plot between the Age,Education,Profit,Loss and Hours/week to show how they are related.
    """
	data = pandas.read_csv('dataset.txt', sep=',', header=None, names=['Age','JobType','Other','Education','Education_Score','Relationship','Position','Status','Race','Sex','Profit','Loss','Hours/Week','Country','Income'])
	#print data
	# data = data.drop('Age', 1)
	data = data.drop('JobType', 1)
	data = data.drop('Other', 1)
	# data = data.drop('Education', 1)
	data = data.drop('Education_Score', 1)
	data = data.drop('Relationship', 1)
	data = data.drop('Position', 1)
	data = data.drop('Status', 1)
	data = data.drop('Race', 1)
	data = data.drop('Sex', 1)
	# data = data.drop('Profit', 1)
	# data = data.drop('Loss', 1)
	# data = data.drop('Hours/Week', 1)
	data = data.drop('Country', 1)
	data = data.drop('Income', 1)

	parallel_coordinates(data[:50], 'Education')
	plt.show()

def matrix_coorelation():
	"""
    This function draw plot to all numeric values of datasets to show relation. 
    """
	data = pandas.read_csv('dataset.txt', sep=',', header=None)
	sns.heatmap(data.corr(),square= True)
	plt.show()



if __name__ == '__main__':
     data_statistics()
     print "---Histogram----"
     plot_histogram()
     print "---Scatter Plot----"
     scatterplot()
     print "---Box Plot----"
     boxplot()
     print "---Density Map----"
     density_map()
     print "---Parallel Coordinate Map----"
     parallel_coordinate()
     print "---Matrix Corelation Map----"
     matrix_coorelation()