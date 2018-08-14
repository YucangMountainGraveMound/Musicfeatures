#!/usr/bin/python
# -*- coding: utf-8 -*-

import YaafeExtract as yl
import EssentiaExtract as el
import WriteFeatures as wf
import numpy as np
import Tools as tool
import os

FEATURES = [['MFCC最大值', '13', ], ['MFCC中位值', '13'], ['MFCC平均值', '13'], ['MFCC方差', '13'], ['MFCC_d1最大值', '13'],
            ['ZCR平均值', '1'], ['ZCR方差', '1'], ['LPC平均值', '2'], ['LPC方差', '2'], ['ENERGY平均值', '1'], ['ENERGY方差', '1'],
            ['SHARPNESS平均值', '1'], ['SHARPNESS方差', '1'], ['LSF平均值', '10'], ['SPECTRALFLATNESS平均值', '1'],
            ['SPECTRALFLATNESS方差', '1'], ['SPECTRALROLLOFF平均值', '1'], ['SPECTRALROLLOFF方差', '1'], ['ESSENTIA ZCR', '1'],
            ['LOUDNESS', '1'], ['INHARMONICITY', '1'], ['PITCHSAILENCE', '1'], ['PITCH最大值', '1'], ['PITCH最小值', '1'],
            ['PITCH平均值', '1'], ['PITCH方差', '1'], ['PITCH中位值', '1'], ['TUNINGFREQUENCY基频', '1'],
            ['TUNINGCENTS基频偏差', '1'], ['BEATOFLOUDNESS节拍响度数量', '1'], ['BEATOFLOUDNESS节拍响度最大值', '1'],
            ['BEATOFLOUDNESS节拍响度最小值', '1'], ['BEATOFLOUDNESS节拍响度平均值', '1'], ['BEATOFLOUDNESS节拍响度方差', '1'],
            ['BEATOFLOUDNESS节拍响度中位值', '1']]

def initSoft():
    # yaafe初始化
    yl.initYaafe()
    # essentia初始化
    el.initEssentia()

def getOriginFeature(path, featureName):
    yl.initYaafe()
    el.initEssentia()
    yl.startEngine(path)
    el.startLoader(path)
    array = []
    if featureName == 'beat' or featureName == 'pitch':
        array = el.getFeature(featureName)
    else:
        array = yl.getFeature(featureName)

    return array


