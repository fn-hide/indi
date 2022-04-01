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

# import pandas as pd
# # import os
# # os.listdir('c:/users/febri/projects/indi/assets/')
# df = pd.read_csv('D:/Backup/hello/dataset_myIndiHme.csv')

# negative = df.loc[df['star'] == 0]
# positive = df.loc[df['star'] == 1]

# df_new = pd.concat([negative.iloc[:5, :], positive.iloc[:5, :]])
# df_new = df_new.review
# df_new

# df_new.to_csv('c:/users/febri/projects/indi/assets/data2.csv', index=False)

# pd.read_csv('c:/users/febri/projects/indi/assets/data2.csv')
# pd.read_csv('c:/users/febri/projects/indi/assets/data.csv')

