from functools import partial

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        
        self.conSignals()
    
    def conSignals(self):
        self._view.predictButton.clicked.connect(partial(self.setPreprocessingDisplay, 'bangsad'))
    
    def setPreprocessingDisplay(self, txt):
        self._view.cleanDisplay.setPlainText(txt)
        self._view.cleanDisplay.setFocus()