'''
created on 2017.03.04
@author: bzq
'''
import numpy as np
import bayes


if __name__ == '__main__':
	# from numpy import *
	# 
	# listOPosts,listClasses=bayes.loadDataSet()
# 
	# myVocabList = bayes.createVocabList(listOPosts)
# 
	# print myVocabList
# 
	# trainMat=[]
# 
	# for postinDoc in listOPosts:
	# 	trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
	# p0V,p1V,pAb=bayes.trainNB0(trainMat,listClasses)
# 
	# #print pAb
	# print p1V

	bayes.spamTest()