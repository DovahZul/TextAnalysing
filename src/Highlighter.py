from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTextEdit


class MyHighlighter(QTextEdit):
    def __init__(self, parent=None):
        super(MyHighlighter, self).__init__(parent)
        # Setup the text editor
        text = """In this text I want to highlight this word and only this word.\n""" +\
        """Any other word shouldn't be highlighted"""
        self.setText(text)
        cursor = self.textCursor()
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        # Setup the regex engine
        pattern = "word"
        regex = QtCore.QRegExp(pattern)
        # Process the displayed document
        pos = 0
        index = regex.indexIn(self.toPlainText(), pos)
        while (index != -1):
            # Select the matched text and apply the desired format
            cursor.setPosition(index)
            cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
            cursor.mergeCharFormat(format)
            # Move to the next match
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.toPlainText(), pos)
