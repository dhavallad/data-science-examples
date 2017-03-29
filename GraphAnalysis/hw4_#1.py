__author__ = 'Dhaval Lad'

import math

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
