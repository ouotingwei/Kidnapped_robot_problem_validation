# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/battery_profile_frame.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_battery_profile_frame(object):
    def setupUi(self, battery_profile_frame):
        battery_profile_frame.setObjectName("battery_profile_frame")
        battery_profile_frame.resize(791, 414)
        battery_profile_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        battery_profile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(battery_profile_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_browser = QtWidgets.QTextBrowser(battery_profile_frame)
        self.text_browser.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle("")
        self.text_browser.setSource(QtCore.QUrl("qrc:/text/battery_profile.html"))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout_2.addWidget(self.text_browser, 0, 0, 1, 1)
        self.battery_profile_group_box = QtWidgets.QGroupBox(battery_profile_frame)
        self.battery_profile_group_box.setObjectName("battery_profile_group_box")
        self.gridLayout_2.addWidget(self.battery_profile_group_box, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(battery_profile_frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(96, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.angular_speed_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.angular_speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.angular_speed_spinbox.setPrefix("")
        self.angular_speed_spinbox.setMaximum(3.14)
        self.angular_speed_spinbox.setSingleStep(0.1)
        self.angular_speed_spinbox.setProperty("value", 1.2)
        self.angular_speed_spinbox.setObjectName("angular_speed_spinbox")
        self.gridLayout.addWidget(self.angular_speed_spinbox, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(181, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.groupBox)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 1, 1, 1, 1)
        self.stop_button = QtWidgets.QPushButton(self.groupBox)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(battery_profile_frame)
        QtCore.QMetaObject.connectSlotsByName(battery_profile_frame)

    def retranslateUi(self, battery_profile_frame):
        _translate = QtCore.QCoreApplication.translate
        battery_profile_frame.setWindowTitle(_translate("battery_profile_frame", "Frame"))
        self.battery_profile_group_box.setTitle(_translate("battery_profile_frame", "Battery Profile"))
        self.groupBox.setTitle(_translate("battery_profile_frame", "Controls"))
        self.angular_speed_spinbox.setSuffix(_translate("battery_profile_frame", " rad/s"))
        self.start_button.setText(_translate("battery_profile_frame", "Start"))
        self.stop_button.setText(_translate("battery_profile_frame", "Stop"))
import text_rc
