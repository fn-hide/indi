import pandas as pd

from wordcloud import WordCloud 
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QFileDialog,
    QTableWidgetItem,
    QLabel
)

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        
        self.conSignals()
    
    def conSignals(self):
        self._view.predictButton.clicked.connect(partial(self._clfSentence))
        self._view.windowButton.clicked.connect(partial(self._view._window.show))
        self._view._window.flButton.clicked.connect(partial(self._openFile))
        self._view._window.wcButton.clicked.connect(partial(self._wordCloud))
    
    def _wordCloud(self):
        pos_comment = ' '
        for sentence in self._model.df_pre:
            pos_comment += str(sentence) + ' '
        print(pos_comment)

        wordcloud = WordCloud(width = 350, height = 350,
                        background_color ='white',
                        # stopwords = stopwords,
                        min_font_size = 10).generate(pos_comment)

        filename = 'assets/wordcloud.png'
        wordcloud.to_file(filename)
        
        # wordcloud display
        self._view._window.wcImage = QPixmap(filename)
        self._view._window.wcImage = self._view._window.wcImage.scaled(350, 350, Qt.KeepAspectRatio)
        self._view._window.wcLabel.setPixmap(self._view._window.wcImage)
                
    def _openFile(self):
        filepath, _ = QFileDialog.getOpenFileName(self._view._window, 
                                               "QFileDialog.getOpenFileName()", 
                                               "",
                                               "All Files (*);;Python Files (*.py)")
        df = pd.read_csv(filepath).values
        
        # preprocessing result
        self._model.df_pre = [self._model.preprocessing(i[0]) for i in df]
        for i in self._model.df_pre:
            print(' '.join(i))

        # classifying result
        self._model.df_res = [self._model.classify(i)[0] for i in self._model.df_pre]
        print(self._model.df_res)
        
        # insert into table
        self._view._window.wcTable.setRowCount(len(self._model.df_pre))
        for i in range(len(self._model.df_pre)):
            res = 'positive' if self._model.df_res[i] == 1 else 'negative'
            clsItem = QTableWidgetItem(res)
            clsItem.setTextAlignment(Qt.AlignHCenter)
            
            self._view._window.wcTable.setItem(i, 0, clsItem)
            self._view._window.wcTable.setItem(i, 1, QTableWidgetItem(' '.join(self._model.df_pre[i])))
    
    def _clfSentence(self):
        data = self._view.getSentence()
        preprocessed = self._model.preprocessing(data)
        result = self._model.classify(preprocessed)[0]
        self._view.insent.setPlainText(str(result))
        self._view.cleanDisplay.setPlainText(' '.join(preprocessed))
        
        self._view.blkLabel.setFixedHeight(0)
        if result:
            self._view.pstLabel.setFixedHeight(100)
            self._view.ngtLabel.setFixedHeight(0)
            self._view.classifiedLabel.setText('Your sentence classified as: <strong>Positive</strong> sentence.')
        else:
            self._view.ngtLabel.setFixedHeight(100)
            self._view.pstLabel.setFixedHeight(0)
            self._view.classifiedLabel.setText('Your sentence classified as: <strong>Negative</strong> sentence.')
        
        
        