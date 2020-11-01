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

class model_C:
    @staticmethod
    def scaler(X):
        return X/100
    @staticmethod
    def CatBoost(X):
        classifier = CatBoostClassifier()
        classifier.load_model('COLD/C_cb',format = 'cbm')
        X[0] = model_C.scaler(X[0])
        X[1] = model_C.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def K_NN(X):
        classifier = KNeighborsClassifier()
        classifier = load('COLD/C_knn.joblib')
        X[0] = model_C.scaler(X[0])
        X[1] = model_C.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticReg(X):
        classifier = LogisticRegression()
        classifier = load('COLD/C_lr.joblib')
        X[0] = model_C.scaler(X[0])
        X[1] = model_C.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticRegCV(X):
        classifier = LogisticRegressionCV()
        classifier = load('COLD/C_lrcv.joblib')
        X[0] = model_C.scaler(X[0])
        X[1] = model_C.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def RandomForest(X):
        classifier = RandomForestClassifier()
        classifier = load('COLD/C_rf.joblib')
        X[0] = model_C.scaler(X[0])
        X[1] = model_C.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def Svc(X):
        classifier = SVC()
        classifier = load('COLD/C_svm.joblib')
        X[0] = model_C.scaler(X[0])
        X[1] = model_C.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def Xgboost(X):
        classifier = XGBClassifier()
        classifier.load_model('COLD/C_xgb')
        X[0] = model_C.scaler(X[0])
        X[1] = model_C.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def select(X):
        cb = X.copy()
        knn = X.copy()
        lr = X.copy()
        lrcv = X.copy()
        rf = X.copy()
        sv = X.copy()
        xgb = X.copy()
        
        mod = [model_C.CatBoost(cb), 
               model_C.K_NN(knn), 
               model_C.LogisticReg(lr), 
               model_C.LogisticRegCV(lrcv), 
               model_C.RandomForest(rf), 
               model_C.Svc(sv), 
               model_C.Xgboost(xgb)]
        return mod
        