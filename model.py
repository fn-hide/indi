import re
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from string import punctuation
from correction_functions import correction


class Model:
    def __init__(self):
        # load tfidf, pca, and svm models
        self._classifier = pickle.load(open('model/indihome_model.pkl', 'rb'))
        self._extractor = pickle.load(open('model/indihome_tfidf.pkl', 'rb'))
        self._reductor = pickle.load(open('model/indihome_pca.pkl', 'rb'))
        
        # configuring stopwords
        self._sw_indo = list(punctuation)
        self._sw_indo = self._sw_indo + stopwords.words('indonesian')
        self._sw_indo = self._sw_indo + [i for i in StopWordRemoverFactory().get_stop_words() if i not in self._sw_indo]
        print(len(self._sw_indo))
    
    def preprocessing(self, data):
        return self.stemmer_changer(        # 6. stemming
            self.stopword_changer(          # 5. stopword removing
                self.spell_changer(         # 4. word correcting
                    self.slang_changer(     # 3. slang changing
                        word_tokenize(      # 2. tokenize
                            self.cleaner(   # 1. cleaner
                                data
                            )
                        )
                    )
                )
            )
        )
        
    def classify(self, data):
        return self._classifier.predict(
            self._reductor.transform(
                self._extractor.transform(
                    data
                ).todense()
            )
        )
    
    def cleaner(self, sentence):
        review = sentence.lower()
        # clear double letters
        review = re.compile(r"(.)\1{1,}").sub(r"\1", review )
        # clear @username
        review = re.sub('@[^\s]+', '', review )
        # clear #tag
        review = re.sub(r'#([^\s]+)', '', review )
        # clear non-ascii value
        review = re.sub(r'[^\x00-\x7f]', r'', review )
        review = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', review )
        review = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", review )
        review = re.sub(r'\\u\w\w\w\w', '', review )
        # remove symbol, number, and strange char
        review = re.sub(r"[.,:;+!\-_<^/=?\"'\(\)\d\*]", " ", review )
        
        return review

    def slang_changer(self, review):
        kamus_slangword = eval(open("assets/slangwords.txt").read())
        # search pola kata (contoh kpn -> kapan)
        pattern = re.compile(r'\b( ' + '|'.join(kamus_slangword.keys()) + r')\b') 
        content = []
        for kata in review:
            # replace slangword berdasarkan pola review yg telah ditentukan
            filteredSlang = pattern.sub(lambda x: kamus_slangword[x.group()], kata) 
            content.append(filteredSlang.lower())
        
        return content
    
    def spell_changer(self, sentence):
        return [correction(i) for i in sentence]

    def stopword_changer(self, sentence):
        return [i for i in sentence if i not in self._sw_indo]

    def stemmer_changer(self, sentence):
        return [StemmerFactory().create_stemmer().stem(i) for i in sentence]
