
# -*- coding: utf-8 -*-
'''
created on 2016.09.29
@author bzq
'''
from math import log

#获取矩阵标签的熵值
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCount = {}
	for featVec in dataSet:   #featVec: feature vector
		currentLabel = featVec[-1]
		if currentLabel not in labelCount.keys():
			labelCount[currentLabel] = 0
			labelCount[currentLabel] += 1
	shannonEnt = 0.0

	for key in labelCount:
		prob = float(labelCount[key])/numEntries
		shannonEnt -= prob * log(prob,2)
	return shannonEnt

#构造示例数据集
def createDataSet():
	dataSet = [ [1,1,'yes'],
				[1,0,'yes'],
				[0,1,'no'],
				[0,1,'no'],
				[0,1,'no']
				]
	labels = {'no','yes'}
	return dataSet, labels

#数据切分
def splitDataSet(dataSet, axis, value):
	retDataSet= []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0 
    bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntroy = 0.0
        for value in uniqueVals:
        	subDataSet = splitDataSet(dataSet, i, value)
        	prob = len(subDataSet)/ float(len(dataSet))


        







if __name__ == '__main__':
	dataSet, labels = createDataSet()
	#print calcShannonEnt(dataSet)
	chooseBestFeatureToSplit(dataSet)




