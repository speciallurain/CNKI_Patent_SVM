#-*- coding:utf-8 -*-
import numpy
import csv
# -*- coding: cp936 -*-
import numpy as np
import random
import matplotlib.pyplot as plt
import re
from os import listdir #读取整个目录的文件
import string
import sklearn
from sklearn import svm
Label=[]
Vector=[]
PartVector=[]
EvaluateFunctionResult=listdir('SVMTestPart')
for SingleFunction in EvaluateFunctionResult:
    print SingleFunction
    fr = open('SVMTestPart\%s' % SingleFunction)
    TotalLineCost = fr.readlines()
    fr.close()
    for LineCost in TotalLineCost:
        LineCost1=LineCost.strip()
        NumberLineCost=LineCost1.split('\t')
        if '2' in NumberLineCost[-1] or '4' in NumberLineCost[-1] or '8' in NumberLineCost[-1]:# or '8' in NumberLineCost[-1]:
            NumberLineCost1 = NumberLineCost[:501]#降维度
            Label.append(NumberLineCost[-1])
            PartVector.append(NumberLineCost1)
        #asvm详情请参见http://www.cnblogs.com/luyaoblog/p/6775342.html
        # 1.split(数据，分割位置，轴 = 1（水平分割） or 0（垂直分割）)。
        # 2.x = x[:, :2]是为方便后期画图更直观，故只取了前两列特征值向量训练。
        # 3.sklearn.model_selection.train_test_split随机划分训练集与测试集。train_test_split(train_data, train_target, test_size=数字,random_state=0)
        # 　　参数解释：
        # 　　train_data：所要划分的样本特征集
        # 　　train_target：所要划分的样本结果
        # 　　test_size：样本占比，如果是整数的话就是样本的数量
        # 　　random_state：是随机数的种子。
        # 　　随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。随机数的产生取决于种子，随机数和种子之间的关系遵从以下两个规则：种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。
Vector=PartVector
VectorTrain, VectorTest, LabelTrain, LabelTest = sklearn.model_selection.train_test_split(Vector, Label, random_state=1, train_size=0.8)
clf = svm.SVC(C=0.9, kernel='rbf', gamma=100, decision_function_shape='ovo')
clf.fit(VectorTrain, LabelTrain)
#  　　kernel='linear'时，为线性核，C越大分类效果越好，但有可能会过拟合（defaul C=1）。
# 　　 kernel='rbf'时（default），为高斯核，gamma值越小，分类界面越连续；gamma值越大，分类界面越“散”，分类效果越好，但有可能会过拟合。
# 　　decision_function_shape='ovr'时，为one v rest，即一个类别与其他类别进行划分，
# 　　decision_function_shape='ovo'时，为one v one，即将类别两两之间进行划分，用二分类的方法模拟多分类的结果。
print clf.score(VectorTrain, LabelTrain)  # 精度
print clf.score(VectorTest, LabelTest)
