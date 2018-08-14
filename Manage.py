#!/usr/bin/python
# -*- coding: utf-8 -*-


import TrainAndTest as tat
import YaafeExtract as yl
import WriteFeatures as wf
import Tools as tool
import ExtractFeature as extra
import os
import numpy as np

feature = []
num = []
train_path = []
train_mode = []
test_path = []
test_mode = []

common = [0, 1, 6, 7, 19, 20, 21, 22, 23, 29, 30]
emotion = range(0, 34)
rock = [0, 1, 6, 7, 11, 14, 15, 16, 19, 20, 21, 22, 23, 29, 30]
opera = [0, 1, 4, 6, 7, 19, 20, 21, 22, 23, 29, 30, 33]
jazz = [0, 1, 6, 7, 12, 19, 20, 21, 22, 23, 27, 28, 29, 30]
happy = [0, 1, 4, 6, 7, 9, 10, 15, 19, 20, 21, 22, 23, 29, 30, 31, 32, 34]
sad = [0, 1, 2, 6, 7, 19, 20, 21, 22, 23, 29, 30]
person = [0, 1, 3, 4, 10, 13, 19, 20, 21, 25, 27, 28]

# 设置分类算法
def setClassifier(classify='svm'):
	# print 'svm,knn,tree'
	tat.setClassifier(classify)


# ===========================================================================


def readSelectedTestData(test_path, test_mode):
	# 获得测试类型的代码,代码根据输入类别的数组确定
	test_code = []
	for i in range(len(test_mode)):
		for j in range(len(train_mode)):
			if train_mode[j] == test_mode[i]:
				test_code.append(j)
	test_data, test_target = extra.readSelectedTestData(test_path, test_mode, test_code)
	return test_data, test_target


# =============================================================================
def readTrainData(train_path, train_mode):
	train_data, train_target = extra.readTrainData(train_path, train_mode)
	return train_data, train_target

def readSelectedTrainData(data_file, test_mo):
	return extra.readSelectedTrainData(data_file, test_mo)

# 读取已有特征
def readTestData(train_mode, test_path, test_mode):
	# 获得测试类型的代码,代码根据输入类别的数组确定
	test_code = []
	for i in range(len(test_mode)):
		for j in range(len(train_mode)):
			if train_mode[j] == test_mode[i]:
				test_code.append(j)
	test_data, test_target = extra.readTestData(test_path, test_mode, test_code)

	return test_data, test_target


# ============================================================================
# 提取特征数据
def extraTrainData(train_path, train_mode, mode_name, featureList):
	train_data, train_target = extra.getTrainData(train_path, train_mode, mode_name, featureList)
	return train_data, train_target

def extraTestData(test_path, test_mode, mode_name):
	# 获得测试类型的代码,代码根据输入类别的数组确定
	test_code = []
	train_mode = wf.readFileTxt('dataSystem/' + mode_name + '/modeList.txt')

	for i in range(len(test_mode)):
		for j in range(len(train_mode)):
			if train_mode[j] == test_mode[i]:
				test_code.append(j)


	test_data, test_target, allUseFeature = extra.getTestData(test_path, test_mode, test_code, mode_name)
	return test_data, test_target, allUseFeature


# +==============================================================================
# 初始化软件
def preExtraData():
	extra.initSoft()

# ==============================================================================
# 数据预处理,开始训练和测试
def train(train_data, train_target, train_mode, mode_name):
	return tat.train(train_data, train_target, train_mode, mode_name)


def test(test_data, test_target, test_mode, mode_name):
	return tat.test(test_data, test_target, test_mode, mode_name)

# =================================================================================
def testSong(path, one_mode=None, train_data=None, train_target=None, train_mode=None):
    if one_mode == None:
        print 'error mode'
        return
    extra.initSoft()
    if one_mode == 'emotion':
        test_data = extra.getOneSongData(path, emotion)
    else:
        test_data = extra.getOneSongData(path, emotion)
    return tat.testBydefualtData(test_data, one_mode)

def testAllSong(path, one_mode=None, data_fi=None):
    data_file = []
    test_mo = ['happy',]
    data_file.append(data_fi)

    if one_mode == None:
        print 'error mode'
        return
    extra.initSoft()
    if one_mode == 'emotion':
        test_data ,train_target = extra.readSelectedTrainData(data_file, test_mo)
    else:
        test_data ,train_target = extra.readSelectedTrainData(data_file, test_mo)

    files = tool.getAllFileWithoutPath(path)
    return tat.testAlldefualtData(test_data, one_mode, files, path)


def showSongDetail(path, featureName):
	way, name = os.path.split(path)
	#	modeName = name.split('.')[0]
	title = featureName + ' for ' + name + ' in 20 - 40'
	data = extra.getOriginFeature(path, featureName)
	print data
	tool.showFeatureDetail(data, featureName)

def train_test(train_data,train_target,test_data,test_target):

	tat.train_test(train_data,train_target,test_data,test_target)
def help():
	print'''
	提取特征软件		特征			统计值		维数		索引标识

	YAAFE:
				MFCC:
							MAX				13		0
							MEDIAN			13		1
							MEAN			13		2
							VAR				13		3
				MFCC_D1:
							MAX				13		4
				ZCR:
							MEAN			1		5
							VAR				1		6
				LPC:
							MEAN			2		7
							VAR				2		8
				ENERGY:
							MEAN			1		9
							VAR				1		10
				SHARPNESS:
							MEAN			1		11
							VAR				1		12
				LSF:
							MEAN			10		13
				SPECTRALFLATNESS:
							MEAN			1		14
							VAR				1		15
				SPECTRALROLLOFF:
							MEAN			1		16
							VAR				1		17

	ESSENTIA:
				ZCR:
							ZCR				1		18
				LOUDNESS:
							LOUDNESS		1		19
				INHARMONICITY:
							INHARMONICITY	1		20
				PITCHSALIENCE:
							PITCHSALIENCE	1		21
				PITCH:
							MAX				1		22
							MIN				1		23
							MEAN			1		24
							VAR				1		25
							MEDIAN			1		26
				TUNINGFREQUENCY:
							TUNINGFREQUENCY	1		27
							TUNINGCENTS		1		28
				BEATOFLOUDNESS:
							NUM				1		29
							MAX				1		30
							MIN				1		31
							MEAN			1		32
							VAR				1		33
							MEDIAN			1		34

	'''
	print 'addfeature:()参数使用1,2,3...'
	print 'setClassifier()参数使用[svm,knn,tree]'
	print 'setSong(第二个参数类型)classic opera jazz rock happy sad'
	print 'showSongDetail()参数使用zcr,sharpness ,lpc ,lsf,spectralRolloff ,spectralFlatness ,mfcc_d1,mfcc,pitch,beat'
	print '音乐所在路径下生成文件夹保存音乐特征数据'


