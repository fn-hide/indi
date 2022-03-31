from PyQt5.QtCore import Qt
from functools import partial
import numpy as np

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        
        self.conSignals()
    
    def conSignals(self):
        self._view.predictButton.clicked.connect(partial(self._clfSentence))
    
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
        
        
        