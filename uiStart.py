#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import testUi
import sys
import Manage as m
import Tools as tool
import moveFile as mf
import WriteFeatures as wf

#使中文不乱码
QTextCodec.setCodecForTr(QTextCodec.codecForName("system"))
QTextCodec.setCodecForCStrings(QTextCodec.codecForName("system"))
QTextCodec.setCodecForLocale(QTextCodec.codecForName("system"))

class TestDialog(QMainWindow,testUi.Ui_MainWindow):
    train_path = []
    train_mode = []
    test_path = []
    test_mode = []
    svcList = []

    def __init__(self,parent=None):
        super(TestDialog,self).__init__(parent)

        self.setupUi(self)
        self.connectButton()



    def connectButton(self):
        QObject.connect(self.trainFlile,SIGNAL("clicked()"),self.openTrainDir)
        QObject.connect(self.fileSelect,SIGNAL("clicked()"),self.openTestDir)
        QObject.connect(self.testButton,SIGNAL("clicked()"),self.test)
        QObject.connect(self.addTrainPath,SIGNAL("clicked()"),self.setTrainPath)
        QObject.connect(self.startTrain,SIGNAL("clicked()"),self.startTraintest)



    def startTraintest(self):
        self.trainResult.clear()
        path = str(self.trainPath.text())
        self.trainResult.append("开始训练")
        m.setClassifier('svm')
        train_data, train_target = m.readSelectedTrainData(self.train_path, self.train_mode)
        reslut_info = m.train(train_data, train_target, self.train_mode, 'emotion')
        self.trainResult.append(reslut_info)
        self.train_path = []
        self.train_mode = []



    def setTrainPath(self):
        path = str(self.trainPath.text())
        mode = str(self.trainMode.text())
        if path == "":
            self.trainResult.append("训练路径不能为空")
        elif mode == "":
            self.trainResult.append("训练类型不能为空")
        else:
            self.trainPath.setText("")
            self.trainMode.setText("")
            self.trainResult.append("路径:" + path + "\n类型:" + mode + "\n添加成功")
            self.train_path.append(path)
            self.train_mode.append(mode)


    def openTrainDir(self):
        s = QFileDialog.getOpenFileName(self,"Choose a file to open","/home", "*.txt")
        self.trainPath.setText(s)

    def openTestDir(self):
        s = QFileDialog.getExistingDirectory(self,"Choose a directory","/home")
        self.songPath.setText(s)

    def test(self):
        self.result.clear()
        self.result.append('开始测试,请等待')
        print 'asdasdasdasd'
        mode_name = str(self.testStyle.currentText().toAscii())
        test_pa = str(self.songPath.text())
        test_file_type = str(self.songPath.text()).split('/')
        test_file = str(self.songPath.text())+'/feature_0/'+test_file_type[len(test_file_type)-1]+'.txt'
        self.result.append(test_file)
        test_result = m.testAllSong(test_pa, one_mode = mode_name, data_fi =test_file)
        print test_result;
        test_result = '\n'.join(test_result)
        unicode(QString(test_result).toUtf8(), 'utf-8', 'ignore')
        self.result.append(test_result)
        typeMode = wf.readFileTxt('dataSystem/emotion/modeList.txt')
        mf.moveMusic(test_pa, typeMode)
        '''
        test_result = '\n'.join(test_result)
        print test_result
        unicode(QString(test_result).toUtf8(), 'utf-8', 'ignore')
        self.result.append(test_result)
        '''




app=QApplication(sys.argv)
dialog=TestDialog()
dialog.show()
app.exec_()