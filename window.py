from styles import STYLES
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
        self.setStyleSheet(
            STYLES['main']
        )
        
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
        
        self.flButton.setStyleSheet(
            STYLES['button']
        )

        # wordcloud table
        self.wcTable = QTableWidget()
        self.wcTable.setColumnCount(2)
        self.wcTable.verticalHeader().setVisible(False)
        self.wcTable.horizontalHeader().sectionResized.connect(self.wcTable.resizeRowsToContents)
        self.wcTable.setStyleSheet(
            '''
            QScrollBar{
                background-color: #F7F5F2;
            }
            QScrollBar:handle{
                background-color: #313552;
            }
            QScrollBar::handle::pressed{
                background-color: #151D3B;
            }
            '''
        )
        
        item1 = QTableWidgetItem('Classified as')
        item1.setBackground(QtGui.QColor('#F7F5F2'))
        item1.setForeground(QtGui.QColor('#151D3B'))
        self.wcTable.setHorizontalHeaderItem(0, item1)
        
        item2 = QTableWidgetItem('Sentiment')
        item2.setBackground(QtGui.QColor('#F7F5F2'))
        item2.setForeground(QtGui.QColor('#151D3B'))
        self.wcTable.setHorizontalHeaderItem(1, item2)
        
        # self.wcTable.setHorizontalHeaderLabels(['Classified as', 'Sentiment'])
        self.wcTable.setShowGrid(False)
        self.wcTable.horizontalHeader().setStretchLastSection(True)
        
        self._ndLayout.addWidget(self.wcTable)
        
        # wordcloud button
        self.wcButton = QPushButton('Generate Wordcloud')
        self.wcButton.setFixedHeight(40)
        
        self._ndLayout.addWidget(self.wcButton)
        
        self.wcButton.setStyleSheet(
            STYLES['button']
        )
        
        # wordcloud display
        self.wcLabel = QLabel('WordCloud')
        self.wcLabel.setFixedSize(350, 350)
        self.wcLabel.setAlignment(Qt.AlignCenter)

        self._fsLayout.addWidget(self.wcLabel)
        
        self.wcLabel.setStyleSheet(
            STYLES['main']
        )
        
        
        