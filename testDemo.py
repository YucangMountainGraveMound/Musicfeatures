#!/usr/bin/python
# -*- coding:utf-8 -*-


def test(path):
    test_file_type = path.split('/')
    test_file = path+'/feature_0/'+test_file_type[len(test_file_type)-1]+'.txt'
    print test_file;


if __name__ == '__main__':
    type = ['happy', 'sad']
    test('/home/chenming/Music/sad')