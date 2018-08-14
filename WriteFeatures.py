#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import Tools as tool


# 设置类别

def setMode(m):

    global mode
    mode = m

    return '类别设置成功'

# 设置输出特征位置
def setFeaturePrintPath(path):
	global newPath
	path = path.strip()
	path = path.rstrip('/')
	#print type(path),type('/'),type(tool.getFeatureDirName(path))
	newPath = path + '/' + tool.getFeatureDirName(path)
	tool.mkdir(newPath)


	return

# 将特征和说明写入文件
def writeFeature(featureList,introFeature=[]):
	filePath = newPath + '/' + mode +'.txt'
	readPath = newPath + '/readme.txt'
	#输出特征
	featureList = np.array(featureList)
	np.savetxt(filePath,featureList)

	#输出特征说明
	f = open(readPath,'a') #会创建新文件
	for i in range(len(introFeature)):
		f.write('特征:%s\t维数:%s\n' % (introFeature[i][0],introFeature[i][1]))
		print '特征:',introFeature[i][0],'维数:',introFeature[i][1]
	f.close()


# 将特征说明写入文件
def writeFeatureDetial(path,introFeature):

	#输出特征说明
	f = open(path,'w')
	for i in range(len(introFeature)):
		f.write('特征:%s\t维数:%s\n' % (introFeature[i][0],introFeature[i][1]))
		print '特征:',introFeature[i][0],'维数:',introFeature[i][1]
	f.close()

def writeDetial(path,list):
	f = open(path,'w')
	for i in list:
		f.write(str(i)+'\n')
	f.close()

#读取文件每行数据生成一个数组
def readFileTxt(path):
	context = []
	f = open(path,'r')
	'''
	line=f.readline()
	while line:
		print line
		context.append(line)
		line=f.readline()#如果没有这行会造成死循环
	'''
	for line in f:
		#print line.strip()
		context.append(line.strip())
	f.close()
	return context


def main():

    print readFileTxt('/home/chenming/GraduateDesign/feature_2/happy.txt')
	#setFeaturePrintPath('/home/chenming/GraduateDesign')
	#a = [[1,2,3,4,5,5]]
	#writeFeature(a)

if __name__ == '__main__':
	main()