import pickle



class Model:
    def __init__(self):
        self._classifier = pickle.load(open('model/indihome_model.pkl', 'rb'))
        self._extractor = pickle.load(open('model/indihome_tfidf.pkl', 'rb'))
        self._reductor = pickle.load(open('model/indihome_pca.pkl', 'rb'))
    
    def extract(self, data):
        self.data = data
        return self._extractor.transform(self.data)
    
    def reduct(self, data):
        self.extracted = self.extract(data).todense()
        return self._reductor.transform(self.extracted)
    
    def classify(self, data):
        self.reducted = self.reduct(data)
        return self._classifier(self.reducted)
        
        
        