#!/usr/bin/python
# -*- coding:utf-8 -*-

from sklearn import svm, grid_search
from sklearn import tree
from sklearn import neighbors
from sklearn.mixture import GMM
import numpy as np
from sklearn import metrics
import Tools as tool
from sklearn import preprocessing
import myUI
import WriteFeatures as wf
import ExtractFeature as ef
from sklearn.externals import joblib


# svm:支持向量机;knn:k临近;tree:决策树
# 设置算法
def setClassifier(Ctype='svm'):
    global classifierType
    # print 'svm,knn,tree'

    classifierType = Ctype

    print '设置分类器成功'

def train(train_data, train_target, train_mode, mode_name):
    # 数据标准化

    train_data = np.array(train_data)
    train_target = np.array(train_target)

    # sklearn提供的数据处理方法
    # train_data = preprocessing.scale(train_data)
    # test_data = preprocessing.scale(test_data)

    (meanData, stdData) = tool.trainDataStandardNor(train_data)

    # 存储
    np.savetxt('dataSystem/' + mode_name + '/meanData.txt', meanData)
    np.savetxt('dataSystem/' + mode_name + '/stdData.txt', stdData)
    wf.writeDetial('dataSystem/' + mode_name + '/modeList.txt', train_mode)
    #np.savetxt('dataSystem/' + mode_name + '/modeList.txt', train_mode)
    '''
	c=np.arange(1,10,1)
	g=np.arange(0,1,0.1)
	tuned_parameters = [{'kernel': ['rbf'], 'gamma': g,'C': c}]
	#print classifierType,type(classifierType)
	'''
    clf = svm.SVC()
    if classifierType == 'svm':
        clf = svm.SVC()
    elif classifierType == 'knn':
        clf = neighbors.KNeighborsClassifier()  # knn K-临近算法
    elif classifierType == 'tree':
        clf = tree.DecisionTreeClassifier()  # 决策树

    # clf = grid_search.GridSearchCV(svm.SVC(), tuned_parameters, cv=3) #svm支持向量机
    print train_data
    print train_target

    clf.fit(train_data, train_target)
    # clf.fit(train_data)
    # clf.score(test_data, test_target)
    # showStyleDetail(test_data,test_target,clf)
    from sklearn.externals import joblib

    tool.mkdir('svcSystem/' + mode_name)
    joblib.dump(clf, 'svcSystem/' + mode_name + '/svc1.pkl')
    # clf2=joblib.load('svc/svc1.pkl')
    # print clf.score(test_data, test_target)
    # showDetail(test_data,test_target,clf2)
    # print clf.best_estimator_

    return '训练成功,模型' + mode_name + '存储成功,'+'位置:svcSystem/'+mode_name +'/svc1.pkl'

def train_test(train_data, train_target, test_data, test_target):
    train_data = np.array(train_data)
    train_target = np.array(train_target)
    test_data = np.array(test_data)
    test_target = np.array(test_target)

    (meanData, stdData) = tool.trainDataStandardNor(train_data)
    tool.testDataStandardNor(test_data, meanData, stdData)
    clf = svm.SVC()
    if classifierType == 'svm':
        clf = svm.SVC()
    elif classifierType == 'knn':
        clf = neighbors.KNeighborsClassifier()  # knn K-临近算法
    elif classifierType == 'tree':
        clf = tree.DecisionTreeClassifier()  # 决策树
    clf.fit(train_data, train_target)

    predicted = clf.predict(test_data)
    print metrics.classification_report(test_target, predicted)
    print metrics.confusion_matrix(test_target, predicted)

def testOneSong(train_data, train_target, train_mode, test_data):
    # 数据标准化

    train_data = np.array(train_data)
    train_target = np.array(train_target)
    test_data = np.array(test_data)
    # print test_data
    # sklearn提供的数据处理方法
    # train_data = preprocessing.scale(train_data)
    # test_data = preprocessing.scale(test_data)

    (meanData, stdData) = tool.trainDataStandardNor(train_data)
    tool.testDataStandardNor(test_data, meanData, stdData)

    clf = svm.SVC()
    if classifierType == 'svm':
        clf = svm.SVC()
    elif classifierType == 'knn':
        clf = neighbors.KNeighborsClassifier()  # knn K-临近算法
    elif classifierType == 'tree':
        clf = tree.DecisionTreeClassifier()  # 决策树

    # clf = grid_search.GridSearchCV(svm.SVC(), tuned_parameters, cv=3) #svm支持向量机

    clf.fit(train_data, train_target)

    predicted = clf.predict(test_data)

    print '预测结果:' + str(train_mode[predicted]) + '类型'
    out = '预测结果:' + str(train_mode[predicted]) + '类型'
    return out

def test(test_data, test_target, test_mode, mode_name):
    test_data = np.array(test_data)
    test_target = np.array(test_target)

    print 'test_data:', test_data
    print 'test_target:', test_target
    print 'test_mode:', test_mode

    path1 = 'dataSystem/' + mode_name + '/meanData.txt'
    path2 = 'dataSystem/' + mode_name + '/stdData.txt'
    path3 = 'svcSystem/' + mode_name + '/svc1.pkl'
    path4 = 'dataSystem/' + mode_name + '/modeList.txt'

    print '数据路径:' + 'dataSystem/' + mode_name + '和svcSystem/' + mode_name

    meanData = np.loadtxt(path1)
    stdData = np.loadtxt(path2)
    modeList = wf.readFileTxt(path4)
    mode = wf.readFileTxt('dataSystem/' + mode_name + '/modeList.txt')

    tool.testDataStandardNor(test_data, meanData, stdData)

    from sklearn.externals import joblib

    clf = joblib.load(path3)

    s = showDetail(clf, test_data, test_target, modeList)

    return s

