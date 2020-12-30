# -*- coding: utf-8 -*-
"""
Application : Smart Ocr tool with NLP Algorithm
@author: Raj Dalsaniya
"""
# Form implementation generated from reading ui file 'Video_Extration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget
from PyQt5.QtGui import QPixmap
from PIL import Image
import pytesseract

class Ui_SMART_OCR(QWidget):
    
    """ MAIN CLass For all GUI Instance"""
    
    def setupUi(self, SMART_OCR):
        SMART_OCR.setObjectName("SMART_OCR")
        SMART_OCR.resize(1385, 720)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        SMART_OCR.setFont(font)
        self.Central_Widget_OCR = QtWidgets.QWidget(SMART_OCR)
        self.Central_Widget_OCR.setObjectName("Central_Widget_OCR")
        self.Input_Window = QtWidgets.QLabel(self.Central_Widget_OCR)
        self.Input_Window.setGeometry(QtCore.QRect(30, 80, 391, 471))
        self.Input_Window.setStyleSheet("")
        self.Input_Window.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Input_Window.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Input_Window.setLineWidth(6)
        self.Input_Window.setMidLineWidth(6)
        self.Input_Window.setText("")
        self.Input_Window.setObjectName("Input_Window")
        self.Input_Label = QtWidgets.QTextBrowser(self.Central_Widget_OCR)
        self.Input_Label.setGeometry(QtCore.QRect(30, 20, 391, 51))
        self.Input_Label.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(106, 186, 255)\n"
"")
        self.Input_Label.setObjectName("Input_Label")
        self.Output_Label = QtWidgets.QTextBrowser(self.Central_Widget_OCR)
        self.Output_Label.setGeometry(QtCore.QRect(450, 160, 321, 51))
        self.Output_Label.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(106, 186, 255)\n"
"")
        self.Output_Label.setObjectName("Output_Label")
        self.Output_Window = QtWidgets.QLabel(self.Central_Widget_OCR)
        self.Output_Window.setGeometry(QtCore.QRect(450, 230, 321, 321))
        self.Output_Window.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Output_Window.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Output_Window.setLineWidth(6)
        self.Output_Window.setMidLineWidth(6)
        self.Output_Window.setText("")
        self.Output_Window.setObjectName("Output_Window")
        self.Translator_Label = QtWidgets.QTextBrowser(self.Central_Widget_OCR)
        self.Translator_Label.setGeometry(QtCore.QRect(800, 160, 321, 51))
        self.Translator_Label.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(106, 186, 255)\n"
"")
        self.Translator_Label.setObjectName("Translator_Label")
        self.Translator_Window = QtWidgets.QLabel(self.Central_Widget_OCR)
        self.Translator_Window.setGeometry(QtCore.QRect(800, 230, 321, 321))
        self.Translator_Window.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Translator_Window.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Translator_Window.setLineWidth(6)
        self.Translator_Window.setMidLineWidth(6)
        self.Translator_Window.setText("")
        self.Translator_Window.setObjectName("Translator_Window")
        self.Convert_Button = QtWidgets.QPushButton(self.Central_Widget_OCR)
        self.Convert_Button.setGeometry(QtCore.QRect(240, 570, 171, 51))
        self.Convert_Button.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(106, 186, 255)\n"
"")
        self.Convert_Button.setObjectName("Convert_Button")
        self.Exit_Button = QtWidgets.QPushButton(self.Central_Widget_OCR)
        self.Exit_Button.setGeometry(QtCore.QRect(660, 570, 171, 51))
        self.Exit_Button.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.Exit_Button.setObjectName("Exit_Button")
        self.Translator_Button = QtWidgets.QPushButton(self.Central_Widget_OCR)
        self.Translator_Button.setGeometry(QtCore.QRect(450, 570, 171, 51))
        self.Translator_Button.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(255, 170, 0)\n"
"")
        self.Translator_Button.setObjectName("Translator_Button")
        self.Help_Button = QtWidgets.QPushButton(self.Central_Widget_OCR)
        self.Help_Button.setGeometry(QtCore.QRect(870, 570, 171, 51))
        self.Help_Button.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(255, 137, 250)\n"
