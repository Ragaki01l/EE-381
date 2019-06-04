#William Jorgensen
#014721822
# Start Date: 2/3/2019
# End Date: 2/6/2019

#This program outputs summary for inputted data

#def = data()

L = [] #list for the data
v = 1 #Boolean variable set to high logic

#Written in Python 3.7

import math
import collections


while v == 1:
	try:
		I = int(input("Enter a non-negative integer: "))
		L.append(I)
	except ValueError:
		print('Input has been stopped')
		print('\n')
		v = 0 #change logic state

print('You inputted a list of numbers', L)
print('\n')

#print('L[len(L)/2]')

def mean(L):
	mean = (sum(L)/len(L))
	return mean

def median(L):
	l = sorted(L)
	listLength = len(L)
	if listLength < 1:
		return print('There is no list') 
	if listLength % 2 == 0 :
		median = ( l[(listLength-1)//2] + l[(listLength+1)//2] ) // 2.0
		return median
	else:
		median = l[(listLength-1)//2]
		return median

def mode(L):
	mode = []
	c = collections.Counter(L)
	freq = c.most_common()
	maxOccur = freq[0][1]
	if maxOccur != 1:
		for m in freq:
			if m[1] == maxOccur:
				mode.append(m[0])
		print("The mode(s) are: ")
		for p in mode:
			print (str(p))
		print("With Frequence", maxOccur)
	else:
		print("There is no mode")
	
def calrange(L):
	l = sorted(L)
	range = l[len(L) - 1] - l[0]
	return range

def findVariance(L, M):
	S = 0 #Accumulator Value
	N = len(L)
	for n in L:
		x = (n - M) ** 2
		S = S + x
	Variance = S/N
#	print("Variance:  ", Variance)
	return Variance

def STD(X): #Calculating the standard deviation
	SD = math.sqrt(X)
	print("Standard Deviation = ", SD)
	return SD

calcMean = mean(L)
print('Mean: ',calcMean)
calcMedian = median(L)
print('Median: ', calcMedian)
mode(L)
calculateRan = calrange(L)
print('Range: ', calculateRan)
calcVariance = findVariance(L, calcMean)
print('Variance: ',calcVariance)
calcSTD = STD(findVariance(L, calcMean))



