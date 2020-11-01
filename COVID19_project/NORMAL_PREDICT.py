import numpy as np
from joblib import load
from catboost import  CatBoostClassifier
from xgboost import  XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


class model_N:
    @staticmethod
    def scaler(X):
        return X/100

    @staticmethod
    def CatBoost(X):
        classifier = CatBoostClassifier()
        classifier.load_model('NORMAL/N_cb',format = 'cbm')
        X[0] = model_N.scaler(X[0])
        X[1] = model_N.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticReg(X):
        classifier = LogisticRegression()
        classifier = load('NORMAL/N_lr.joblib')
        X[0] = model_N.scaler(X[0])
        X[1] = model_N.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def RandomForest(X):
        classifier = RandomForestClassifier()
        classifier = load('NORMAL/N_rf.joblib')
        X[0] = model_N.scaler(X[0])
        X[1] = model_N.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def Xgboost(X):
        classifier = XGBClassifier()
        classifier.load_model('NORMAL/N_xgb')
        X[0] = model_N.scaler(X[0])
        X[1] = model_N.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def DecisionT(X):
        classifier = DecisionTreeClassifier()
        classifier = load('NORMAL/N_dt.joblib')
        X[0] = model_N.scaler(X[0])
        X[1] = model_N.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def select(X):
        cb = X.copy()
        dt = X.copy()
        lr = X.copy()
        rf = X.copy()
        xgb = X.copy()
        
        mod = [model_N.CatBoost(cb), 
               model_N.LogisticReg(lr), 
               model_N.RandomForest(rf), 
               model_N.Xgboost(xgb),
               model_N.DecisionT(dt)]
        return mod
