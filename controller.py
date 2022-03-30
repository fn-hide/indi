from functools import partial

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        
        self.conSignals()
    
    def conSignals(self):
        self._view.predictButton.clicked.connect(self._clfSentence)
    
    def _clfSentence(self):
        
        print('self._view.insent.toPlainText()')
        self._view.cleanDisplay.setPlainText('bangsad')
        # data = self._view.getSentence()
        # result = self._model.classify(data)
        
        # self._view.tfidfDisplay.setPlainText(self._model.extracted)
        # self._view.pcaDisplay.setPlainText(self._model.reducted)
        
        # self._view.insent.setPlainText(result)
        

        
        
        