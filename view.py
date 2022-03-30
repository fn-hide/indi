from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QPlainTextEdit, QTextEdit, QFormLayout, QGroupBox, QLabel


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(400, 900)
        self.setWindowTitle('Sentiment Classifier')
        self.setStyleSheet('''
                           background-color: #0d0d0d;
                           color: #ffffff;
                           font: 14px "Raleway Light";
                           ''')
        
        self._gnrLayout = QVBoxLayout()
        self._cntWidget = QWidget()
        
        self.setCentralWidget(self._cntWidget)
        
        self._cntWidget.setLayout(self._gnrLayout)
        
        self._createWidget()
    
    def _createWidget(self):
        # input sentiment sentence
        self.insent = QPlainTextEdit()
        self.insent.setFixedHeight(150)
        
        self._gnrLayout.addWidget(self.insent)
        
        self.insent.setStyleSheet('''
                                  QPlainTextEdit{
                                      background-color: #fff;
                                      color: #000;
                                      border-radius: 10px;
                                  }
                                  ''')
        
        # predict button
        self.predictButton = QPushButton('Classify')
        self.predictButton.setFixedHeight(40)
        
        self._gnrLayout.addWidget(self.predictButton)
        
        self.predictButton.setStyleSheet('''
                                         QPushButton:hover{
                                             background-color: #5f5f5f;
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
                                            border-radius: 10px;
                                        }
                                        ''')
        
        # tf-idf view
        self.tfidfLabel = QLabel('TF-IDF')
        self.tfidfDisplay = QPlainTextEdit()
        self.tfidfLabel.setFixedHeight(30)
        self.tfidfLabel.setAlignment(Qt.AlignBottom)
        self.tfidfDisplay.setFixedHeight(80)
        self.tfidfDisplay.setReadOnly(True)
        
        self._gnrLayout.addWidget(self.tfidfLabel)
        self._gnrLayout.addWidget(self.tfidfDisplay)
        
        self.tfidfDisplay.setStyleSheet('''
                                        QPlainTextEdit{
                                            background-color: #fff;
                                            color: #000;
                                            border-radius: 10px;
                                        }
                                        ''')
        
        # pca view
        self.pcaLabel = QLabel('PCA')
        self.pcaDisplay = QPlainTextEdit()
        self.pcaLabel.setFixedHeight(30)
        self.pcaLabel.setAlignment(Qt.AlignBottom)
        self.pcaDisplay.setFixedHeight(80)
        self.pcaDisplay.setReadOnly(True)
        
        self._gnrLayout.addWidget(self.pcaLabel)
        self._gnrLayout.addWidget(self.pcaDisplay)
        
        self.pcaDisplay.setStyleSheet('''
                                    QPlainTextEdit{
                                        background-color: #fff;
                                        color: #000;
                                        border-radius: 10px;
                                    }
                                    ''')
        
        # classified view
        self.classifiedLabel = QLabel('Your sentence classified as:')
        self.classifiedLabel.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.classifiedLabel.setFixedHeight(50)
        
        self._gnrLayout.addWidget(self.classifiedLabel)
        
        self.resLabel = QLabel()
        self.resImage = QPixmap('img/negative.png')
        
        self.resImage = self.resImage.scaled(200, 200, Qt.KeepAspectRatio)
        
        self.resLabel.setPixmap(self.resImage)
        self.resLabel.setAlignment(Qt.AlignCenter)
        
        self._gnrLayout.addWidget(self.resLabel)
    
    def getSentence(self):
        return self.insent.toPlainText()
    

        
        
        
        
        
        