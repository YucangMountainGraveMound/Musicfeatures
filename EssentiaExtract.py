#!/usr/bin/python
# -*- coding: utf-8 -*-
from yaafelib import *
from essentia.standard import *
import essentia.standard
import essentia.streaming
import essentia
from pylab import plot, show, figure
import matplotlib.pyplot as plt
import numpy as np


def initEssentia():

    global wind
    global spectrum
    wind = Windowing(type = 'hann')#@UndefinedVariable
    spectrum = Spectrum() # FFT() would give the complex FFT, here we just want the magnitude spectrum @UndefinedVariable

    return 'Essentia初始化'

def startLoader(path):
    global audio
    global spec
    global specFrequencies
    global specMagnitudes
    global frame

    loader = MonoLoader(filename = path)
    audio = loader()
    frame=audio[44100*20:44100*40]#20s-40s

    spec = spectrum(wind(frame))
    specFrequencies,specMagnitudes=SpectralPeaks()(spec)#@UndefinedVariable
    return 'Essentia路径设置成功'

#一维数组的中位值
def getMedian1(arr):
    arr.sort()
    median=0
    size=len(arr)
    temp1=(size-1)/2
    temp2=size/2
    if(size%2==1):
        median=arr[temp1]
    else:
        median=(arr[temp2]+arr[temp2-1])/2.0
    return median

#过零率
def getZCR():
    ZCR=ZeroCrossingRate() #@UndefinedVariable
    zcr=ZCR(frame)

    #print 'return ZCR'
    return zcr

#响度提取
def getLoudness():

    #响度
    loudness = Loudness() #@UndefinedVariable
    ln = loudness(frame) #real

    return ln

#不和谐性
def getInharmonicity():

    global specFrequencies
    global specMagnitudes
    #计数：频率为0的个数
    i=0
    for specFre in specFrequencies:
        if specFre==0:
            i=i+1
    #去掉频率为0的记录，（specFrequencies是升序排列的，所以可以用[i:]去除0频）
    specFrequencies=specFrequencies[i:]
    specMagnitudes=specMagnitudes[i:]
    pitch,pitchConfidence =PitchYinFFT()(spec) #@UndefinedVariable
    harmonicFrequencies,harmonicMagnitudes=HarmonicPeaks()(specFrequencies,specMagnitudes,pitch) #@UndefinedVariable
    inharmonicity=Inharmonicity()(harmonicFrequencies,harmonicMagnitudes) #@UndefinedVariable

    #print 'return inharmonicity'
    return inharmonicity

#音调突出
def getPitchSalience():

    pitchSalience = PitchSalience()(spec) #@UndefinedVariable

    return pitchSalience

#音调
def getPitch():

     #音调
    audio2 = EqualLoudness()(audio) #@UndefinedVariable
    #The output is a vector of estimated melody pitch values and a vector of confidence values. 音高值[HZ]向量和置信度值向量
    #pitch vector-real
    hopSize = 128 #跳幅
    frameSize = 2048
    guessUnvoiced = True # read the algorithm's reference for more details
    run_predominant_melody = PredominantMelody(guessUnvoiced=guessUnvoiced, #@UndefinedVariable
                                           frameSize=frameSize,
                                           hopSize=hopSize);
    pitch, confidence = run_predominant_melody(audio2[44100*20:44100*40]) #@UndefinedVariable

    pitchMax=pitch.max(axis=0) #最大值
    pitchMin=pitch.min(axis=0) #最小值
    pitchMean=pitch.mean(axis=0) #均值
    pitchVar=pitch.var(axis=0) #方差
    pitchMedian=getMedian1(pitch) #中位值

    return pitchMax, pitchMin, pitchMean, pitchVar, pitchMedian

#调谐频率及基频偏差
def getTuningFrequency():

    #调谐频率及调谐音程
    tuningFrequency,tuningCents =TuningFrequency()(specFrequencies,specMagnitudes) #@UndefinedVariable

    return tuningFrequency, tuningCents

#节拍
def getBeat():
        #节拍
    beats, _ = BeatTrackerMultiFeature()(frame)  #节拍位置
    beatLoudness,loudnessBandRatio=BeatsLoudness(beats=beats)(frame) #beatLoudness:响度； loudnessBandRatio：每个频带中节拍能量比率

    lnlen = len(beats)
    lnMax=beatLoudness.max(axis=0) #最大值
    lnMin=beatLoudness.min(axis=0) #最小值
    lnMean=beatLoudness.mean(axis=0) #均值
    lnVar=beatLoudness.var(axis=0) #方差
    lnMedian=getMedian1(beatLoudness) #中位值

    return lnlen, lnMax, lnMin, lnMean, lnVar, lnMedian

def getFeature(featureName):

    if featureName == 'beat':
        beat = []
        beats, _ = BeatTrackerMultiFeature()(frame) #@UndefinedVariable #节拍位置
        beatLoudness,loudnessBandRatio=BeatsLoudness(beats=beats)(frame) #@UndefinedVariable

        beat.append(beatLoudness)
        return beat

    elif featureName == 'pitch':
        array = []

        audio2 = EqualLoudness()(audio) #@UndefinedVariable
        #The output is a vector of estimated melody pitch values and a vector of confidence values. 音高值[HZ]向量和置信度值向量
        #pitch vector-real
        hopSize = 128 #跳幅
        frameSize = 2048
        guessUnvoiced = True # read the algorithm's reference for more details
        run_predominant_melody = PredominantMelody(guessUnvoiced=guessUnvoiced,frameSize=frameSize,hopSize=hopSize)

        #print 'hello'
        pitch, confidence = run_predominant_melody(audio2[44100*20:44100*40]) #@UndefinedVariable

        array.append(pitch)
        return array

#测试
def main():
    initEssentia()
    startLoader('/home/chenming/Music/test.mp3')
    print getBeats()


if __name__ == '__main__':
    main()