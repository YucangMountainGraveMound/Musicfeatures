#!/usr/bin/python
# -*- coding:utf-8 -*-

import Manage as m


def main():
    '''
    #读取已有特征数据测试,测试成功
    trainpath = []
    trainmode = []
    trainpath.append('/home/chenming/Music/happy/feature_0/happy.txt')
    trainmode.append('happy')
    trainpath.append('/home/chenming/Music/sad/feature_0/sad.txt')
    trainmode.append('sad')

    m.setClassifier('svm')

    testpath = []
    testmode = []
    testpath.append('/home/chenming/Music/happytest/feature_0/happy.txt')
    testmode.append('happy')
    testpath.append('/home/chenming/Music/sadtest/feature_0/sad.txt')
    testmode.append('sad')

    train_data,train_target = m.readTrainData(trainpath,trainmode)
    test_data,test_target = m.readTestData(trainmode,testpath,testmode)

    m.train_test(train_data,train_target,test_data,test_target)
	#ok
    '''
    #==========================================================================
    #m.testSong('/home/chenming/Music/happytest/Happy - Johnny Rollins.mp3','emotion')
    m.testAllSong('/home/chenming/Music/111','emotion')
    #m.showSongDetail('/home/chenming/Music/happytest/小跳蛙 - 青蛙乐队.mp3','sharpness')
	#m.help()


if __name__ == '__main__':
	main()