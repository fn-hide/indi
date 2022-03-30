from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QPlainTextEdit, QTextEdit, QFormLayout, QGroupBox, QLabel


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(400, 500)
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
        
        self.resLabel = QLabel()
        self.resImage = QPixmap('img/negative.png')
        
        self.resImage = self.resImage.scaled(100, 100, Qt.KeepAspectRatio)
        
        self.resLabel.setPixmap(self.resImage)
        self.resLabel.setAlignment(Qt.AlignCenter)
        
        self._gnrLayout.addWidget(self.resLabel)
    
    def getSentence(self):
        return self.insent.toPlainText()
    

        
        
        
        
        
        