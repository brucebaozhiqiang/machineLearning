'''
created on 2016.08.19
@author: bzq
'''
import numpy as np
import operator

def createDataSet():
	group = np.array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels;

def classify0(inX, dataSet, labels,k):
	dataSetSize = dataSet.shape[0];
	diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axix = 1)
	sqlDistances = sqDistances ** 0.5
	
