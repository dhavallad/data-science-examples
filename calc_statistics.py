__author__ = 'Dhaval Lad'

import math
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

def func_range(listNumbers):
	return min(listNumbers),max(listNumbers)

def func_mean(listNumbers):
	return sum(listNumbers)/len(listNumbers)

def func_median(listNumbers):
	data = sorted(listNumbers)
	n = len(data)
	if n == 0:
	    raise StatisticsError("Empty Data.")
	if n%2 == 1:
	    return data[n/2]
	else:
	    i = n/2
	    return (data[i - 1] + data[i])/2

def func_variance(listNumbers):
	m = func_mean(listNumbers)
	mylen = len(listNumbers)
	temp = 0
	for i in range(mylen):
		temp += (listNumbers[i] - m) * (listNumbers[i] - m) 
	return temp / mylen

def func_std_dev(listNumbers):
	no = func_variance(listNumbers)
	return math.sqrt(no)

def func_MAD(listNumbers):
	mean = func_mean(listNumbers)
	mylen = len(listNumbers)
	temp = 0
	for i in range(mylen):
		temp += abs(listNumbers[i]-mean)
	return temp / mylen

def func_histogram():
	alphab = [1,1,20,3,3,6,7,7,7,8,3,8,8,8,12,15,15,16,18,6]
	result_dict = dict( [ (i, alphab.count(i)) for i in set(alphab) ] )

	# print result_dict

	# ax = plt.axes()
	# ax.set_xlim(min(alphab),max(alphab))
	plt.hist(alphab,bins = 5)
	# plt.bar(pos, result_dict.values(),width, color='blue')
	plt.title("Histogram for 10 bins")
	plt.ylabel('Frequncy')
	plt.xlabel('Numbers')
	# plt.grid(True)
	plt.show()
	pass

def func_boxplot():
	data1 = [1,1,20,3,3,6,7,7,7,8,3,8,8,8,12,15,15,16,18,6]
	data2 = [9,10,11,12,12,15,16,16,16,17,17,18,18,18,18,22,25,25,26,28]
	# result_dict = dict( [ (i,alphab.count(i)) for i in set(alphab) ] )

	# print result_dict
	data = [data1,data2]
	boxplot(data)
	plt.show()
	pass


if __name__ == '__main__':
	theFile = open("input.txt", "r")
	theInts = []
	for val in theFile.read().split(','):
		theInts.append(float(val))
	theFile.close()

	print "Range:[%d,%d]" %func_range(theInts)
	print "Mean: %f" %func_mean(theInts)
	print "Median: %f" %func_median(theInts)
	print "Variance: %f" %func_variance(theInts)
	print "Standard Deviation: %f" %func_std_dev(theInts)
	print "Mean absolute deviation (MAD): %f" %func_MAD(theInts)
	func_histogram()
	func_boxplot()




