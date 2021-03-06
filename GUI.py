# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KoledarWindow(object):
    def setupUi(self, KoledarWindow):
        KoledarWindow.setObjectName("KoledarWindow")
        KoledarWindow.resize(300, 400)
        KoledarWindow.setMinimumSize(QtCore.QSize(300, 400))
        KoledarWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(KoledarWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.meseci = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meseci.sizePolicy().hasHeightForWidth())
        self.meseci.setSizePolicy(sizePolicy)
        self.meseci.setObjectName("meseci")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.meseci.addItem("")
        self.horizontalLayout.addWidget(self.meseci)
        self.leto = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leto.sizePolicy().hasHeightForWidth())
        self.leto.setSizePolicy(sizePolicy)
        self.leto.setMaximum(3000)
        self.leto.setProperty("value", 2022)
        self.leto.setObjectName("leto")
        self.horizontalLayout.addWidget(self.leto)
        self.datumLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datumLine.sizePolicy().hasHeightForWidth())
        self.datumLine.setSizePolicy(sizePolicy)
        self.datumLine.setObjectName("datumLine")
        self.horizontalLayout.addWidget(self.datumLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.koledarLayout = QtWidgets.QGridLayout()
        self.koledarLayout.setObjectName("koledarLayout")
        self.gridLayout.addLayout(self.koledarLayout, 1, 0, 1, 1)
        KoledarWindow.setCentralWidget(self.centralwidget)
        self.actionOdpri = QtWidgets.QAction(KoledarWindow)
        self.actionOdpri.setObjectName("actionOdpri")
        self.actionIzhod = QtWidgets.QAction(KoledarWindow)
        self.actionIzhod.setObjectName("actionIzhod")

        self.retranslateUi(KoledarWindow)
        QtCore.QMetaObject.connectSlotsByName(KoledarWindow)

    def retranslateUi(self, KoledarWindow):
        _translate = QtCore.QCoreApplication.translate
        KoledarWindow.setWindowTitle(_translate("KoledarWindow", "Koledar Rok ??vikart"))
        self.meseci.setItemText(0, _translate("KoledarWindow", "Januar"))
        self.meseci.setItemText(1, _translate("KoledarWindow", "Februar"))
        self.meseci.setItemText(2, _translate("KoledarWindow", "Marec"))
        self.meseci.setItemText(3, _translate("KoledarWindow", "April"))
        self.meseci.setItemText(4, _translate("KoledarWindow", "Maj"))
        self.meseci.setItemText(5, _translate("KoledarWindow", "Junij"))
        self.meseci.setItemText(6, _translate("KoledarWindow", "Julij"))
        self.meseci.setItemText(7, _translate("KoledarWindow", "Avgust"))
        self.meseci.setItemText(8, _translate("KoledarWindow", "September"))
        self.meseci.setItemText(9, _translate("KoledarWindow", "Oktober"))
        self.meseci.setItemText(10, _translate("KoledarWindow", "November"))
        self.meseci.setItemText(11, _translate("KoledarWindow", "December"))
        self.datumLine.setPlaceholderText(_translate("KoledarWindow", "DD.MM.LLLL"))
        self.actionOdpri.setText(_translate("KoledarWindow", "Odpri"))
        self.actionIzhod.setText(_translate("KoledarWindow", "Izhod"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KoledarWindow = QtWidgets.QMainWindow()
    ui = Ui_KoledarWindow()
    ui.setupUi(KoledarWindow)
    KoledarWindow.show()
    sys.exit(app.exec_())
