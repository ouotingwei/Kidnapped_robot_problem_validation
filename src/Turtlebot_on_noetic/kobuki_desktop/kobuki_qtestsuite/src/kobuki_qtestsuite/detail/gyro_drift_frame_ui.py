# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/gyro_drift_frame.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gyro_drift_frame(object):
    def setupUi(self, gyro_drift_frame):
        gyro_drift_frame.setObjectName("gyro_drift_frame")
        gyro_drift_frame.resize(791, 414)
        gyro_drift_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        gyro_drift_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(gyro_drift_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_browser = QtWidgets.QTextBrowser(gyro_drift_frame)
        self.text_browser.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle("")
        self.text_browser.setSource(QtCore.QUrl("qrc:/text/gyro_drift.html"))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout_2.addWidget(self.text_browser, 0, 0, 1, 1)
        self.scan_angle_group_box = QtWidgets.QGroupBox(gyro_drift_frame)
        self.scan_angle_group_box.setObjectName("scan_angle_group_box")
        self.gridLayout_2.addWidget(self.scan_angle_group_box, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(gyro_drift_frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(96, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.angular_speed_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.angular_speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.angular_speed_spinbox.setPrefix("")
        self.angular_speed_spinbox.setMaximum(3.14)
        self.angular_speed_spinbox.setSingleStep(0.1)
        self.angular_speed_spinbox.setProperty("value", 0.4)
        self.angular_speed_spinbox.setObjectName("angular_speed_spinbox")
        self.gridLayout.addWidget(self.angular_speed_spinbox, 0, 2, 1, 1)
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

        self.retranslateUi(gyro_drift_frame)
        QtCore.QMetaObject.connectSlotsByName(gyro_drift_frame)

    def retranslateUi(self, gyro_drift_frame):
        _translate = QtCore.QCoreApplication.translate
        gyro_drift_frame.setWindowTitle(_translate("gyro_drift_frame", "Frame"))
        self.scan_angle_group_box.setTitle(_translate("gyro_drift_frame", "Gyro vs Laser"))
        self.groupBox.setTitle(_translate("gyro_drift_frame", "Controls"))
        self.label_2.setText(_translate("gyro_drift_frame", "Angular Speed"))
        self.angular_speed_spinbox.setSuffix(_translate("gyro_drift_frame", " rad/s"))
        self.start_button.setText(_translate("gyro_drift_frame", "Start"))
        self.stop_button.setText(_translate("gyro_drift_frame", "Stop"))
import common_rc
import text_rc
