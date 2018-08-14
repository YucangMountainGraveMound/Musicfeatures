#!/usr/bin/python
# -*- coding:utf-8 -*-

from yaafelib import Engine, FeaturePlan,AudioFileProcessor

def initYaafe():

    global df
    fp = FeaturePlan(sample_rate=44100, resample=True, time_start=20,time_limit=40)  # 20s

    fp.addFeature("energy: Energy")#能量
    fp.addFeature("zcr: ZCR")#过零率
    #fp.addFeature("loudness: Loudness")#响度
    fp.addFeature("sharpness: PerceptualSharpness") #尖锐度
    fp.addFeature("lpc: LPC")#线性预测系数
    fp.addFeature("lsf: LSF")#线性谱率
    fp.addFeature("spectralRolloff: SpectralRolloff") #谱流量
    fp.addFeature("spectralFlatness: SpectralFlatness") #谱平坦度
    fp.addFeature("mfcc: MFCC CepsNbCoeffs=13") #MFCC
    fp.addFeature('mfcc_d1: MFCC blockSize=1024 stepSize=512 > Derivate DOrder=1')#MFCC一阶倒数

    df = fp.getDataFlow()


    return 'Yaafe初始化'

def startEngine(path):

    global features

    engine = Engine()
    engine.load(df)

    afp  = AudioFileProcessor()
    afp.processFile(engine,path)
    features = engine.readAllOutputs()

    return 'Yaafe引擎启动成功'

#特征MFCC提取
def getMFCC():
    mfcc = features.get('mfcc')
    mfccMax=mfcc.max(axis=0)
    mfccMax=mfccMax.reshape(-1,) # 最大值

    mfccMedian=getMedian(mfcc) # 中位数

    mfccMean=mfcc.mean(axis=0)  # 平均值
    mfccMean=mfccMean.reshape(-1,)


    mfccVar=mfcc.var(axis=0)  # 方差
    mfccVar=mfccVar.reshape(-1,)


    #print 'MFCC : ',len(mfcc),len(mfccMax)
    #print mfcc
#	print 'MFCC : 4 个特征 ,有4组数组:',len(mfccMax),len(mfccMedian),len(mfccMean),len(mfccVar)
    return mfccMax , mfccMedian , mfccMean , mfccVar

#过零率ZCR
def getZCR():
    zcr = features.get('zcr')
    zcrMean=zcr.mean(axis=0) #均值
    zcrVar =zcr.var(axis=0)  #方差

    #print 'ZCR : 2个数组 :'
    return zcrMean , zcrVar
#能量
def getEnergy():
    energy = features.get('energy')
    energyMean=energy.mean(axis=0) #均值
    energyVar =energy.var(axis=0)  #方差

    #print 'energy : 2个数组 :'
    return energyMean , energyVar
#尖锐度
def getSharpness():
    sharpness =features.get('sharpness')
    sharpnessMean=sharpness.mean(axis=0)
    sharpnessVar =sharpness.var(axis=0)

    #print 'sharpness : 2数组 :'
    return sharpnessMean , sharpnessVar
#线性预测系数
def getLPC():
    lpc =features.get('lpc')
    lpcMean=lpc.mean(axis=0)
    lpcVar =lpc.var(axis=0)

    #print 'LPC : 2 个数组:'
    return lpcMean , lpcVar
#线性谱率
def getLSF():
    lsf= features.get('lsf')
    lsfMean=lsf.mean(axis=0)
    lsfMean=lsfMean.reshape(-1,) # 平均值

    #print 'LSF : 1 个数组:'
    return lsfMean
#谱流量
def getSpectralRolloff():
    spectralRolloff = features.get('spectralRolloff')
    spectralRolloffMean=spectralRolloff.mean(axis=0)
    spectralRolloffVar =spectralRolloff.var(axis=0)

    #print 'spectralRolloff : 2 个数组:'
    return spectralRolloffMean , spectralRolloffVar
#谱平坦度
def getSpectraFlatness():
    spectralFlatness = features.get('spectralFlatness')
    spectralFlatnessMean=spectralFlatness.mean(axis=0)
    spectralFlatnessVar =spectralFlatness.var(axis=0)

    #print 'spectraFlatness : 2 个数组:'
    return spectralFlatnessMean , spectralFlatnessVar
#MFCC一阶倒数
def getMfcc_d1():
    mfcc_d1= features.get('mfcc_d1')
    mfcc_d1MAX=mfcc_d1.max(axis=0)  # mfcc一阶差分最大值
    mfcc_d1MAX=mfcc_d1MAX.reshape(-1,)

    #print 'mfcc_d1 :1 个数组:'
    return mfcc_d1MAX
#根据特征要求提取
def getFeature(featureName):
    f = featureName
    if f == 'mfcc':
        mfcc = features.get('mfcc')
        return mfcc.T
    elif f == 'mfcc_d1':
        mfcc_d1= features.get('mfcc_d1')
        return mfcc_d1.T
    elif f == 'lsf':
        lsf= features.get('lsf')
        return lsf.T
    elif f == 'lpc':
        lpc =features.get('lpc')
        return lpc.T
    elif f == 'spectralFlatness':
        spectralFlatness = features.get('spectralFlatness')
        return spectralFlatness.T
    elif f == 'spectralRolloff':
        spectralRolloff = features.get('spectralRolloff')
        return spectralRolloff.T
    elif f == 'sharpness':
        sharpness =features.get('sharpness')
        return sharpness.T
    elif f == 'energy':
        energy = features.get('energy')
        return energy.T
    elif f == 'zcr':
        zcr = features.get('zcr')
        return zcr.T
    else:
        return

#一阶倒数矩阵转置求平均
def getMedian(mfcc):
    mfccT=mfcc.T
    #print mfccT.shape
    #print 'len(mfccT):', len(mfccT)
    size=len(mfccT[0])
    mfccMedian=[]

    for mfccData in mfccT:
        mfccData.sort()
        median=0
        mid1=(size-1)/2
        mid2=size/2
        if(size%2==1):
            median=mfccData[mid1]
        else:
            median=(mfccData[mid2]+mfccData[mid2-1])/2.0
        mfccMedian.append(median)

    return mfccMedian

#测试
def main():
    initYaafe()
    startEngine('/home/chenming/Music/test.mp3')
    print getMfcc_d1()


if __name__ == '__main__':
    main()