"")
        self.Help_Button.setObjectName("Help_Button")
        self.layoutWidget = QtWidgets.QWidget(self.Central_Widget_OCR)
        self.layoutWidget.setGeometry(QtCore.QRect(450, 20, 620, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Vert_CheckBox = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Vert_CheckBox.setContentsMargins(0, 0, 0, 0)
        self.Vert_CheckBox.setObjectName("Vert_CheckBox")
        self.Img_Filter_Label = QtWidgets.QTextBrowser(self.layoutWidget)
        self.Img_Filter_Label.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(106, 186, 255)\n"
"")
        self.Img_Filter_Label.setObjectName("Img_Filter_Label")
        self.Vert_CheckBox.addWidget(self.Img_Filter_Label)
        self.Hori_CheckBox = QtWidgets.QHBoxLayout()
        self.Hori_CheckBox.setObjectName("Hori_CheckBox")
        self.Skwe_Corr_Box = QtWidgets.QCheckBox(self.layoutWidget)
        self.Skwe_Corr_Box.setObjectName("Skwe_Corr_Box")
        self.Hori_CheckBox.addWidget(self.Skwe_Corr_Box)
        self.Blurr_Corr_Box = QtWidgets.QCheckBox(self.layoutWidget)
        self.Blurr_Corr_Box.setObjectName("Blurr_Corr_Box")
        self.Hori_CheckBox.addWidget(self.Blurr_Corr_Box)
        self.No_Filter_Box = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.No_Filter_Box.setFont(font)
        self.No_Filter_Box.setObjectName("No_Filter_Box")
        self.Hori_CheckBox.addWidget(self.No_Filter_Box)
        self.Thresh_Corr_Box = QtWidgets.QCheckBox(self.layoutWidget)
        self.Thresh_Corr_Box.setObjectName("Thresh_Corr_Box")
        self.Hori_CheckBox.addWidget(self.Thresh_Corr_Box)
        self.Vert_CheckBox.addLayout(self.Hori_CheckBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.Central_Widget_OCR)
        self.layoutWidget1.setGeometry(QtCore.QRect(1140, 230, 211, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Vert_Doc_Lang = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.Vert_Doc_Lang.setContentsMargins(0, 0, 0, 0)
        self.Vert_Doc_Lang.setObjectName("Vert_Doc_Lang")
        self.Doc_Lang_Label = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.Doc_Lang_Label.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(106, 186, 255)\n"
"")
        self.Doc_Lang_Label.setObjectName("Doc_Lang_Label")
        self.Vert_Doc_Lang.addWidget(self.Doc_Lang_Label)
        self.Doc_Lang_Select = QtWidgets.QComboBox(self.layoutWidget1)
        self.Doc_Lang_Select.setObjectName("Doc_Lang_Select")
        self.Doc_Lang_Select.addItem("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Hindi_Letter.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.Doc_Lang_Select.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("English_Letter.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.Doc_Lang_Select.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("French_Letter.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.Doc_Lang_Select.addItem(icon2, "")
        self.Doc_Lang_Select.addItem("")
        self.Doc_Lang_Select.setItemText(4, "")
        self.Vert_Doc_Lang.addWidget(self.Doc_Lang_Select)
        self.Upload_Button = QtWidgets.QPushButton(self.Central_Widget_OCR)
        self.Upload_Button.setGeometry(QtCore.QRect(30, 570, 171, 51))
        self.Upload_Button.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(59, 255, 49)\n"
"")
        self.Upload_Button.setObjectName("Upload_Button")
        self.layoutWidget2 = QtWidgets.QWidget(self.Central_Widget_OCR)
        self.layoutWidget2.setGeometry(QtCore.QRect(1140, 400, 211, 141))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.Vert_Trans_Lang = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.Vert_Trans_Lang.setContentsMargins(0, 0, 0, 0)
        self.Vert_Trans_Lang.setObjectName("Vert_Trans_Lang")
        self.Trans_Lang_Label = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.Trans_Lang_Label.setStyleSheet("font-size:35px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color:rgb(106, 186, 255)\n"
"")
        self.Trans_Lang_Label.setObjectName("Trans_Lang_Label")
        self.Vert_Trans_Lang.addWidget(self.Trans_Lang_Label)
        self.Trans_Lang_Select = QtWidgets.QComboBox(self.layoutWidget2)
        self.Trans_Lang_Select.setObjectName("Trans_Lang_Select")
        self.Trans_Lang_Select.addItem("")
        self.Trans_Lang_Select.addItem(icon, "")
        self.Trans_Lang_Select.addItem(icon1, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("French_Letter.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.Trans_Lang_Select.addItem(icon3, "")
        self.Vert_Trans_Lang.addWidget(self.Trans_Lang_Select)
        SMART_OCR.setCentralWidget(self.Central_Widget_OCR)
        self.menubar = QtWidgets.QMenuBar(SMART_OCR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1385, 21))
        self.menubar.setObjectName("menubar")
        SMART_OCR.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SMART_OCR)
        self.statusbar.setObjectName("statusbar")
        SMART_OCR.setStatusBar(self.statusbar)

        self.retranslateUi(SMART_OCR)
        QtCore.QMetaObject.connectSlotsByName(SMART_OCR)
        
        
        #--------------Button Click Event----------------------#
        self.Upload_Button.clicked.connect(self.Upload_Img)
        self.Convert_Button.clicked.connect(self.Convert_Text)

    def retranslateUi(self, SMART_OCR):
        _translate = QtCore.QCoreApplication.translate
        SMART_OCR.setWindowTitle(_translate("SMART_OCR", "MainWindow"))
        self.Input_Label.setHtml(_translate("SMART_OCR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:400; color:#0717ff;\">INPUT WINDOW</span></p></body></html>"))
        self.Output_Label.setHtml(_translate("SMART_OCR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#0717ff;\">OUTPUT WINDOW</span></p></body></html>"))
        self.Translator_Label.setHtml(_translate("SMART_OCR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#0717ff;\">TRANSLATOR WINDOW</span></p></body></html>"))
        self.Convert_Button.setText(_translate("SMART_OCR", "Convert"))
        self.Exit_Button.setText(_translate("SMART_OCR", "Exit"))
        self.Translator_Button.setText(_translate("SMART_OCR", "Translate"))
        self.Help_Button.setText(_translate("SMART_OCR", "Help"))
        self.Img_Filter_Label.setHtml(_translate("SMART_OCR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#0717ff;\">Image Filter</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:400; color:#0717ff;\">(To Improve Image Quality)</span></p></body></html>"))
        self.Skwe_Corr_Box.setText(_translate("SMART_OCR", "Skew Correction"))
        self.Blurr_Corr_Box.setText(_translate("SMART_OCR", "Remove Blurr"))
        self.No_Filter_Box.setText(_translate("SMART_OCR", "No Filter"))
        self.Thresh_Corr_Box.setText(_translate("SMART_OCR", "Thresholding"))
        self.Doc_Lang_Label.setHtml(_translate("SMART_OCR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#0717ff;\">SELECT </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#0717ff;\">DOCUMENT LANGAUGE</span></p></body></html>"))
        self.Doc_Lang_Select.setItemText(0, _translate("SMART_OCR", "SELECT LANGUAGE"))
        self.Doc_Lang_Select.setItemText(1, _translate("SMART_OCR", "Hindi"))
        self.Doc_Lang_Select.setItemText(2, _translate("SMART_OCR", "English"))
        self.Doc_Lang_Select.setItemText(3, _translate("SMART_OCR", "French"))
        self.Upload_Button.setText(_translate("SMART_OCR", "Upload"))
        self.Trans_Lang_Label.setHtml(_translate("SMART_OCR", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#0717ff;\">SELECT </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#0717ff;\">TRANSLATION LANGAUGE</span></p></body></html>"))
        self.Trans_Lang_Select.setItemText(0, _translate("SMART_OCR", "SELECT LANGUAGE"))
        self.Trans_Lang_Select.setItemText(1, _translate("SMART_OCR", "Hindi"))
        self.Trans_Lang_Select.setItemText(2, _translate("SMART_OCR", "English"))
        self.Trans_Lang_Select.setItemText(3, _translate("SMART_OCR", "French"))
    
    #----Upload Image and Display to Frame------#
    def Upload_Img(self):
        Doc_img = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.gif *.png)")
        Doc_img_Path = Doc_img[0]
        img = Image.open(Doc_img_Path)
        
        image = img.resize((391, 471), Image.ANTIALIAS)
        image.save("change.jpeg", 'jpeg', quality=96)
        pixmap = QPixmap("change.jpeg")
        self.Input_Window.setPixmap(pixmap)
    
    #------Extract Text From Image------------------#
    def Convert_Text(self):
        img = Image.open("change.jpeg")
        select_lang = self.Doc_Lang_Select.currentText()
        if select_lang == "English":
            prefer_lang = "eng"
        elif select_lang == "Hindi":
            prefer_lang = "hin"
        elif select_lang == "French":
            prefer_lang = "fra"
        text = pytesseract.image_to_string(img,lang=prefer_lang)
        self.Output_Window.setText(text)
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SMART_OCR = QtWidgets.QMainWindow()
    ui = Ui_SMART_OCR()
    ui.setupUi(SMART_OCR)
    SMART_OCR.show()
    sys.exit(app.exec_())

