# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stged_mw.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.modetab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modetab.sizePolicy().hasHeightForWidth())
        self.modetab.setSizePolicy(sizePolicy)
        self.modetab.setMinimumSize(QtCore.QSize(207, 0))
        self.modetab.setObjectName("modetab")
        self.normal = QtWidgets.QWidget()
        self.normal.setObjectName("normal")
        self.modetab.addTab(self.normal, "")
        self.crusader = QtWidgets.QWidget()
        self.crusader.setObjectName("crusader")
        self.modetab.addTab(self.crusader, "")
        self.deathmatch = QtWidgets.QWidget()
        self.deathmatch.setObjectName("deathmatch")
        self.modetab.addTab(self.deathmatch, "")
        self.horizontalLayout_5.addWidget(self.modetab)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.wood = QtWidgets.QSpinBox(self.groupBox)
        self.wood.setMaximum(65535)
        self.wood.setObjectName("wood")
        self.verticalLayout.addWidget(self.wood)
        self.stone = QtWidgets.QSpinBox(self.groupBox)
        self.stone.setMaximum(65535)
        self.stone.setObjectName("stone")
        self.verticalLayout.addWidget(self.stone)
        self.iron = QtWidgets.QSpinBox(self.groupBox)
        self.iron.setMaximum(65535)
        self.iron.setObjectName("iron")
        self.verticalLayout.addWidget(self.iron)
        self.pitch = QtWidgets.QSpinBox(self.groupBox)
        self.pitch.setMaximum(65535)
        self.pitch.setObjectName("pitch")
        self.verticalLayout.addWidget(self.pitch)
        self.hop = QtWidgets.QSpinBox(self.groupBox)
        self.hop.setMaximum(65535)
        self.hop.setObjectName("hop")
        self.verticalLayout.addWidget(self.hop)
        self.wheat = QtWidgets.QSpinBox(self.groupBox)
        self.wheat.setMaximum(65535)
        self.wheat.setObjectName("wheat")
        self.verticalLayout.addWidget(self.wheat)
        self.beer = QtWidgets.QSpinBox(self.groupBox)
        self.beer.setMaximum(65535)
        self.beer.setObjectName("beer")
        self.verticalLayout.addWidget(self.beer)
        self.flour = QtWidgets.QSpinBox(self.groupBox)
        self.flour.setMaximum(65535)
        self.flour.setObjectName("flour")
        self.verticalLayout.addWidget(self.flour)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox1.setFlat(False)
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox1)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.groupBox1)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.label_20 = QtWidgets.QLabel(self.groupBox1)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        self.label_19 = QtWidgets.QLabel(self.groupBox1)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.meat = QtWidgets.QSpinBox(self.groupBox1)
        self.meat.setMaximum(65535)
        self.meat.setObjectName("meat")
        self.verticalLayout_6.addWidget(self.meat)
        self.fruit = QtWidgets.QSpinBox(self.groupBox1)
        self.fruit.setMaximum(65535)
        self.fruit.setObjectName("fruit")
        self.verticalLayout_6.addWidget(self.fruit)
        self.cheese = QtWidgets.QSpinBox(self.groupBox1)
        self.cheese.setMaximum(65535)
        self.cheese.setObjectName("cheese")
        self.verticalLayout_6.addWidget(self.cheese)
        self.bread = QtWidgets.QSpinBox(self.groupBox1)
        self.bread.setMaximum(65535)
        self.bread.setObjectName("bread")
        self.verticalLayout_6.addWidget(self.bread)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox2.setObjectName("groupBox2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_21 = QtWidgets.QLabel(self.groupBox2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.label_24 = QtWidgets.QLabel(self.groupBox2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_7.addWidget(self.label_24)
        self.label_22 = QtWidgets.QLabel(self.groupBox2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_7.addWidget(self.label_22)
        self.label_25 = QtWidgets.QLabel(self.groupBox2)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_7.addWidget(self.label_25)
        self.label_23 = QtWidgets.QLabel(self.groupBox2)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_7.addWidget(self.label_23)
        self.label_26 = QtWidgets.QLabel(self.groupBox2)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_7.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.groupBox2)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_7.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.groupBox2)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_7.addWidget(self.label_28)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.bows = QtWidgets.QSpinBox(self.groupBox2)
        self.bows.setMaximum(65535)
        self.bows.setObjectName("bows")
        self.verticalLayout_8.addWidget(self.bows)
        self.crossbows = QtWidgets.QSpinBox(self.groupBox2)
        self.crossbows.setMaximum(65535)
        self.crossbows.setObjectName("crossbows")
        self.verticalLayout_8.addWidget(self.crossbows)
        self.spears = QtWidgets.QSpinBox(self.groupBox2)
        self.spears.setMaximum(65535)
        self.spears.setObjectName("spears")
        self.verticalLayout_8.addWidget(self.spears)
        self.pikes = QtWidgets.QSpinBox(self.groupBox2)
        self.pikes.setMaximum(65535)
        self.pikes.setObjectName("pikes")
        self.verticalLayout_8.addWidget(self.pikes)
        self.maces = QtWidgets.QSpinBox(self.groupBox2)
        self.maces.setMaximum(65535)
        self.maces.setObjectName("maces")
        self.verticalLayout_8.addWidget(self.maces)
        self.swords = QtWidgets.QSpinBox(self.groupBox2)
        self.swords.setMaximum(65535)
        self.swords.setObjectName("swords")
        self.verticalLayout_8.addWidget(self.swords)
        self.leatherarmor = QtWidgets.QSpinBox(self.groupBox2)
        self.leatherarmor.setMaximum(65535)
        self.leatherarmor.setObjectName("leatherarmor")
        self.verticalLayout_8.addWidget(self.leatherarmor)
        self.metalarmor = QtWidgets.QSpinBox(self.groupBox2)
        self.metalarmor.setMaximum(65535)
        self.metalarmor.setObjectName("metalarmor")
        self.verticalLayout_8.addWidget(self.metalarmor)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_2.addWidget(self.groupBox2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.groupBox3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox3.setObjectName("groupBox3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox3)
        self.gridLayout.setObjectName("gridLayout")
        self.humangold0 = QtWidgets.QSpinBox(self.groupBox3)
        self.humangold0.setMaximum(65535)
        self.humangold0.setObjectName("humangold0")
        self.gridLayout.addWidget(self.humangold0, 0, 0, 1, 1)
        self.humangold1 = QtWidgets.QSpinBox(self.groupBox3)
        self.humangold1.setMaximum(65535)
        self.humangold1.setObjectName("humangold1")
        self.gridLayout.addWidget(self.humangold1, 0, 1, 1, 1)
        self.humangold2 = QtWidgets.QSpinBox(self.groupBox3)
        self.humangold2.setMaximum(65535)
        self.humangold2.setObjectName("humangold2")
        self.gridLayout.addWidget(self.humangold2, 0, 2, 1, 1)
        self.humangold4 = QtWidgets.QSpinBox(self.groupBox3)
        self.humangold4.setMaximum(65535)
        self.humangold4.setObjectName("humangold4")
        self.gridLayout.addWidget(self.humangold4, 0, 4, 1, 1)
        self.humangold3 = QtWidgets.QSpinBox(self.groupBox3)
        self.humangold3.setMaximum(65535)
        self.humangold3.setObjectName("humangold3")
        self.gridLayout.addWidget(self.humangold3, 0, 3, 1, 1)
        self.aigold1 = QtWidgets.QSpinBox(self.groupBox3)
        self.aigold1.setMaximum(65535)
        self.aigold1.setObjectName("aigold1")
        self.gridLayout.addWidget(self.aigold1, 2, 1, 1, 1)
        self.aigold2 = QtWidgets.QSpinBox(self.groupBox3)
        self.aigold2.setMaximum(65535)
        self.aigold2.setObjectName("aigold2")
        self.gridLayout.addWidget(self.aigold2, 2, 2, 1, 1)
        self.aigold0 = QtWidgets.QSpinBox(self.groupBox3)
        self.aigold0.setMaximum(65535)
        self.aigold0.setObjectName("aigold0")
        self.gridLayout.addWidget(self.aigold0, 2, 0, 1, 1)
        self.aigold3 = QtWidgets.QSpinBox(self.groupBox3)
        self.aigold3.setMaximum(65535)
        self.aigold3.setObjectName("aigold3")
        self.gridLayout.addWidget(self.aigold3, 2, 3, 1, 1)
        self.aigold4 = QtWidgets.QSpinBox(self.groupBox3)
        self.aigold4.setMaximum(65535)
        self.aigold4.setObjectName("aigold4")
        self.gridLayout.addWidget(self.aigold4, 2, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox3)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox3)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.groupBox3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 3, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.groupBox3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 4, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupBox3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.modetab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Start Goods Editor - UCPREGUI"))
        self.modetab.setTabText(self.modetab.indexOf(self.normal), _translate("MainWindow", "Normal"))
        self.modetab.setTabText(self.modetab.indexOf(self.crusader), _translate("MainWindow", "Crusader"))
        self.modetab.setTabText(self.modetab.indexOf(self.deathmatch), _translate("MainWindow", "Deathmatch"))
        self.groupBox.setTitle(_translate("MainWindow", "Stockpile"))
        self.label.setText(_translate("MainWindow", "Wood"))
        self.label_3.setText(_translate("MainWindow", "Stone"))
        self.label_4.setText(_translate("MainWindow", "Iron"))
        self.label_5.setText(_translate("MainWindow", "Pitch"))
        self.label_2.setText(_translate("MainWindow", "Hop"))
        self.label_6.setText(_translate("MainWindow", "Wheat"))
        self.label_7.setText(_translate("MainWindow", "Beer"))
        self.label_8.setText(_translate("MainWindow", "Flour"))
        self.groupBox1.setTitle(_translate("MainWindow", "Granary"))
        self.label_17.setText(_translate("MainWindow", "Meat"))
        self.label_18.setText(_translate("MainWindow", "Fruit"))
        self.label_20.setText(_translate("MainWindow", "Cheese"))
        self.label_19.setText(_translate("MainWindow", "Bread"))
        self.groupBox2.setTitle(_translate("MainWindow", "Armoury"))
        self.label_21.setText(_translate("MainWindow", "Bows"))
        self.label_24.setText(_translate("MainWindow", "Crossbows"))
        self.label_22.setText(_translate("MainWindow", "Spears"))
        self.label_25.setText(_translate("MainWindow", "Pikes"))
        self.label_23.setText(_translate("MainWindow", "Maces"))
        self.label_26.setText(_translate("MainWindow", "Swords"))
        self.label_27.setText(_translate("MainWindow", "Leather Armor"))
        self.label_28.setText(_translate("MainWindow", "Metal Armor"))
        self.groupBox3.setTitle(_translate("MainWindow", "Starting Gold"))
        self.label_9.setText(_translate("MainWindow", "Human Gold"))
        self.label_10.setText(_translate("MainWindow", "AI Gold"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
