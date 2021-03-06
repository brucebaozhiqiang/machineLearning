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
		line = line.trip()  #去除每行后面的换行符
		listFromLine  = line.split('\t')
		returnMat[index:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
	return returnMat, classLabelVector

if __name__ == '__main__':
	group,labels = createDataSet()
	test = classify0([0.2,0.2],group,labels,3)
	print test
