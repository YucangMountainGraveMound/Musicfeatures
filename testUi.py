# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 751, 521))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.label_4 = QtGui.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(80, 50, 71, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(80, 120, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.trainPath = QtGui.QLineEdit(self.tab_1)
        self.trainPath.setGeometry(QtCore.QRect(150, 50, 241, 27))
        self.trainPath.setObjectName(_fromUtf8("trainPath"))
        self.trainFlile = QtGui.QToolButton(self.tab_1)
        self.trainFlile.setGeometry(QtCore.QRect(400, 50, 31, 25))
        self.trainFlile.setObjectName(_fromUtf8("trainFlile"))
        self.addTrainPath = QtGui.QPushButton(self.tab_1)
        self.addTrainPath.setGeometry(QtCore.QRect(300, 120, 171, 27))
        self.addTrainPath.setObjectName(_fromUtf8("addTrainPath"))
        self.startTrain = QtGui.QPushButton(self.tab_1)
        self.startTrain.setGeometry(QtCore.QRect(440, 170, 98, 27))
        self.startTrain.setObjectName(_fromUtf8("startTrain"))
        self.label_6 = QtGui.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(70, 180, 61, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.trainResult = QtGui.QTextEdit(self.tab_1)
        self.trainResult.setGeometry(QtCore.QRect(100, 220, 481, 231))
        self.trainResult.setObjectName(_fromUtf8("trainResult"))
        self.trainMode = QtGui.QLineEdit(self.tab_1)
        self.trainMode.setGeometry(QtCore.QRect(130, 120, 131, 27))
        self.trainMode.setObjectName(_fromUtf8("trainMode"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(50, 40, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.songPath = QtGui.QLineEdit(self.tab_2)
        self.songPath.setGeometry(QtCore.QRect(120, 40, 241, 27))
        self.songPath.setObjectName(_fromUtf8("songPath"))
        self.fileSelect = QtGui.QToolButton(self.tab_2)
        self.fileSelect.setGeometry(QtCore.QRect(370, 40, 31, 25))
        self.fileSelect.setObjectName(_fromUtf8("fileSelect"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.testStyle = QtGui.QComboBox(self.tab_2)
        self.testStyle.setGeometry(QtCore.QRect(120, 110, 78, 27))
        self.testStyle.setObjectName(_fromUtf8("testStyle"))
        self.testStyle.addItem(_fromUtf8(""))
        self.testButton = QtGui.QPushButton(self.tab_2)
        self.testButton.setGeometry(QtCore.QRect(360, 110, 98, 27))
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 61, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.result = QtGui.QTextEdit(self.tab_2)
        self.result.setGeometry(QtCore.QRect(73, 227, 531, 241))
        self.result.setObjectName(_fromUtf8("result"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "训练路径", None))
        self.label_5.setText(_translate("MainWindow", "Mode", None))
        self.trainFlile.setText(_translate("MainWindow", "...", None))
        self.addTrainPath.setText(_translate("MainWindow", "添加训练路径和Mode", None))
        self.startTrain.setText(_translate("MainWindow", "开始训练", None))
        self.label_6.setText(_translate("MainWindow", "训练结果", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "歌曲训练", None))
        self.label.setText(_translate("MainWindow", "歌曲路径：", None))
        self.fileSelect.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "类型", None))
        self.testStyle.setItemText(0, _translate("MainWindow", "emotion", None))
        self.testButton.setText(_translate("MainWindow", "开始测试", None))
        self.label_3.setText(_translate("MainWindow", "测试结果", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "歌曲分类", None))