def getFeature(yl, el, featureList):
    introFeature = []
    extraFeature = []

    # featureList = list(set(featureList))
    for fe in range(len(featureList)):
        f = int(featureList[fe])
        introFeature.append(FEATURES[f])
        # 0-3
        if f < 4 and f > -1:
            mfccMax, mfccMedian, mfccMean, mfccVar = yl.getMFCC()
            if f == 0:
                for data0 in mfccMax:
                    extraFeature.append(data0)
            if f == 1:
                for data1 in mfccMedian:
                    extraFeature.append(data1)
            if f == 2:
                for data2 in mfccMean:
                    extraFeature.append(data2)
            if f == 3:
                for data3 in mfccVar:
                    extraFeature.append(data3)
        # 4
        if f == 4:
            mfcc_d1Max = yl.getMfcc_d1()
            for data4 in mfcc_d1Max:
                extraFeature.append(data4)
        # 5-6
        if f < 7 and f > 4:
            zcrMean, zcrVar = yl.getZCR()
            if f == 5:
                for data5 in zcrMean:
                    extraFeature.append(data5)
            if f == 6:
                for data6 in zcrVar:
                    extraFeature.append(data6)
        # 7-8
        if f < 9 and f > 6:
            lpcMean, lpcVar = yl.getLPC()
            if f == 7:
                for data7 in lpcMean:
                    extraFeature.append(data7)
            if f == 8:
                for data8 in lpcVar:
                    extraFeature.append(data8)
        # 9-10
        if f < 11 and f > 8:
            energyMean, energyVar = yl.getEnergy()
            if f == 9:
                for data9 in energyMean:
                    extraFeature.append(data9)
            if f == 10:
                for data10 in energyVar:
                    extraFeature.append(data10)
        # 11-12
        if f < 13 and f > 10:
            sharpnessMean, sharpnessVar = yl.getSharpness()
            if f == 11:
                for data11 in sharpnessMean:
                    extraFeature.append(data11)
            if f == 12:
                for data12 in sharpnessVar:
                    extraFeature.append(data12)
        # 13
        if f == 13:
            lsfMean = yl.getLSF()
            for data13 in lsfMean:
                extraFeature.append(data13)
        # 14-15
        if f < 16 and f > 13:
            spectralFlatnessMean, spectralFlatnessVar = yl.getSpectraFlatness()
            if f == 14:
                for data14 in spectralFlatnessMean:
                    extraFeature.append(data14)
            if f == 15:
                for data15 in spectralFlatnessVar:
                    extraFeature.append(data15)
        # 16-17
        if f < 18 and f > 15:
            spectralRolloffMean, spectralRolloffVar = yl.getSpectralRolloff()
            if f == 16:
                for data16 in spectralRolloffMean:
                    extraFeature.append(data16)
            if f == 17:
                for data17 in spectralRolloffVar:
                    extraFeature.append(data17)
        # 18
        if f == 18:
            zcr = el.getZCR()
            extraFeature.append(zcr)
        # 19
        if f == 19:
            ln = el.getLoudness()
            extraFeature.append(ln)
        # 20
        if f == 20:
            inharmonicity = el.getInharmonicity()
            extraFeature.append(inharmonicity)
        # 21
        if f == 21:
            pitchSalience = el.getPitchSalience()
            extraFeature.append(pitchSalience)
        # 22-26
        if f < 27 and f > 21:
            pitchMax, pitchMin, pitchMean, pitchVar, pitchMedian = el.getPitch()
            if f == 22:
                # for data22 in pitchMax:
                # float
                extraFeature.append(pitchMax)
            if f == 23:
                # for data23 in pitchMin:
                extraFeature.append(pitchMin)
            if f == 24:
                # for data24 in pitchMean:
                extraFeature.append(pitchMean)
            if f == 25:
                # for data25 in pitchVar:
                extraFeature.append(pitchVar)
            if f == 26:
                # for data26 in pitchMedian:
                extraFeature.append(pitchMedian)
        # 27-28
        if f < 29 and f > 26:
            tuningFrequency, tuningCents = el.getTuningFrequency()
            if f == 27:
                # for data27 in tuningFrequency:
                # float
                extraFeature.append(tuningFrequency)
            if f == 28:
                # for data28 in tuningCents:
                extraFeature.append(tuningCents)
        # 29-34
        if f < 35 and f > 28:
            lnNum, lnMax, lnMin, lnMean, lnVar, lnMedian = el.getBeat()
            if f == 29:
                # for data29 in lnNum:
                extraFeature.append(lnNum)
            if f == 30:
                # for data30 in lnMax:
                extraFeature.append(lnMax)
            if f == 31:
                # for data31 in lnMin:
                extraFeature.append(lnMin)
            if f == 32:
                # for data32 in lnMean:
                extraFeature.append(lnMean)
            if f == 33:
                # for data33 in lnVar:
                extraFeature.append(lnVar)
            if f == 34:
                # for data34 in lnMedian:
                extraFeature.append(lnMedian)

    return extraFeature, introFeature

# ================================================================================================
# 得到训练数据
def getTrainData(train_path, train_mode, mode_name, featureList):
    num = []
    train_data = []
    train_target = []
    introFeature = []

    for i in range(len(train_mode)):
        allFeature = []
        # print len(train_mode),len(train_path),i,train_path[0],train_path[1]
        # print tool.getFileNum(train_path[i])
        num.append(tool.getFileNum(train_path[i]))
        for j in tool.getAllFile(train_path[i]):
            yl.startEngine(j)
            el.startLoader(j)
            oneFeature, introFeature = getFeature(yl, el, featureList)

            allFeature.append(oneFeature)
        # print allFeature

        # 判断是否有歌曲的特征被提取出
        if len(allFeature) == 0:
            print '无音频文件'
        else:
            wf.setMode(train_mode[i])  # 设置类别和目录．输出
            wf.setFeaturePrintPath(train_path[i])  # 音乐目录/feature_num/train_mode[i].txt  readme.txt
            wf.writeFeature(allFeature, introFeature)
            tool.mkdir('dataSystem/' + mode_name)
            wf.writeDetial('dataSystem/' + mode_name + '/feature.txt', featureList)
        for singleFeature in allFeature:
            train_data.append(singleFeature)  # 设置训练数据
            train_target.append(i)  # 设置训练目标

    return train_data, train_target

# 得到测试数据
def getTestData(test_path, test_mode, test_code, mode_name):
    test_target = []
    test_data = []
    introFeature = []
    print mode_name

    featureList = wf.readFileTxt('dataSystem/' + mode_name + '/feature.txt')

    for i in range(len(test_path)):
        allFeature = []
        print 'test_path', test_path
        test_num = tool.getFileNum(test_path[i])
        for j in tool.getAllFile(test_path[i]):
            yl.startEngine(j)
            el.startLoader(j)
            oneFeature, introFeature = getFeature(yl, el, featureList)
            # 将一首歌20s-40s里的数据放入数组的一个元素中
            allFeature.append(oneFeature)


        # 判断是否有歌曲的特征被提取出
        if len(allFeature) == 0:
            print '无音频文件'
        else:
            wf.setMode(test_mode[i])  # 设置类别和目录．输出
            wf.setFeaturePrintPath(test_path[i]) # 音乐目录/feature_num/mode.txt  readme.txt
            wf.writeFeature(allFeature, introFeature)
        for singleFeature in allFeature:
            test_data.append(singleFeature)  # 得到测试数据
            test_target.append(test_code[i])  # 得到测试目标代码

    allUseFeature = ''
    for k in range(len(introFeature)):
        allUseFeature = allUseFeature + '特征:%s\t维数:%s\n' % (introFeature[k][0], introFeature[k][1])

    return test_data, test_target, allUseFeature

