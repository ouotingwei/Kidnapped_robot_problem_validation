# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/payload_frame.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_payload_frame(object):
    def setupUi(self, payload_frame):
        payload_frame.setObjectName("payload_frame")
        payload_frame.resize(791, 414)
        payload_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        payload_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(payload_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_browser = QtWidgets.QTextBrowser(payload_frame)
        self.text_browser.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle("")
        self.text_browser.setSource(QtCore.QUrl("qrc:/text/payload.html"))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName("text_browser")
        self.verticalLayout.addWidget(self.text_browser)
        self.groupBox = QtWidgets.QGroupBox(payload_frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(96, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.speed_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speed_spinbox.setPrefix("")
        self.speed_spinbox.setMaximum(0.7)
        self.speed_spinbox.setSingleStep(0.1)
        self.speed_spinbox.setProperty("value", 0.3)
        self.speed_spinbox.setObjectName("speed_spinbox")
        self.gridLayout.addWidget(self.speed_spinbox, 0, 2, 2, 1)
        self.distance_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.distance_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.distance_spinbox.setPrefix("")
        self.distance_spinbox.setMaximum(2.0)
        self.distance_spinbox.setSingleStep(0.1)
        self.distance_spinbox.setProperty("value", 1.0)
        self.distance_spinbox.setObjectName("distance_spinbox")
        self.gridLayout.addWidget(self.distance_spinbox, 0, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        self.stop_button = QtWidgets.QPushButton(self.groupBox)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 1, 3, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(181, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.groupBox)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 4, 1, 3)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(payload_frame)
        QtCore.QMetaObject.connectSlotsByName(payload_frame)

    def retranslateUi(self, payload_frame):
        _translate = QtCore.QCoreApplication.translate
        payload_frame.setWindowTitle(_translate("payload_frame", "Frame"))
        self.groupBox.setTitle(_translate("payload_frame", "Controls"))
        self.label_2.setText(_translate("payload_frame", "Speed"))
        self.speed_spinbox.setSuffix(_translate("payload_frame", " m/s"))
        self.distance_spinbox.setSuffix(_translate("payload_frame", "m"))
        self.label_3.setText(_translate("payload_frame", "Side Length"))
        self.stop_button.setText(_translate("payload_frame", "Stop"))
        self.start_button.setText(_translate("payload_frame", "Start"))
import common_rc
import text_rc
