import numpy as np
from catboost import  CatBoostClassifier
from xgboost import  XGBClassifier
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from joblib import load

class model_C19:
    @staticmethod
    def scaler(X):
        return X/100
    @staticmethod
    def CatBoost(X):
        classifier = CatBoostClassifier()
        classifier.load_model('COVID19/C19_cb',format = 'cbm')
        X[0] = model_C19.scaler(X[0])
        X[1] = model_C19.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def K_NN(X):
        classifier = KNeighborsClassifier()
        classifier = load('COVID19/C19_knn.joblib')
        X[0] = model_C19.scaler(X[0])
        X[1] = model_C19.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def DecisionT(X):
        classifier = DecisionTreeClassifier()
        classifier = load('COVID19/C19_dt.joblib')
        X[0] = model_C19.scaler(X[0])
        X[1] = model_C19.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def RandomForest(X):
        classifier = RandomForestClassifier()
        classifier = load('COVID19/C19_rf.joblib')
        X[0] = model_C19.scaler(X[0])
        X[1] = model_C19.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticReg(X):
        classifier = LogisticRegression()
        classifier = load('COVID19/C19_lr.joblib')
        X[0] = model_C19.scaler(X[0])
        X[1] = model_C19.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticRegCV(X):
        classifier = LogisticRegressionCV()
        classifier = load('COVID19/C19_lrcv.joblib')
        X[0] = model_C19.scaler(X[0])
        X[1] = model_C19.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def Xgboost(X):
        classifier = XGBClassifier()
        classifier.load_model('COVID19/C19_xgb')
        X[0] = model_C19.scaler(X[0])
        X[1] = model_C19.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def select(X):
        cb = X.copy()
        knn = X.copy()
        lr = X.copy()
        lrcv = X.copy()
        rf = X.copy()
        dt = X.copy()
        xgb = X.copy()
        
        mod = [model_C19.CatBoost(cb), 
               model_C19.K_NN(knn),  
               model_C19.RandomForest(rf),
               model_C19.LogisticReg(lr),
               model_C19.LogisticRegCV(lrcv), 
               model_C19.Xgboost(xgb),
               model_C19.DecisionT(dt)]
        return mod
        