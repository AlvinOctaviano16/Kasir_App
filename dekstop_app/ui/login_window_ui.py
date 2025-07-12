# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 601, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(0, QFormLayout.ItemRole.FieldRole, self.verticalSpacer_2)

        self.login_tittle = QLabel(self.verticalLayoutWidget)
        self.login_tittle.setObjectName(u"login_tittle")
        self.login_tittle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_tittle.setMargin(0)
        self.login_tittle.setIndent(-1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.login_tittle)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.ItemRole.FieldRole, self.verticalSpacer)

        self.username_label = QLabel(self.verticalLayoutWidget)
        self.username_label.setObjectName(u"username_label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.username_label)

        self.username_input = QLineEdit(self.verticalLayoutWidget)
        self.username_input.setObjectName(u"username_input")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.username_input)

        self.password_label = QLabel(self.verticalLayoutWidget)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.password_label)

        self.password_input = QLineEdit(self.verticalLayoutWidget)
        self.password_input.setObjectName(u"password_input")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.password_input)

        self.login_button = QPushButton(self.verticalLayoutWidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.login_button.setAutoFillBackground(True)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.login_button)


        self.verticalLayout.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_tittle.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

