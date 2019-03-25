import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from controller import Controller

uipath = 'main.ui'

class AntiplagiatView(QDialog):
    ## @brief         Конструктор класса формы.
    #
    #
    # @param		            Отсутствуют.
    #
    # @return
    # @return		            Отсутствуют.
    #

    def __init__(self):
        super(AntiplagiatView,self).__init__()
        loadUi(uipath, self)
        self.pushButtonCompare.clicked.connect(self.pushButtonCompareHandler)
        self.pushButtonAdd.clicked.connect(self.pushButtonAddHandler)

    ## @brief         Функция обработки нажатий на клавишу "Сравнить".
    #
    #
    # @param		            Отсутствуют.
    #
    # @return
    # @return		            Отсутствуют.
    #

    @pyqtSlot()
    def pushButtonCompareHandler(self):
        if not (self.textEditIn.toPlainText() is ''):
            self.textEditOut.clear()
            self.textEditResInfo.clear()
            contrl = Controller()
            name, text, shingl, levesh = contrl.comp(self.textEditIn.toPlainText())
            if name is '':
                self.textEditOut.setPlainText(text)
            else:
                self.textEditResInfo.setPlainText('Название найденного текста {0}\nСтепень схожести по алгоритму шинглов = {1}\nРасстояние Левенштейна = {2}\n'.format(name, shingl, levesh))
                self.textEditOut.setPlainText(text)

    ## @brief         Функция обработки нажатий на клавишу "Добавить в БД".
    #
    #
    # @param		            Отсутствуют.
    #
    # @return
    # @return		            Отсутствуют.
    #

    @pyqtSlot()
    def pushButtonAddHandler(self):
        if not (self.textEditIn.toPlainText() is ''):
            contrl = Controller()
            res = contrl.add(self.textEditIn.toPlainText())
            self.textEditIn.clear()
            self.textEditIn.setPlainText(str(res))

app = QApplication(sys.argv)
form=AntiplagiatView()
form.show()
sys.exit(app.exec_())