# ============================================================================================
# 读取训练数据
def readTrainData(train_path, train_mode):
    train_data = []
    train_target = []
    for i in range(len(train_path)):

        path = train_path[i]
        path = path.strip()
        # path = path.rstrip('/')
        # newPath = path + '/' + train_mode[i] + '.txt'
        data = np.loadtxt(path)
        for k in range(len(data)):
            train_data.append(data[k])
            train_target.append(i)

    return train_data, train_target

# 读取测试数据
def readTestData(test_path, test_mode, test_code):
    test_data = []
    test_target = []
    for i in range(len(test_path)):

        path = test_path[i]
        path = path.strip()
        # path = path.strip('/')
        # path = path + test_mode[i] + '.txt'
        data = np.loadtxt(path)
        for k in range(len(data)):
            test_data.append(data[k])
            test_target.append(test_code[i])
    return test_data, test_target

# =============================================================================================
#写入单首歌的数据
def getOneSongData(spath, featureList):
    test_data = []
    yl.startEngine(spath)
    el.startLoader(spath)
    getdata, introFeature = getFeature(yl, el, featureList)
    test_data.append(getdata)

    way, name = os.path.split(spath)
    modeName = name.split('.')[0]
    wf.setMode(modeName)  # 设置类别和目录．输出
    wf.setFeaturePrintPath(way)
    wf.writeFeature(test_data, introFeature)
    return test_data

def getAllSongData(test_path, featureList):
    test_data = []

    print 'test_path', test_path
    test_num = tool.getFileNum(test_path)
    for j in tool.getAllFile(test_path):
        yl.startEngine(j)
        el.startLoader(j)
        oneFeature, introFeature = getFeature(yl, el, featureList)
        # 将一首歌20s-40s里的数据放入数组的一个元素中
        test_data.append(oneFeature)
    return test_data


#读取单首歌数据
def readOneSongData(path):
    test_data = []
    readdata = np.loadtxt(path)
    test_data.append(readdata)
    return test_data

# ===============================================================================================
# 自己改动用
def readSelectedTestData(test_path, test_mode, test_code):
    test_data = []
    test_target = []
    for k in range(len(test_path)):

        path = test_path[k]
        path = path.strip()
        # path = path.strip('/')
        # path = path + test_mode[i] + '.txt'
        data = np.loadtxt(path)
        for i in range(len(data)):

            index = []

            # yes
            # mfcc max
            for a1 in range(0, 13):
                index.append(data[i][a1])

            # yes
            # mfcc median
            for a2 in range(13, 26):
                index.append(data[i][a2])
            '''
			#yes
			#mfcc mean
			for a3 in range(26,39):
				index.append(data[i][a3])


			#no
			#mfcc var
			for a4 in range(39,52):
				index.append(data[i][a4])


			#yes
			#mfcc_d1 max
			for a5 in range(52,65):
				index.append(data[i][a5])


			#zcr mean var
			for a6 in range(65,67):
				index.append(data[i][a6])
			'''
            #			index.append(data[i][65])
            index.append(data[i][66])
            index.append(data[i][67])
            index.append(data[i][68])
            #			index.append(data[i][69])
            #			index.append(data[i][70])
            #			index.append(data[i][72])
            #			index.append(data[i][71])
            #			index.append(data[i][73])
            #			index.append(data[i][74])

            '''
			#lpc mean var
			#mean rock up,sad down
			#var jazz opera  happy rock up ,classic sad down
			for a7 in range(67,71):
				index.append(data[i][a7])

			#energy mean var
			#mean classic opera sad up ,other down
			#var up
			for a8 in range(71,73):
				index.append(data[i][a8])

			#sharpness mean var
			for a9 in range(73,75):
				index.append(data[i][a9])

			#lsf mean
			for a10 in range(75,85):
				index.append(data[i][a10])

			'''
            #			index.append(data[i][85])
            #			index.append(data[i][86])
            #			index.append(data[i][87])
            #			index.append(data[i][88])
            '''
			#spectalflatness mean var
			for a11 in range(85,87):
				index.append(data[i][a11])

			#spectalrolloff mean var
			for a12 in range(87,89):
				index.append(data[i][a12])

			#zcr
#			index.append(data[i][89])
			'''
            # loundess
            index.append(data[i][90])

            # inharmonicity
            index.append(data[i][91])

            # pitchsalience
            index.append(data[i][92])

            index.append(data[i][93])
            index.append(data[i][94])
            #			index.append(data[i][95])
            #			index.append(data[i][96])
            #			index.append(data[i][97])
            #			index.append(data[i][98])
            #			index.append(data[i][99])
            index.append(data[i][100])
            index.append(data[i][101])
            #			index.append(data[i][102])
            #			index.append(data[i][103])
            #			index.append(data[i][104])
            #			index.append(data[i][105])
            '''
			#pitch max min mean var median
			for a13 in range(93,98):
				index.append(data[i][a13])

			#tuningfrequece tuningcents
			for a14 in range(98,100):
				index.append(data[i][a14])

			#beats num max min mean var median
			for a15 in range(100,106):
				index.append(data[i][a15])
			'''
            test_data.append(index)

            test_target.append(test_code[k])

    return test_data, test_target


