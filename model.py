import pickle
import numpy as np


class Model:
    def __init__(self):
        self._classifier = pickle.load(open('model/indihome_model.pkl', 'rb'))
        self._extractor = pickle.load(open('model/indihome_tfidf.pkl', 'rb'))
        self._reductor = pickle.load(open('model/indihome_pca.pkl', 'rb'))
        # self._classifier = None
        # self._extractor = None
        # self._reductor = None
    
    def classify(self, data):
        return self._classifier.predict(
            self._reductor.transform(
                self._extractor.transform(
                    np.array([data])
                ).todense()
            )
        )
        
        
        