#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import PyQt4 QtCore and QtGui modules
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor, QTextCursor
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableWidgetItem

import AuxiliaryMethods

color="red";

app = QApplication(sys.argv)

MainWindow = uic.loadUi('gui/mainform.ui')
SearchRes = uic.loadUi('gui/SearchResults.ui')
#TextAnalysisWindow = uic.loadUi('gui/TextAnalysisWindow.ui')
GraphsWidget = uic.loadUi('gui/graphs.ui')

#Методы нажатия соответствующих кнопок
def browseButton_click():
    analysisText = MainWindow.plainTextEdit_Main.toPlainText()
    words = AuxiliaryMethods.getWordsFromString(analysisText)
    print(words)
    print("_________")
    temp= AuxiliaryMethods.getCountWords(analysisText)
    #t = sorted( [(x,len(words[x])) for x in segnifikentWords] , key=lambda x: x[1], reverse=True)
    print(sorted(temp.items(),key=lambda x: x[1],reverse=True )[:10])

def ChooseFile(self):
    if MainWindow.radioButton.isChecked():
        try:
            filename = QFileDialog.getOpenFileName(None, 'Save File', os.getenv('HOME'),)[0]
            file = open(filename)
            data = file.read()
            # elif MainWindow.radioButton2.isChecked():

            # Clear previous selections
            clear()

            MainWindow.plainTextEdit_Main.setPlainText(data)
        except:pass




def Proceed():
    analysis = AuxiliaryMethods.analysisText(MainWindow.plainTextEdit_Main.toPlainText())
    table = MainWindow.tableWidget  # Создаём таблицу

    table.setColumnCount(2)  # Устанавливаем три колонки
    table.setRowCount(len(analysis))  # и одну строку в таблице

    # Устанавливаем заголовки таблицы
    table.setHorizontalHeaderLabels(["Параметры", "Значения"])

    # заполняем таблицу
    for i, item in enumerate(analysis):
        parametr = QTableWidgetItem(item[0])
        parametr.setFlags(Qt.ItemIsEditable)
        table.setItem(i, 0, parametr)

        value = QTableWidgetItem(str(item[1]))
        value.setFlags(Qt.ItemIsEditable)
        table.setItem(i, 1, value)
    table.resizeColumnsToContents()


def textAnalysisButton_click():
    analysis = AuxiliaryMethods.analysisText(MainWindow.plainTextEdit_Main.toPlainText())

    table = TextAnalysisWindow.tableWidget  # Создаём таблицу

    table.setColumnCount(2)  # Устанавливаем три колонки
    table.setRowCount(len(analysis))  # и одну строку в таблице

    # Устанавливаем заголовки таблицы
    table.setHorizontalHeaderLabels(["Параметры", "Значения"])

    # заполняем таблицу
    for i,item in enumerate(analysis):
        parametr = QTableWidgetItem(item[0])
        parametr.setFlags(Qt.ItemIsEditable)
        table.setItem(i, 0, parametr)

        value = QTableWidgetItem(str(item[1]))
        value.setFlags(Qt.ItemIsEditable)
        table.setItem(i, 1, value)

    # делаем ресайз колонок по содержимому
    table.resizeColumnsToContents()

    TextAnalysisWindow.show()

def clear():
    cursor = MainWindow.plainTextEdit_Main.textCursor()
    cursor.select(QTextCursor.Document)
    cursor.setCharFormat(QTextCharFormat())
    cursor.clearSelection()
    MainWindow.plainTextEdit_Main.setTextCursor(cursor)