def readSelectedTrainData(train_path, train_mode):
    train_data = []
    train_target = []
    for k in range(len(train_path)):

        path = train_path[k]
        path = path.strip()
        # path = path.rstrip('/')
        # newPath = path + '/' + train_mode[i] + '.txt'
        data = np.loadtxt(path)
        for i in range(len(data)):
            index = []

            # yes
            # mfcc max
            for a1 in range(0, 13):
                index.append(data[i][a1])

            # yes
            # mfcc median
            for a2 in range(13, 26):
                index.append(data[i][a2])
            '''
			#yes
			#mfcc mean
			for a3 in range(26,39):
				index.append(data[i][a3])


			#no
			#mfcc var
			for a4 in range(39,52):
				index.append(data[i][a4])


			#yes
			#mfcc_d1 max
			for a5 in range(52,65):
				index.append(data[i][a5])


			#zcr mean var
			for a6 in range(65,67):
				index.append(data[i][a6])
			'''
            #			index.append(data[i][65])
            index.append(data[i][66])
            index.append(data[i][67])
            index.append(data[i][68])
            #			index.append(data[i][69])
            #			index.append(data[i][70])
            #			index.append(data[i][72])
            #			index.append(data[i][71])
            #			index.append(data[i][73])
            #			index.append(data[i][74])

            '''
			#lpc mean var
			#mean rock up,sad down
			#var jazz opera  happy rock up ,classic sad down
			for a7 in range(67,71):
				index.append(data[i][a7])

			#energy mean var
			#mean classic opera sad up ,other down
			#var up
			for a8 in range(71,73):
				index.append(data[i][a8])

			#sharpness mean var
			for a9 in range(73,75):
				index.append(data[i][a9])

			#lsf mean
			for a10 in range(75,85):
				index.append(data[i][a10])

			'''
            #			index.append(data[i][85])
            #			index.append(data[i][86])
            #			index.append(data[i][87])
            #			index.append(data[i][88])
            '''
			#spectalflatness mean var
			for a11 in range(85,87):
				index.append(data[i][a11])

			#spectalrolloff mean var
			for a12 in range(87,89):
				index.append(data[i][a12])

			#zcr
#			index.append(data[i][89])
			'''
            # loundess
            index.append(data[i][90])

            # inharmonicity
            index.append(data[i][91])

            # pitchsalience
            index.append(data[i][92])

            index.append(data[i][93])
            index.append(data[i][94])
            #			index.append(data[i][95])
            #			index.append(data[i][96])
            #			index.append(data[i][97])
            #			index.append(data[i][98])
            #			index.append(data[i][99])
            index.append(data[i][100])
            index.append(data[i][101])
            #			index.append(data[i][102])
            #			index.append(data[i][103])
            #			index.append(data[i][104])
            #			index.append(data[i][105])
            '''
			#pitch max min mean var median
			for a13 in range(93,98):
				index.append(data[i][a13])

			#tuningfrequece tuningcents
			for a14 in range(98,100):
				index.append(data[i][a14])

			#beats num max min mean var median
			for a15 in range(100,106):
				index.append(data[i][a15])
			'''

            train_data.append(index)
            train_target.append(k)

    return train_data, train_target

def main():
    initSoft()
    p = ['/home/chenming/Music/test']
    a = ['test',]
    b = 'emotion'
    c = range(0,34)
    print getTrainData(p, a, b, c)
    '''
    train_path = ['/home/chenming/Music/happy/feature_0/happy.txt',]
    train_mode = ['happy',]
    test_code = range(0, 34)
    print readSelectedTrainData(train_path, train_mode)
    '''




if __name__ == '__main__':
	main()
