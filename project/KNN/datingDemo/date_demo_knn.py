# -*- coding: utf-8 -*-
'''		
created on 2016.08.19
@author: bzq
'''
import numpy as np
import operator

def createDataSet():
	group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels;

def classify0(inX, dataSet, labels,k):
	dataSetSize = dataSet.shape[0];
	diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteLabel = labels[sortedDistIndicies[i]]
		classCount[voteLabel] = classCount.get(voteLabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fr = open(filename)
	arrayOfLines = fr.readlines()
	numOfLines = len(arrayOfLines)
	returnMat = np.zeros((numOfLines, 3))
	classLabelVector = []
	index = 0
	for line in arrayOfLines:
		line = line.strip()  #去除每行后面的换行符
		listFromLine  = line.split('\t')
		returnMat[index:] = listFromLine[0:3]
		index += 1
		classLabelVector.append(int(listFromLine[-1]))
	return returnMat, classLabelVector

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	m = dataSet.shape[0]
	normDataSet = np.zeros(np.shape(dataSet))
	normDataSet = dataSet - np.tile(minVals,(m,1))
	normDataSet = normDataSet / np.tile(ranges, (m,1))
	return normDataSet,ranges,minVals;

def datingClassTest():
	hoRatio = 0.1
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print 'the classifier came back with: %d, the real answer is: %d' %(classifierResult,datingLabels[i])
		if(classifierResult != datingLabels[i]):
			errorCount += 1.0
		print 'total result is: %f' %(errorCount/ float(numTestVecs))

def classifyperson():
	resultList = ['not at all', 'in small does', 'in large does']
	input_man = [50000,20,1.5]
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	result = classify0((input_man - minVals)/ranges,normMat,datingLabels,3)
	print 'you will probably like this person:', resultList[result -1]

if __name__ == '__main__':
	#group,labels = createDataSet()
	#test = classify0([0.2,0.2],group,labels,3)
	#print test

	#datingClassTest()

	classifyperson()