def Search():
    data = SearchRes.plainTextEdit
    analysisText = MainWindow.plainTextEdit_Main.toPlainText()
    searchText = MainWindow.lineEdit_SearchWords.text()
    searchWords = AuxiliaryMethods.getWordsFromString(searchText)
    if len(searchWords) < 1: return

    # Все слова текста
    words = AuxiliaryMethods.getWordsFromString(analysisText)

    # Найденные слова
    detectedWords = {k: words[k] for k in searchWords.keys() if k in words.keys()}

    print(detectedWords)
    #SearchRes.plainTextEdit.setPlainText("");
    SearchRes.plainTextEdit.appendPlainText("______________RESULTS________________")
    SearchRes.plainTextEdit.appendPlainText(str(detectedWords))
    SearchRes.plainTextEdit.appendPlainText("**********************************************")

    #Стираем результаты предыдущего выделения
    clear()

    cursor = MainWindow.plainTextEdit_Main.textCursor()

    format = QTextCharFormat()
    format.setBackground(QBrush(QColor("yellow")))


    searchWordsList = AuxiliaryMethods.getWordsFromString2(MainWindow.lineEdit_SearchWords.text())
    pattern=""
    print("SEARCHWORLDLIST: ")
    print(searchWordsList)

    for w in searchWordsList[0:-1]:
        pattern +=w+"|"
    pattern+=searchWordsList[-1]

    #pattern = "We|you|enough"
    print("PATTERN: ")
    print(pattern)
    regex = QRegExp(pattern)
    # Обработка выбранного документа
    pos = 0
    index = regex.indexIn(MainWindow.plainTextEdit_Main.toPlainText(), pos)
    print("INDEX_" + index.__str__())
    while (index != -1):

        # Бираем совпадающий текст и применяем к нему format
        cursor.setPosition(index)
        cursor.movePosition(QTextCursor.EndOfWord, 1)
        cursor.mergeCharFormat(format)

        #передвигает курсор на позицию следующего совпадение
        pos = index + regex.matchedLength()
        index = regex.indexIn(MainWindow.plainTextEdit_Main.toPlainText(), pos)
    MainWindow.plainTextEdit_Main.moveCursor(QTextCursor.Start)
    SearchRes.show()


def ClearRes():
    SearchRes.plainTextEdit.clear()

def SaveSearchToFile():
    try:
        filename = QFileDialog.getSaveFileName(None, 'Save File')[0]
        file = open(filename,'w')
        file.write(SearchRes.plainTextEdit.toPlainText())
        file.close()
    except:pass

def searchButton_click():
    analysisText = MainWindow.plainTextEdit_Main.toPlainText()
    searchText = MainWindow.lineEdit_SearchWords.text()
    stopText = MainWindow.lineEdit_StopWords.text()
    print(stopText)

    #Слова которые ищут
    searchWords = AuxiliaryMethods.getWordsFromString(searchText)
    if len(searchWords)<1: return

    #Все слова текста
    words = AuxiliaryMethods.getWordsFromString(analysisText)

    #Стоп слова
    #print()

    #Найденные слова
    detectedWords = {k:words[k] for k in searchWords.keys() if k in words.keys() }
    print(detectedWords)


def Graphs():
    analysisText = MainWindow.plainTextEdit_Main.toPlainText()
    stopText = MainWindow.lineEdit_StopWords.text()
    words = AuxiliaryMethods.getWordsFromString(analysisText)
    stopWords = AuxiliaryMethods.getWordsFromString(stopText)
    morphWords = AuxiliaryMethods.getMorphWords(words)
    segnifikentWords = list(set(morphWords[0])-set(stopWords.keys()))

    stopWordsFromStats = AuxiliaryMethods.getCountWords(stopText)
    temp = AuxiliaryMethods.getCountWords(analysisText)

    finalwords={k:v for k,v in temp.items() if k not in stopWordsFromStats.keys()}
    print("FINALWORDS")
    print(finalwords.items())

    print(sorted(finalwords.items(), key=lambda x: x[1], reverse=True)[:10])
    t=sorted(finalwords.items(), key=lambda x: x[1], reverse=True)
    tmp = t[:10]

    plt.figure(1)


    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    def f(t):
        return np.exp(-t) * np.cos(2 * np.pi * t)

    plt.figure(1)
    plt.subplot(211)
    plt.bar(range(len(tmp)), [x[1] for x in tmp], width=0.1, tick_label=[x[0] for x in tmp])
    plt.title("Top 10 words")
    plt.grid(True)

    plt.subplot(212)
    plt.pie([x[1] for x in tmp], labels=[x[0] for x in tmp], autopct='%1.1f%%')

    plt.show()


    plt.show()


#Подключение методов к элементам
MainWindow.pickFileButt.clicked.connect(ChooseFile)
MainWindow.pushButton_Proceed.clicked.connect(Proceed)
MainWindow.pushButton_SearchButt.clicked.connect(Search)
SearchRes.pushButton.clicked.connect(SaveSearchToFile)
SearchRes.pushButton_2.clicked.connect(ClearRes)
MainWindow.pushButton_Stats.clicked.connect(Graphs)
MainWindow.pushButton_PickFileButt2.clicked.connect(browseButton_click)


#Показ главного окна и старт приложения.
MainWindow.show()
sys.exit(app.exec_())
