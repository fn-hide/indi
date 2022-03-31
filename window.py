from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(800, 400)
        self.setWindowTitle('Wordcloud')
        # self.setStyleSheet('''
        #                    background-color: #0d0d0d;
        #                    color: #ffffff;
        #                    font: 11px "Raleway";
        #                    ''')
        
        # first layout
        self._fsLayout = QHBoxLayout()
        self.setLayout(self._fsLayout)
        
        # second layout        
        self._ndLayout = QVBoxLayout()
        self._ndLayout.setAlignment(Qt.AlignTop)
        self._fsLayout.addLayout(self._ndLayout)
        
        self._createWidgets()
    
    def _createWidgets(self):        
        # file button
        self.flButton = QPushButton('Choose File')
        self.flButton.setFixedHeight(40)
        
        self._ndLayout.addWidget(self.flButton)
        
        # self.flButton.setStyleSheet('''
        #                             QPushButton{
        #                                     background-color: #0d0d0d;
        #                                     border: 0px;
        #                             }
        #                             QPushButton:hover{
        #                                     background-color: #3f3f3f;
        #                                     border: 0px;
        #                                     border-radius: 20px;
        #                             }
        #                              ''')

        # wordcloud table
        self.wcTable = QTableWidget()
        self.wcTable.setColumnCount(2)
        
        item1 = QTableWidgetItem('Classified as')
        self.wcTable.setHorizontalHeaderItem(0, item1)
        
        item2 = QTableWidgetItem('Sentiment')
        self.wcTable.setHorizontalHeaderItem(1, item2)
        
        # self.wcTable.setHorizontalHeaderLabels(['Classified as', 'Sentiment'])
        self.wcTable.setShowGrid(False)
        self.wcTable.horizontalHeader().setStretchLastSection(True)
        
        self._ndLayout.addWidget(self.wcTable)
        
        # wordcloud button
        self.wcButton = QPushButton('Generate Wordcloud')
        self.wcButton.setFixedHeight(40)
        
        self._ndLayout.addWidget(self.wcButton)
        
        # self.wcButton.setStyleSheet('''
        #                             QPushButton{
        #                                     background-color: #0d0d0d;
        #                                     border: 0px;
        #                             }
        #                             QPushButton:hover{
        #                                     background-color: #3f3f3f;
        #                                     border: 0px;
        #                                     border-radius: 20px;
        #                             }
        #                              ''')
        
        # wordcloud display
        self.wcLabel = QLabel()
        self.wcLabel.setFixedSize(350, 350)

        self._fsLayout.addWidget(self.wcLabel)
        
        # self.wcLabel.setStyleSheet('''
        #                             background-color: #fff;
        #                             border-radius: 20px;
        #                             ''')
        
        
        