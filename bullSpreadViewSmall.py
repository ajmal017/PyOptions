# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bullSpreadViewSmall.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ib_insync import *


# Need to disconnect
# see note in function // onConnectButtonClicked
# import asyncio
util.useQt()

from localUtilities import errorHandler, configIB, buildOptionMatrices, dateUtils

class Ui_MainWindow(object):
    def __init__(self):
        self.ib = IB()
        self.ib.setCallback('error', errorHandler.onError)

    # def setup Ui -- goes here:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 319)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../local-packages/localUtilities/icons/ib.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 331, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.updateQualifyClose = QtWidgets.QPushButton(self.groupBox_2)
        self.updateQualifyClose.setGeometry(QtCore.QRect(130, 190, 75, 23))
        self.updateQualifyClose.setObjectName("updateQualifyClose")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 185, 17))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.radioButton_Index = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_Index.setChecked(True)
        self.radioButton_Index.setObjectName("radioButton_Index")
        self.radioButton_Stock = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_Stock.setObjectName("radioButton_Stock")
        self.radioButton_Option = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_Option.setObjectName("radioButton_Option")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 250, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.labelExchange = QtWidgets.QLabel(self.layoutWidget)
        self.labelExchange.setWhatsThis("")
        self.labelExchange.setObjectName("labelExchange")
        self.gridLayout.addWidget(self.labelExchange, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.underlyingText = QtWidgets.QLineEdit(self.layoutWidget)
        self.underlyingText.setObjectName("underlyingText")
        self.gridLayout.addWidget(self.underlyingText, 1, 0, 1, 1)
        self.comboBoxExchange = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxExchange.setToolTip("")
        self.comboBoxExchange.setObjectName("comboBoxExchange")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.gridLayout.addWidget(self.comboBoxExchange, 1, 1, 1, 1)
        self.comboBox_Expiry = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.comboBox_Expiry.setFont(font)
        self.comboBox_Expiry.setObjectName("comboBox_Expiry")
        self.gridLayout.addWidget(self.comboBox_Expiry, 1, 2, 1, 1)
        self.groupBox_StrikePrice = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_StrikePrice.setGeometry(QtCore.QRect(20, 130, 251, 41))
        self.groupBox_StrikePrice.setObjectName("groupBox_StrikePrice")
        self.label_4 = QtWidgets.QLabel(self.groupBox_StrikePrice)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_StrikePrice)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 41, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_StrikePrice)
        self.comboBox.setGeometry(QtCore.QRect(60, 20, 51, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_StrikePrice)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 20, 51, 16))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(20, 98, 121, 21))
        self.widget.setObjectName("widget")
        self.gridLayout_CallPut = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_CallPut.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_CallPut.setObjectName("gridLayout_CallPut")
        self.radioButton_Call = QtWidgets.QRadioButton(self.widget)
        self.radioButton_Call.setChecked(True)
        self.radioButton_Call.setObjectName("radioButton_Call")
        self.gridLayout_CallPut.addWidget(self.radioButton_Call, 0, 0, 1, 1)
        self.radioButton_Put = QtWidgets.QRadioButton(self.widget)
        self.radioButton_Put.setObjectName("radioButton_Put")
        self.gridLayout_CallPut.addWidget(self.radioButton_Put, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIBToolbar = QtWidgets.QToolBar(MainWindow)
        self.actionIBToolbar.setMovable(False)
        self.actionIBToolbar.setFloatable(False)
        self.actionIBToolbar.setObjectName("actionIBToolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.actionIBToolbar)
        self.connectToIB = QtWidgets.QAction(MainWindow)
        self.connectToIB.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../local-packages/localUtilities/icons/ConnectNo.ico"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../../local-packages/localUtilities/icons/ConnectEstablished.ico"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("../../local-packages/localUtilities/icons/ConnectCreating.ico"),
                        QtGui.QIcon.Active, QtGui.QIcon.On)
        self.connectToIB.setIcon(icon1)
        self.connectToIB.setObjectName("connectToIB")
        self.actiontestIB = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../local-packages/localUtilities/icons/py_pic.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actiontestIB.setIcon(icon2)
        self.actiontestIB.setObjectName("actiontestIB")
        self.actiontestCheckableIB = QtWidgets.QAction(MainWindow)
        self.actiontestCheckableIB.setCheckable(True)
        self.actiontestCheckableIB.setChecked(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../local-packages/localUtilities/icons/about.gif"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actiontestCheckableIB.setIcon(icon3)
        self.actiontestCheckableIB.setObjectName("actiontestCheckableIB")
        self.actionIBToolbar.addAction(self.connectToIB)

        # this is not part of the QT Creator for setupUi()
        # These are the function connectors
        self.updateConnect()

        # don't forget these from QT
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi -- goes below:
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IB Options"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Underlying"))
        self.updateQualifyClose.setText(_translate("MainWindow", "Qualify Close"))
        self.radioButton_Index.setText(_translate("MainWindow", "Index"))
        self.radioButton_Stock.setText(_translate("MainWindow", "Stock "))
        self.radioButton_Option.setText(_translate("MainWindow", "Option"))
        self.label_8.setText(_translate("MainWindow", "Underlying:"))
        self.labelExchange.setText(_translate("MainWindow", "Exchange:"))
        self.label.setText(_translate("MainWindow", "Expiry"))
        self.comboBoxExchange.setItemText(0, _translate("MainWindow", "CBOE"))
        self.comboBoxExchange.setItemText(1, _translate("MainWindow", "SMART"))
        self.comboBoxExchange.setItemText(2, _translate("MainWindow", "ISLAND"))
        self.comboBoxExchange.setItemText(3, _translate("MainWindow", "NYSE"))
        self.comboBoxExchange.setItemText(4, _translate("MainWindow", "AMEX"))
        self.comboBoxExchange.setItemText(5, _translate("MainWindow", "IDEAL"))
        self.comboBoxExchange.setItemText(6, _translate("MainWindow", "PHLX"))
        self.groupBox_StrikePrice.setTitle(_translate("MainWindow", "Strkie Price"))
        self.label_4.setText(_translate("MainWindow", "Range"))
        self.label_3.setText(_translate("MainWindow", "Multiple"))
        self.comboBox.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox.setItemText(2, _translate("MainWindow", "15"))
        self.comboBox.setItemText(3, _translate("MainWindow", "20"))
        self.comboBox.setItemText(4, _translate("MainWindow", "25"))
        self.comboBox.setItemText(5, _translate("MainWindow", "30"))
        self.comboBox.setItemText(6, _translate("MainWindow", "35"))
        self.comboBox.setItemText(7, _translate("MainWindow", "40"))
        self.comboBox.setItemText(8, _translate("MainWindow", "45"))
        self.comboBox.setItemText(9, _translate("MainWindow", "50"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "20"))
        self.radioButton_Call.setText(_translate("MainWindow", "Call"))
        self.radioButton_Put.setText(_translate("MainWindow", "Put"))
        self.actionIBToolbar.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.connectToIB.setText(_translate("MainWindow", "Connect to IB "))
        self.connectToIB.setToolTip(_translate("MainWindow", "Connect to IB api"))
        self.actiontestIB.setText(_translate("MainWindow", "test"))
        self.actiontestIB.setToolTip(_translate("MainWindow", "Bark"))
        self.actiontestCheckableIB.setText(_translate("MainWindow", "testCheckable"))
        self.actiontestCheckableIB.setToolTip(_translate("MainWindow", "Meow"))

        # this is not part of the QT Creator for retranslateUi()
        self.doExpiry(_translate)

    def doExpiry(self, _translate):
        """Create a list of 18 Months of Option Fridays
        for the Expiry DropDown: comboBox_Expiry

        Keyword arguments:
        none
        """
        orderNum = 0
        expiry_list = dateUtils.getExpiries()
        for anExpiry in expiry_list:
            self.comboBox_Expiry.addItem("")
            self.comboBox_Expiry.setItemText(orderNum, _translate("MainWindow", anExpiry))
            orderNum += 1

    def get_underlying_info(self):
        self.statusbar.clearMessage()
        the_underlying = self.underlyingText.text()
        the_exchange = self.comboBoxExchange.currentText()

        a=self.security_type(the_underlying, the_exchange)
        try:
            get_underlying = self.ib.qualifyContracts(a)
        except ConnectionError:
            self.statusbar.showMessage("NOT CONNECTED")
            return
        if not get_underlying:  # empty list - failed qualifyContract
            self.statusbar.showMessage("Underlying: " + the_underlying + " not recognized!")
        else:
            print('self.comboBoxExchange.currentText(): ', self.comboBoxExchange.currentText())
            a_qualified_contract = get_underlying.pop()
            self.statusbar.showMessage(str(a_qualified_contract))
            buildOptionMatrices.qualify_option_chain_close(self.ib, a_qualified_contract,
                                                           self.right(), self.comboBoxExchange.currentText())


    def right(self):
        if self.radioButton_Call.isChecked():
            return 'C'
        else:
            return 'P'


    def security_type(self, the_underlying, the_exchange):
        if self.radioButton_Index.isChecked():
            a_underlying = Index(the_underlying, the_exchange)
        elif self.radioButton_Stock.isChecked():
            a_underlying = Stock(the_underlying, the_exchange)
        else:
            print('<<<< in bullSpreadViewSmall.get_underlying_info(self)>>>>> Option Radio not !completed!')
        return a_underlying

    def updateConnect(self):
        self.updateQualifyClose.clicked.connect(self.get_underlying_info)
        self.connectToIB.triggered.connect(self.onConnectButtonClicked)


    def onConnectButtonClicked(self):
        if self.connectToIB.isChecked():
            self.ib.connect(configIB.IB_API_HOST,
                        configIB.IB_PAPER_TRADE_PORT,
                        configIB.IB_API_CLIENTID_1)
            self.statusbar.showMessage("Connected to IB")
        else:
            self.ib.disconnect()
            # had an issue with disconnecting
            # as disconnect is not accure on the IB Gateway
            # but was disconnected in my code found this thread
            # https://github.com/erdewit/ib_insync/issues/10
            # adding the loop works - not sure why 4/15/18 - mrk
            # loop = asyncio.get_event_loop()
            # loop.run_until_complete(asyncio.sleep(0))
            self.statusbar.showMessage("Disconnected from IB")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