def showDetail(clf, test_data, test_target, mode):
    modeNum = []

    expected = test_target
    predicted = clf.predict(test_data)
    # print expected
    # print predicted
    # print test_mode

    out = '''
*******准确率=被识别为该分类的正确分类记录数/被识别为该分类的记录数
*******召回率=被识别为该分类的正确分类记录数/测试集中该分类的记录总数
*******F1-score=2（准确率 * 召回率）/（准确率 + 召回率），F1-score是F-measure（又称F-score）beta=1时的特例
*******support=测试集中该分类的记录总数\n
		'''
    for d in mode:
        print 'd', d
    out = out + str(metrics.classification_report(expected, predicted, target_names=mode))
    print (metrics.classification_report(expected, predicted, target_names=mode))
    result = metrics.confusion_matrix(expected, predicted)
    out = out + '\n预测数目:\t'
    print  '预测数目:\t',
    for j in range(len(mode)):
        out = out + str(mode[j]) + '\t'
        print mode[j], '\t',
    out = out + '\n\n'
    print '\n'
    for i in range(len(result)):
        out = out + '测试数据' + str(i + 1) + ':\t'
        print '测试数据' + str(i + 1) + ':\t',
        num = 0
        for p in range(len(result[i])):
            out = out + str(result[i][p]) + '\t'
            print result[i][p], '\t',
            num = num + result[i][p]
        out = out + '\n'
        print '\n'
        modeNum.append([result[i][i], num])
        out = out + '\n'
    for k in range(len(modeNum)):
        out = out + str(mode[k]) + ':\t命中/总数:' + str(modeNum[k][0]) + '/' + str(modeNum[k][1]) + '\t正确率:' + str(
            tool.ratio(modeNum[k][0], modeNum[k][1])) + '\n'
        print mode[k], ':\t命中/总数:', modeNum[k][0], '/', modeNum[k][1], '\t正确率:', tool.ratio(modeNum[k][0],
                                                                                            modeNum[k][1])

    return out

# 通过已有数据进行测试
def testBydefualtData(test_data, mode):
    typeMode = ['happy', 'sad']

    path1 = 'dataSystem/' + mode + '/meanData.txt'
    path2 = 'dataSystem/' + mode + '/stdData.txt'
    path3 = 'svcSystem/' + mode + '/svc1.pkl'

    meanData = np.loadtxt(path1)
    stdData = np.loadtxt(path2)

    test_data = np.array(test_data)
    print test_data
    tool.testDataStandardNor(test_data, meanData, stdData)

    from sklearn.externals import joblib

    clf = joblib.load(path3)
    result = clf.predict(test_data)
    if mode == 'emotion':
        print result
        print "测试结果:" + typeMode[result[0]] + "类型"
        return "测试结果:" + typeMode[result[0]] + "类型"
    '''
    else:
        if typeMode[result] == mode:
            print "是" + str(mode) + "类型"
            return "是" + str(mode) + "类型"
        else:
            print "不是" + str(mode) + "类型"
            return "不是" + str(mode) + "类型"
    '''

def testAlldefualtData(test_data, mode, files, path):
    #typeMode = ['happy', 'sad']
    typeMode = wf.readFileTxt('dataSystem/emotion/modeList.txt')
    test_result = []
    test_resultFile = []
    test_resultType = []
    path1 = 'dataSystem/' + mode + '/meanData.txt'
    path2 = 'dataSystem/' + mode + '/stdData.txt'
    path3 = 'svcSystem/' + mode + '/svc1.pkl'

    meanData = np.loadtxt(path1)
    stdData = np.loadtxt(path2)
    clf = joblib.load(path3)
    k = 0
    for test_da in test_data:
        da = []
        test_da = np.array(test_da)
        da.append(test_da)
        da = np.array(da)
        tool.testDataStandardNor(da, meanData, stdData)
        result = clf.predict(da)
        if mode == 'emotion':
            test_resultFile.append(files[k])
            test_resultType.append(typeMode[result[0]])
            test_result.append(files[k] + " : "+ typeMode[result[0]])
            k = k+1
            print "测试结果:" + typeMode[result[0]] + "类型"
    tool.mkdir(path+'/result')
    f1 = open(path+'/result/files.txt','a')
    f2 = open(path+'/result/types.txt','a')
    for i in range(len(test_resultFile)):
        f1.write(test_resultFile[i] + '\n')
        f2.write(test_resultType[i] + '\n')
    f1.close()
    f2.close()
    return test_result


def main():
    '''
    train_path = ['/home/chenming/Music/happy/feature_0/happy.txt','/home/chenming/Music/sad/feature_0/sad.txt']
    train_mode = ['happy','sad']
    test_code = [0,1]
    train_da, train_ta = ef.readSelectedTrainData(train_path, train_mode)
    setClassifier()
    train(train_da, train_ta, train_mode, 'emotion')
    '''
    test_path = ['/home/chenming/Music/happy/feature_0/happy.txt']
    test_mode = ['happy',]
    test_code = [0,]
    test_da, test_ta = ef.readSelectedTrainData(test_path, test_mode)

    #test(test_da, test_ta, 'happy', 'emotion')





if __name__ == '__main__':
	main()