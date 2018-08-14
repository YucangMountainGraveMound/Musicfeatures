#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from pylab import plot, show, figure
import matplotlib.pyplot as plt
import numpy as np
import shutil
import sys
from PyQt4.QtCore import *
#比例
def ratio(n,m):
	if(n==0 or m==0):
		return 0
	else:
		return n*1.0/m
#返回所有文件夹名
def getFileName(path):
	path = path.strip()
	path = path.rstrip('/')
	f_list = os.listdir(path)

	return f_list
#删除文件夹
def removeSVC(name):
	path1 = 'svcSystem/'+name
	path2 = 'dataSystem/'+name

	shutil.rmtree(path1)
	shutil.rmtree(path2)

#判断文件夹是否存在
def mkdir(path):
	path = path.strip()
	path = path.rstrip('/')

	isExists = os.path.exists(path)

	if not isExists :
		os.makedirs(path)
		print path + '创建成功'
		return True
	else :
		print  path +'已经存在'
		return False

#获取目录下所有文件(.mp3文件)
def getAllFile(path):
	path = path.strip()
	path = path.rstrip('/')

	f_list = os.listdir(path)
	files = []
	#print '总共有'+str(len(f_list))+'个文件'
	for  i in f_list:
		if os.path.splitext(i)[1] == '.mp3':
		#os.path.splitext(l)[1] 为．加后缀名．os.path.splitext(l)[０]为文件名
			files.append(path+'/'+i)

	return files

#获取目录下所有文件(.mp3文件)
def getAllFileWithoutPath(path):
	path = path.strip()
	path = path.rstrip('/')

	f_list = os.listdir(path)
	files = []
	#print '总共有'+str(len(f_list))+'个文件'
	for  i in f_list:
		if os.path.splitext(i)[1] == '.mp3':
		#os.path.splitext(l)[1] 为．加后缀名．os.path.splitext(l)[０]为文件名
			files.append(i)

	return files
#获取目录下所有文件数量(.mp3文件)
def getFileNum(path):
	path = path.strip()
	path = path.rstrip('/')
	print 'path:',path
	f_list = os.listdir(path)
	number = 0
	for  i in f_list:
		if os.path.splitext(i)[1] == '.mp3':
		#os.path.splitext(l)[1] 为．加后缀名．os.path.splitext(l)[０]为文件名
			number = number + 1

	return number
#获取文件夹下带有feature_的文件夹个数
def getFeatureDirName(path):
	path = path.strip()
	path = path.rstrip('/')
	num=0
	f_list = os.listdir(path)
	#print path
	for file in f_list:
		#print file
		if file.split('_')[0] == 'feature':
			if os.path.isdir(path+'/'+file):
				num = num + 1
	name = 'feature_'+str(num)
	#print name
	return name
	
#在轴上归一化:标准差归一化(平均值和标准差)
def testDataStandardNor(featureMatrix,meanData,stdData):
	for data in featureMatrix:
		for i in range(len(data)):
			if stdData[i]==0:
				data[i]=0
			else:
				data[i]=(data[i]-meanData[i])/stdData[i]
	return (meanData,stdData)
def trainDataStandardNor(featureMatrix):
	
	#print 'train_feature',featureMatrix
	meanData=featureMatrix.mean(axis=0) #平均值
	stdData=featureMatrix.std(axis=0) #标准差
	for data in featureMatrix:
		for i in range(len(data)):
			if stdData[i]==0:
				data[i]=0
			else:
				print data[i]
				data[i]=(data[i]-meanData[i])/stdData[i]

	return (meanData,stdData)
def testDataMax_MinNor(featureMatrix,maxData,minData):
	
	for data in featureMatrix:
		for i in range(len(data)):
			if maxData[i]-minData[i]==0:
				data[i]=0
			else:
				data[i]=(data[i]-minData[i])/(maxData[i]-minData[i])
	return (maxData,minData)
#在轴上归一化:最大最小归一化
def trainDataMax_MinNor(featureMatrix):
	
	minData=featureMatrix.min(axis=0) #平均值
	maxData=featureMatrix.max(axis=0) #标准差
	for data in featureMatrix:
		for i in range(len(data)):
			if maxData[i]-minData[i]==0:
				data[i]=0
			else:
				data[i]=(data[i]-minData[i])/(maxData[i]-minData[i])
	return (maxData,minData)
def showFeatureDetail(data,title):
	data = np.array(data)
	xNum,yNum = data.shape
	print xNum,yNum
	xAxis = np.linspace(20,40,yNum)
	plt.figure('SongDetail')
	plt.title(title)
	if xNum == 1:
		plt.plot(xAxis,data[0])
	else:
		for i in range(0,xNum):
			plt.plot(xAxis,data[i],label='data' + str(i) )
		
		plt.legend(loc = 'upper right')
	plt.show()

def getAllFileTxt(path):
	path = path.strip()
	path = path.rstrip('/')

	f_list = os.listdir(path)
	files = []
	#print '总共有'+str(len(f_list))+'个文件'
	for  i in f_list:
		if os.path.splitext(i)[1] == '.mp3':
		#os.path.splitext(l)[1] 为．加后缀名．os.path.splitext(l)[０]为文件名
			files.append(i)

	return files

if __name__ == '__main__':
	aa = getAllFileTxt('/home/chenming/Music/happy');
	f1 = open('/home/chenming/Music/happy/types.txt','a');
	for i in range(len(aa)):
		f1.write(aa[i] + '\n')


