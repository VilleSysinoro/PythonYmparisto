# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):

    # Luodaan pääikkuna
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        # Määritellään päävimpain, jonka sisälle muut vimpaimet sijoitetaan
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Määritellään käyttöliittymäelementit päävimpaimen sisälle
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 113, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 80, 111, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 20, 75, 23))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 20, 75, 23))

        # Tehdään oletusfontista poikkeava fonttiasetus
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(10)
        font.setBold(False)

        # Käytetään fonttiasetusta painikkeessa
        self.pushButton_2.setFont(font)

        # Määritellään painikkeen tyyliasetukset
        self.pushButton_2.setStyleSheet(u"background-color: rgb(202, 119, 71);")

        # Asetetaan pääikkunan päävimpain
        MainWindow.setCentralWidget(self.centralwidget)

        # Määritellään valikko- ja tilarivit
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")

        # Luodaan tyhjä valikkorivi
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        # Luodaan tilarivi
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Kutsutaan metodia, joka muodostaa 8 bittiset elementtien nimet
        self.retranslateUi(MainWindow)

        # Määritellään signaali, joka annetaan kun tekstikenttää "lineEdit" muokataan
        self.lineEdit.textChanged.connect(self.label.setText)

        QMetaObject.connectSlotsByName(MainWindow)

    # Metodi elementtien nimien muuttamiseksi Unicode -> UTF-8
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
    

