from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle

class_train_model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
method_train_model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)

class_dataset = pd.read_csv('quasar/algorithm/dataset/Python_LargeClassSmell_Dataset.csv', sep=',')
method_dataset = pd.read_csv('quasar/algorithm/dataset/Python_LongMethodSmell_Dataset.csv', sep=',')

# TODO: Rewrite this function to be more generic
def train():
    X_class = class_dataset.iloc[:, :-1].values
    y_class = class_dataset.iloc[:, -1].values

    class_train_model.fit(X_class, y_class)
    pickle.dump(class_train_model, open('quasar/algorithm/model/class_model.sav', 'wb'))

    X_method = method_dataset.iloc[:, :-1].values
    y_method = method_dataset.iloc[:, -1].values

    method_train_model.fit(X_method, y_method)
    pickle.dump(method_train_model, open('quasar/algorithm/model/method_model.sav', 'wb'))


if __name__ == "__main__":
    train()
    