# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/testsuite.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testsuite_widget(object):
    def setupUi(self, testsuite_widget):
        testsuite_widget.setObjectName("testsuite_widget")
        testsuite_widget.resize(1021, 562)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/kobuki_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        testsuite_widget.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(testsuite_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.testsuite_tab_widget = QtWidgets.QTabWidget(testsuite_widget)
        self.testsuite_tab_widget.setEnabled(True)
        self.testsuite_tab_widget.setObjectName("testsuite_tab_widget")
        self.battery_profile_tab = QtWidgets.QWidget()
        self.battery_profile_tab.setObjectName("battery_profile_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.battery_profile_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.battery_profile_frame = BatteryProfileFrame(self.battery_profile_tab)
        self.battery_profile_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.battery_profile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.battery_profile_frame.setObjectName("battery_profile_frame")
        self.verticalLayout_3.addWidget(self.battery_profile_frame)
        self.testsuite_tab_widget.addTab(self.battery_profile_tab, "")
        self.gyro_tab = QtWidgets.QWidget()
        self.gyro_tab.setObjectName("gyro_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gyro_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gyro_drift_frame = GyroDriftFrame(self.gyro_tab)
        self.gyro_drift_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gyro_drift_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gyro_drift_frame.setObjectName("gyro_drift_frame")
        self.verticalLayout_4.addWidget(self.gyro_drift_frame)
        self.testsuite_tab_widget.addTab(self.gyro_tab, "")
        self.payload_tab = QtWidgets.QWidget()
        self.payload_tab.setObjectName("payload_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.payload_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.payload_frame = PayloadFrame(self.payload_tab)
        self.payload_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.payload_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.payload_frame.setObjectName("payload_frame")
        self.verticalLayout_5.addWidget(self.payload_frame)
        self.testsuite_tab_widget.addTab(self.payload_tab, "")
        self.cliff_sensor_tab = QtWidgets.QWidget()
        self.cliff_sensor_tab.setObjectName("cliff_sensor_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.cliff_sensor_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cliff_sensor_frame = CliffSensorFrame(self.cliff_sensor_tab)
        self.cliff_sensor_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cliff_sensor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cliff_sensor_frame.setObjectName("cliff_sensor_frame")
        self.verticalLayout_6.addWidget(self.cliff_sensor_frame)
        self.testsuite_tab_widget.addTab(self.cliff_sensor_tab, "")
        self.life_tab = QtWidgets.QWidget()
        self.life_tab.setObjectName("life_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.life_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.life_frame = LifeFrame(self.life_tab)
        self.life_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.life_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.life_frame.setObjectName("life_frame")
        self.verticalLayout_7.addWidget(self.life_frame)
        self.testsuite_tab_widget.addTab(self.life_tab, "")
        self.wandering_tab = QtWidgets.QWidget()
        self.wandering_tab.setObjectName("wandering_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wandering_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wandering_frame = WanderingFrame(self.wandering_tab)
        self.wandering_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wandering_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wandering_frame.setObjectName("wandering_frame")
        self.verticalLayout_2.addWidget(self.wandering_frame)
        self.testsuite_tab_widget.addTab(self.wandering_tab, "")
        self.horizontalLayout.addWidget(self.testsuite_tab_widget)
        self.configuration_dock = ConfigurationDockWidget(testsuite_widget)
        self.configuration_dock.setObjectName("configuration_dock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.configuration_dock.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.configuration_dock)

        self.retranslateUi(testsuite_widget)
        self.testsuite_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(testsuite_widget)

    def retranslateUi(self, testsuite_widget):
        _translate = QtCore.QCoreApplication.translate
        testsuite_widget.setWindowTitle(_translate("testsuite_widget", "Kobuki Test Suite"))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.battery_profile_tab), _translate("testsuite_widget", "Battery Profile"))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.gyro_tab), _translate("testsuite_widget", "Gyro Drift"))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.payload_tab), _translate("testsuite_widget", "Payload"))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.cliff_sensor_tab), _translate("testsuite_widget", "Cliff"))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.life_tab), _translate("testsuite_widget", "Life"))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.wandering_tab), _translate("testsuite_widget", "Wander"))
from kobuki_qtestsuite.battery_profile_frame import BatteryProfileFrame
from kobuki_qtestsuite.cliff_sensor_frame import CliffSensorFrame
from kobuki_qtestsuite.configuration_dock_widget import ConfigurationDockWidget
from kobuki_qtestsuite.gyro_drift_frame import GyroDriftFrame
from kobuki_qtestsuite.life_frame import LifeFrame
from kobuki_qtestsuite.payload_frame import PayloadFrame
from kobuki_qtestsuite.wandering_frame import WanderingFrame
import common_rc
import text_rc
