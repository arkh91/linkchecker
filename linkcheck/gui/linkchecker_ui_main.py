# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Sat Nov  6 13:44:31 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 533)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(4)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.urlinput = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlinput.sizePolicy().hasHeightForWidth())
        self.urlinput.setSizePolicy(sizePolicy)
        self.urlinput.setObjectName("urlinput")
        self.horizontalLayout_3.addWidget(self.urlinput)
        self.controlButton = QtGui.QPushButton(self.centralwidget)
        self.controlButton.setStatusTip("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.controlButton.setIcon(icon1)
        self.controlButton.setDefault(True)
        self.controlButton.setObjectName("controlButton")
        self.horizontalLayout_3.addWidget(self.controlButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setItemsExpandable(False)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAllColumnsShowFocus(True)
        self.treeView.setExpandsOnDoubleClick(False)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        self.menuLinkChecka = QtGui.QMenu(self.menubar)
        self.menuLinkChecka.setObjectName("menuLinkChecka")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon4)
        self.actionHelp.setObjectName("actionHelp")
        self.actionViewOnline = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/online.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewOnline.setIcon(icon5)
        self.actionViewOnline.setObjectName("actionViewOnline")
        self.actionOptions = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon6)
        self.actionOptions.setObjectName("actionOptions")
        self.actionCopyToClipboard = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopyToClipboard.setIcon(icon7)
        self.actionCopyToClipboard.setObjectName("actionCopyToClipboard")
        self.actionViewParentOnline = QtGui.QAction(MainWindow)
        self.actionViewParentOnline.setIcon(icon5)
        self.actionViewParentOnline.setObjectName("actionViewParentOnline")
        self.actionViewParentSource = QtGui.QAction(MainWindow)
        self.actionViewParentSource.setIcon(icon5)
        self.actionViewParentSource.setObjectName("actionViewParentSource")
        self.actionDebug = QtGui.QAction(MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.actionViewProperties = QtGui.QAction(MainWindow)
        self.actionViewProperties.setObjectName("actionViewProperties")
        self.menuLinkChecka.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionDebug)
        self.menubar.addAction(self.menuLinkChecka.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.urlinput)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_("LinkChecker"))
        self.label.setText(_("URL"))
        self.controlButton.setToolTip(_("Start checking the given URL."))
        self.controlButton.setText(_("Start"))
        self.menuLinkChecka.setTitle(_("File"))
        self.menuEdit.setTitle(_("Edit"))
        self.menuHelp.setTitle(_("Help"))
        self.actionQuit.setText(_("Quit"))
        self.actionQuit.setShortcut(_("Ctrl+Q"))
        self.actionAbout.setText(_("About"))
        self.actionHelp.setText(_("Help"))
        self.actionViewOnline.setText(_("View online"))
        self.actionViewOnline.setToolTip(_("View URL online"))
        self.actionOptions.setText(_("Options"))
        self.actionCopyToClipboard.setText(_("Copy to clipboard"))
        self.actionCopyToClipboard.setToolTip(_("Copy URL to clipboard"))
        self.actionCopyToClipboard.setShortcut(_("Ctrl+C"))
        self.actionViewParentOnline.setText(_("View parent online"))
        self.actionViewParentOnline.setToolTip(_("View parent URL online"))
        self.actionViewParentSource.setText(_("View parent source"))
        self.actionViewParentSource.setToolTip(_("View parent URL source"))
        self.actionDebug.setText(_("Debug"))
        self.actionViewProperties.setText(_("View properties"))
        self.actionViewProperties.setToolTip(_("View URL properties"))

import linkchecker_rc
