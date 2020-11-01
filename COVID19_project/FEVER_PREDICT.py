import numpy as np
from catboost import  CatBoostClassifier
from xgboost import  XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier
from joblib import load

class model_F:
    @staticmethod
    def scaler(X):
        return X/100
    @staticmethod
    def CatBoost(X):
        classifier = CatBoostClassifier()
        classifier.load_model('FEVER/F_cb',format = 'cbm')
        X[0] = model_F.scaler(X[0])
        X[1] = model_F.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticReg(X):
        classifier = LogisticRegression()
        classifier = load('FEVER/F_lr.joblib')
        X[0] = model_F.scaler(X[0])
        X[1] = model_F.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def RandomForest(X):
        classifier = RandomForestClassifier()
        classifier = load('FEVER/F_rf.joblib')
        X[0] = model_F.scaler(X[0])
        X[1] = model_F.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def Xgboost(X):
        classifier = XGBClassifier()
        classifier.load_model('FEVER/F_xgb')
        X[0] = model_F.scaler(X[0])
        X[1] = model_F.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def DecisionT(X):
        classifier = DecisionTreeClassifier()
        classifier = load('FEVER/F_dt.joblib')
        X[0] = model_F.scaler(X[0])
        X[1] = model_F.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def select(X):
        cb = X.copy()
        lr = X.copy()
        rf = X.copy()
        dt = X.copy()
        xgb = X.copy()
        
        mod = [model_F.CatBoost(cb), 
               model_F.LogisticReg(lr), 
               model_F.RandomForest(rf), 
               model_F.Xgboost(xgb),
               model_F.DecisionT(dt)]
        return mod
        