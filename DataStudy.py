#-*- coding:utf-8 -*-
import jieba
import urllib
import sys
from jieba import analyse
import os
import jieba.posseg as pseg
import numpy as np
import numpy
import jieba.analyse
from sklearn import feature_extraction
#############################################################################
#############################将单个摘要分别分词保存#######################
WordCast=open('Cnki_label _abstruct2.csv', 'r')#CnkiLabelAbstruct.txt
ReadLines=WordCast.readlines()
JiebaCast=open('BitCnkiNOLabelAbstractJieba.txt', 'w')
stopwords = {}.fromkeys([line.rstrip() for line in open('StopWords.txt')])
for ReadLine in ReadLines:
    #print ReadLine[0]
    AbstractPart = jieba.analyse.extract_tags(ReadLine, topK=50, withWeight=False, allowPOS=())#1原来的数据，2，提取前20个，3权重是否显示，4，允许输出的词性
    segs = AbstractPart
    segs = [word.encode('utf-8') for word in list(segs)]
    segs = [word for word in list(segs) if word not in stopwords]

    for seg in segs:
        #if '\n' not in seg:
        JiebaCast.write('%s\t'%seg)
    # if len(segs)==1:
    #     JiebaCast.write('NA\n')
    JiebaCast.write('\n')
JiebaCast.close()
##########################################数据测试部分##############################

########################################################
##########################生成文本向量################
WordCast=open('DictionaryText.txt', 'r')#导入总词典向量
ReadLines=WordCast.readlines()
LabelOnly1=open('OnlyTable.txt', 'r')#导入标签向量
LabelOnly=LabelOnly1.readlines()
JiebaWordCast=open('BitCnkiNOLabelAbstractJieba.txt', 'r')#导入每个摘要分词后的词语，用于接下来生成每个摘要的向量
JiebaReadLines=JiebaWordCast.readlines()
DictionaryWriteNumber=0
VectorEachAbstract=open('VectorEachAbstract\%s.txt'%DictionaryWriteNumber, 'w')#将每个向量保存起来
DictionaryNumber=0

DictionaryTranslate={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
for JiebaText in JiebaReadLines:
    VectorAbstract = JiebaText.split("\t")
    TextVector = numpy.zeros([len(ReadLines)+1])
    for Vector in VectorAbstract:
        VectorPar=0
        for ReadLine in ReadLines:
            ReadLine = ReadLine.strip('\n')
            if  ReadLine == Vector :
                TextVector[VectorPar] = 1
                break
            VectorPar+=1
    if 'A' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['A']
    if 'B' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['B']
    if 'C' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['C']
    if 'D' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['D']
    if 'E' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['E']
    if 'F' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['F']
    if 'G' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['G']
    if 'H' in LabelOnly[DictionaryNumber]:
        TextVector[len(ReadLines)] = DictionaryTranslate['H']
    print DictionaryNumber
    DictionaryNumber+=1
    #if DictionaryNumber%500!=0:
    for Vector1 in TextVector:
        VectorEachAbstract.write('%s\t'%Vector1)
    VectorEachAbstract.write('\n')
    if DictionaryNumber%2000==0:
        DictionaryWriteNumber+=1
        VectorEachAbstract.close()
        VectorEachAbstract = open('VectorEachAbstract\%s.txt'%DictionaryWriteNumber, 'w')

WordCast.close()
LabelOnly1.close()
JiebaWordCast.close()
VectorEachAbstract.close()
#################################################################
#################################################################
##########标签提取，A B C D E F G H#############################
################################################################
WordCast=open('Cnki_label_abstruct.txt', 'r')#CnkiLabelAbstruct.txt
ReadLines=WordCast.readlines()
LineNumpy=[]
first_ele = True
LabelSelect=[]
WriteLines=open('LabelOnly.txt','w')
JiebaDictionary=[]
for ReadLine in ReadLines:
    ## 去掉每行的换行符，"\n"
    Data2 = ReadLine.strip('\n')
    Data3=Data2.strip(' ')
    LineNumpy = Data3.split("\t")
    LabelPart=LineNumpy[0]
    LineNumpy[0]=LabelPart[0:3]
    LabelSelect.append(LineNumpy)
    print LineNumpy[0]
    WriteLines.write('%s\n'%LineNumpy[0])

########################################################
#############方法1：直接分词，直接对词语标注############
# WordCast=open('test5.txt', 'r')
# ReadLines=WordCast.read()
# DictionaryJieba=jieba.cut(ReadLines)

    #print odom

    #print ReadLine
#print Read_lines
#############################################################################
##########################方法2：用TF*IDF，他是降低维度的一种方式################
WordCast=open('Cnki_label _abstruct2.csv', 'r')#CnkiLabelAbstruct.txt
ReadLines=WordCast.read()
keywords = jieba.analyse.extract_tags(ReadLines, topK=10000, withWeight=False, allowPOS=())#1原来的数据，2，提取前20个，3权重是否显示，4，允许输出的词性


import codecs
stopwords = {}.fromkeys([line.rstrip() for line in open('StopWords.txt')])
print keywords
segs = keywords
segs = [word.encode('utf-8') for word in list(segs)]
segs = [word for word in list(segs) if word not in stopwords]
DictionaryText=[]
WriteLines=open('DictionaryText.txt','w')
for seg in segs:
    WriteLines.write('%s\n'%seg)
    DictionaryText.append(seg)
    print seg


####WriteLines###########################################################################
