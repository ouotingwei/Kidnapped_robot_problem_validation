# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/configuration_dock.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_configuration_dock_widget(object):
    def setupUi(self, configuration_dock_widget):
        configuration_dock_widget.setObjectName("configuration_dock_widget")
        configuration_dock_widget.resize(592, 385)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topic_group_box = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.topic_group_box.setObjectName("topic_group_box")
        self.gridLayout = QtWidgets.QGridLayout(self.topic_group_box)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.topic_group_box)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cmd_vel_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.cmd_vel_topic_combo_box.setEditable(False)
        self.cmd_vel_topic_combo_box.setObjectName("cmd_vel_topic_combo_box")
        self.gridLayout.addWidget(self.cmd_vel_topic_combo_box, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.topic_group_box)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.odom_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.odom_topic_combo_box.setEditable(False)
        self.odom_topic_combo_box.setObjectName("odom_topic_combo_box")
        self.gridLayout.addWidget(self.odom_topic_combo_box, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.topic_group_box)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.core_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.core_topic_combo_box.setEditable(False)
        self.core_topic_combo_box.setObjectName("core_topic_combo_box")
        self.gridLayout.addWidget(self.core_topic_combo_box, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.topic_group_box)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.robot_state_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.robot_state_topic_combo_box.setEditable(False)
        self.robot_state_topic_combo_box.setObjectName("robot_state_topic_combo_box")
        self.gridLayout.addWidget(self.robot_state_topic_combo_box, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.topic_group_box)
        spacerItem = QtWidgets.QSpacerItem(20, 126, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        configuration_dock_widget.setWidget(self.dockWidgetContents)

        self.retranslateUi(configuration_dock_widget)
        QtCore.QMetaObject.connectSlotsByName(configuration_dock_widget)

    def retranslateUi(self, configuration_dock_widget):
        _translate = QtCore.QCoreApplication.translate
        configuration_dock_widget.setWindowTitle(_translate("configuration_dock_widget", "Configuration Dock"))
        self.topic_group_box.setTitle(_translate("configuration_dock_widget", "Topics"))
        self.label.setText(_translate("configuration_dock_widget", "Cmd Vel"))
        self.label_4.setText(_translate("configuration_dock_widget", "Odom"))
        self.label_5.setText(_translate("configuration_dock_widget", "Core Sensors"))
        self.label_6.setText(_translate("configuration_dock_widget", "Robot State"))
from rqt_py_common.extended_combo_box import ExtendedComboBox
