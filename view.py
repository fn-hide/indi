from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QPushButton, 
    QVBoxLayout, 
    QPlainTextEdit, 
    QLabel,
    )
from functools import partial

from window import Window

        
class View(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(400, 600)
        self.setWindowTitle('Sentiment Classifier')
        self.setStyleSheet('''
                           background-color: #0d0d0d;
                           color: #ffffff;
                           font: 11px "Raleway";
                           ''')
        
        self._gnrLayout = QVBoxLayout()
        self._cntWidget = QWidget()
        
        self.setCentralWidget(self._cntWidget)
        
        self._cntWidget.setLayout(self._gnrLayout)
        
        self._createWidget()
        
        self._window = Window()
    
    def _createWidget(self):
        # input sentiment sentence
        self.insent = QPlainTextEdit()
        self.insent.setFixedHeight(80)
        
        self._gnrLayout.addWidget(self.insent)
        
        self.insent.setStyleSheet('''
                                  QPlainTextEdit{
                                      background-color: #fff;
                                      color: #000;
                                      border-radius: 5px;
                                  }
                                  ''')
        
        # predict button
        self.predictButton = QPushButton('Classify')
        self.predictButton.setFixedHeight(40)
        
        self._gnrLayout.addWidget(self.predictButton)
        
        self.predictButton.setStyleSheet('''
                                         QPushButton{
                                             background-color: #0d0d0d;
                                             border: 0px;
                                         }
                                         QPushButton:hover{
                                             background-color: #3f3f3f;
                                             border: 0px;
                                             border-radius: 20px;
                                         }
                                         ''')
        
        # preprocessing view
        self.cleanLabel = QLabel('Preprocessing')
        self.cleanDisplay = QPlainTextEdit()
        self.cleanLabel.setFixedHeight(30)
        self.cleanLabel.setAlignment(Qt.AlignBottom)
        self.cleanDisplay.setFixedHeight(80)
        self.cleanDisplay.setReadOnly(True)
        
        self._gnrLayout.addWidget(self.cleanLabel)
        self._gnrLayout.addWidget(self.cleanDisplay)
        
        self.cleanDisplay.setStyleSheet('''
                                        QPlainTextEdit{
                                            background-color: #fff;
                                            color: #000;
                                            border-radius: 5px;
                                        }
                                        ''')
        
        # classified view
        self.classifiedLabel = QLabel('Your sentence classified as:')
        self.classifiedLabel.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.classifiedLabel.setFixedHeight(30)
        
        self._gnrLayout.addWidget(self.classifiedLabel)
        
        # positive label
        self.pstLabel = QLabel()
        self.pstImage = QPixmap('img/positive.png')
        
        self.pstImage = self.pstImage.scaled(100, 100, Qt.KeepAspectRatio)
        
        self.pstLabel.setPixmap(self.pstImage)
        self.pstLabel.setAlignment(Qt.AlignCenter)
        self.pstLabel.setFixedHeight(0)
        
        self._gnrLayout.addWidget(self.pstLabel)
        
        # negative label
        self.ngtLabel = QLabel()
        self.ngtImage = QPixmap('img/negative.png')
        
        self.ngtImage = self.ngtImage.scaled(100, 100, Qt.KeepAspectRatio)
        
        self.ngtLabel.setPixmap(self.ngtImage)
        self.ngtLabel.setAlignment(Qt.AlignCenter)
        self.ngtLabel.setFixedHeight(0)
        
        self._gnrLayout.addWidget(self.ngtLabel)
        
        # blank label
        self.blkLabel = QLabel()
        self.blkImage = QPixmap('img/blank.png')
        
        self.blkImage = self.blkImage.scaled(100, 100, Qt.KeepAspectRatio)
        
        self.blkLabel.setPixmap(self.blkImage)
        self.blkLabel.setAlignment(Qt.AlignCenter)
        self.blkLabel.setFixedHeight(100)
        
        self._gnrLayout.addWidget(self.blkLabel)
        
        # another window
        self.windowButton = QPushButton('Need wordcloud?')
        self.windowButton.setFixedHeight(40)
        
        self._gnrLayout.addWidget(self.windowButton)
        
        self.windowButton.setStyleSheet('''
                                        QPushButton{
                                             background-color: #0d0d0d;
                                             border: 0px;
                                         }
                                         QPushButton:hover{
                                             background-color: #3f3f3f;
                                             border: 0px;
                                             border-radius: 20px;
                                         }
                                        ''')
    
    def getSentence(self):
        return self.insent.toPlainText()
    

        
        
        
        
        
        