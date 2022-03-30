from functools import partial

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        
        self.conSignals()
    
    def conSignals(self):
        self._view.predictButton.clicked.connect(partial(self._clfSentence))
    
    def _clfSentence(self):
        data = self._view.getSentence()
        result = self._model.classify(data)[0]
        self._view.insent.setPlainText(str(result))
        
        
        
        