
# -*- coding: utf-8 -*-
'''
created on 2016.09.29
@author bzq
'''
from math import log
import  operator

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
        	newEntroy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntroy
        if(infoGain > bestInfoGain):
        	bestInfoGain = infoGain
        	bestFeature = i
    return bestFeature

def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]  #当所有结果都一样的时候
	if len(dataSet[0]) == 1:
		return majorityCnt(classList) #只有一个特征的时候
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
	return myTree



        







if __name__ == '__main__':
	dataSet, labels = createDataSet()
	#print calcShannonEnt(dataSet)
	chooseBestFeatureToSplit(dataSet)




