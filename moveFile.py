#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import numpy as np
import Tools as tool
import shutil

def moveMusic(path, type):
    f1 = open(path+"/result/files.txt", "r")
    f2 = open(path+"/result/types.txt", "r")
    files = []
    types = []
    for line in f1.readlines():
        line=line.strip('\n')
        files.append(line)
    for line in f2.readlines():
        line=line.strip('\n')
        types.append(line)
    print files
    print types
    f1.close()
    f2.close()

    mp3File = tool.getAllFile(path)
    print mp3File

    for x in type:
        tool.mkdir(path+'/'+x)

    for file in range(len(mp3File)):
        shutil.move(mp3File[file], path+'/'+types[file])








if __name__ == '__main__':
    type = ['happy', 'sad']
    moveMusic('/home/chenming/Music/111', type)