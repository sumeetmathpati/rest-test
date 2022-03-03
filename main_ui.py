# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 629)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.collectionTab = QtWidgets.QWidget()
        self.collectionTab.setObjectName("collectionTab")
        self.tabWidget.addTab(self.collectionTab, "")
        self.envTab = QtWidgets.QWidget()
        self.envTab.setObjectName("envTab")
        self.tabWidget.addTab(self.envTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.methodsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.methodsComboBox.setMinimumSize(QtCore.QSize(90, 0))
        self.methodsComboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.methodsComboBox.setObjectName("methodsComboBox")
        self.horizontalLayout_2.addWidget(self.methodsComboBox)
        self.urlInput = QtWidgets.QLineEdit(self.centralwidget)
        self.urlInput.setObjectName("urlInput")
        self.horizontalLayout_2.addWidget(self.urlInput)
        self.sendRequestPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendRequestPushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sendRequestPushButton.setObjectName("sendRequestPushButton")
        self.horizontalLayout_2.addWidget(self.sendRequestPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.middleSection = QtWidgets.QTabWidget(self.centralwidget)
        self.middleSection.setObjectName("middleSection")
        self.queryTab = QtWidgets.QWidget()
        self.queryTab.setObjectName("queryTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.queryTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.queryTabTitle = QtWidgets.QLabel(self.queryTab)
        self.queryTabTitle.setObjectName("queryTabTitle")
        self.verticalLayout_3.addWidget(self.queryTabTitle)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addQueryPushButton = QtWidgets.QPushButton(self.queryTab)
        self.addQueryPushButton.setObjectName("addQueryPushButton")
        self.horizontalLayout_3.addWidget(self.addQueryPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.queriesList = QtWidgets.QListView(self.queryTab)
        self.queriesList.setObjectName("queriesList")
        self.verticalLayout_3.addWidget(self.queriesList)
        self.middleSection.addTab(self.queryTab, "")
        self.headersTab = QtWidgets.QWidget()
        self.headersTab.setObjectName("headersTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.headersTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headersTabTitle = QtWidgets.QLabel(self.headersTab)
        self.headersTabTitle.setObjectName("headersTabTitle")
        self.verticalLayout_2.addWidget(self.headersTabTitle)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addHeaderPushButton = QtWidgets.QPushButton(self.headersTab)
        self.addHeaderPushButton.setObjectName("addHeaderPushButton")
        self.horizontalLayout_4.addWidget(self.addHeaderPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.headersList = QtWidgets.QListView(self.headersTab)
        self.headersList.setObjectName("headersList")
        self.verticalLayout_2.addWidget(self.headersList)
        self.middleSection.addTab(self.headersTab, "")
        self.authTab = QtWidgets.QWidget()
        self.authTab.setObjectName("authTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.authTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.NoneTab = QtWidgets.QTabWidget(self.authTab)
        self.NoneTab.setObjectName("NoneTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.NoneTab.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.NoneTab.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.NoneTab.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.NoneTab.addTab(self.tab_6, "")
        self.verticalLayout_4.addWidget(self.NoneTab)
        self.middleSection.addTab(self.authTab, "")
        self.bodyTab = QtWidgets.QWidget()
        self.bodyTab.setObjectName("bodyTab")
        self.middleSection.addTab(self.bodyTab, "")
        self.verticalLayout.addWidget(self.middleSection)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.outputLayout = QtWidgets.QVBoxLayout()
        self.outputLayout.setObjectName("outputLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.responseStatusTitle = QtWidgets.QLabel(self.centralwidget)
        self.responseStatusTitle.setObjectName("responseStatusTitle")
        self.horizontalLayout_5.addWidget(self.responseStatusTitle)
        self.responseStatusResult = QtWidgets.QLabel(self.centralwidget)
        self.responseStatusResult.setObjectName("responseStatusResult")
        self.horizontalLayout_5.addWidget(self.responseStatusResult)
        self.outputLayout.addLayout(self.horizontalLayout_5)
        self.outputTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.outputLayout.addWidget(self.outputTextEdit)
        self.horizontalLayout.addLayout(self.outputLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.middleSection.setCurrentIndex(2)
        self.NoneTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.collectionTab), _translate("MainWindow", "Collections"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.envTab), _translate("MainWindow", "Env"))
        self.urlInput.setPlaceholderText(_translate("MainWindow", "Enter URL"))
        self.sendRequestPushButton.setText(_translate("MainWindow", "Send"))
        self.queryTabTitle.setText(_translate("MainWindow", "Query Parameters"))
        self.addQueryPushButton.setText(_translate("MainWindow", "Add Query"))
        self.middleSection.setTabText(self.middleSection.indexOf(self.queryTab), _translate("MainWindow", "Query"))
        self.headersTabTitle.setText(_translate("MainWindow", "HTTP Headers"))
        self.addHeaderPushButton.setText(_translate("MainWindow", "Add Header"))
        self.middleSection.setTabText(self.middleSection.indexOf(self.headersTab), _translate("MainWindow", "Headers"))
        self.NoneTab.setTabText(self.NoneTab.indexOf(self.tab), _translate("MainWindow", "None"))
        self.NoneTab.setTabText(self.NoneTab.indexOf(self.tab_4), _translate("MainWindow", "Basic"))
        self.NoneTab.setTabText(self.NoneTab.indexOf(self.tab_5), _translate("MainWindow", "Bearer"))
        self.NoneTab.setTabText(self.NoneTab.indexOf(self.tab_6), _translate("MainWindow", "OAuth2"))
        self.middleSection.setTabText(self.middleSection.indexOf(self.authTab), _translate("MainWindow", "Auth"))
        self.middleSection.setTabText(self.middleSection.indexOf(self.bodyTab), _translate("MainWindow", "Body"))
        self.responseStatusTitle.setText(_translate("MainWindow", "Status:"))
        self.responseStatusResult.setText(_translate("MainWindow", "StatusResult"))
        self.outputTextEdit.setPlaceholderText(_translate("MainWindow", "Output"))
