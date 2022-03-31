import sys

from PyQt5.QtWidgets import QApplication
from controller import Controller
from view import View
from model import Model


app = QApplication(sys.argv)

view = View()
view.show()

model = Model()

Controller(model, view)

sys.exit(app.exec_())

# import pickle
# import numpy as np

# loaded_extractor = pickle.load(open('model/indihome_tfidf.pkl', 'rb'))
# tes = loaded_extractor.transform(np.array(['Aku oragn YAng tidak .pergi DEngag 0123 rang lain.']))
# print(tes.shape)
# print(tes.todense())


import pandas as pd

pd.read_csv('assets/data.csv').shape

