# -*- coding: utf-8 -*-
'''
created on 2016.09.28
@author: bzq
'''
import numpy as np
import operator
from os import listdir

def createDataSet():
	group = np.array([[1.0,1.1],
					  [1.0,1.0],
					  [0,0],
					  [0,0.1]])
	labels = ['A','A','B','B']
	return group, labels;

group, label = createDataSet()

minVals = group.min(0)

print minVals

maxVals = group.max(0)

print maxVals

dirlist = listdir('testDigits')
print dirlist
