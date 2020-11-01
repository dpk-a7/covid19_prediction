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

class model_Fl:
    @staticmethod
    def scaler(X):
        return X/100
    @staticmethod
    def CatBoost(X):
        classifier = CatBoostClassifier()
        classifier.load_model('FLU/Fl_cb',format = 'cbm')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def K_NN(X):
        classifier = KNeighborsClassifier()
        classifier = load('FLU/Fl_knn.joblib')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticReg(X):
        classifier = LogisticRegression()
        classifier = load('FLU/Fl_lr.joblib')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def LogisticRegCV(X):
        classifier = LogisticRegressionCV()
        classifier = load('FLU/Fl_lrcv.joblib')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def RandomForest(X):
        classifier = RandomForestClassifier()
        classifier = load('FLU/Fl_rf.joblib')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def Svc(X):
        classifier = SVC()
        classifier = load('FLU/Fl_svm.joblib')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def Xgboost(X):
        classifier = XGBClassifier()
        classifier.load_model('FLU/Fl_xgb')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def NaiveB(X):
        classifier = GaussianNB()
        classifier = load('FLU/Fl_nb.joblib')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
        X = np.array(X).reshape((1,-1))
        return classifier.predict(X)[0]
    @staticmethod
    def DecisionT(X):
        classifier = DecisionTreeClassifier()
        classifier = load('FLU/Fl_dt.joblib')
        X[0] = model_Fl.scaler(X[0])
        X[1] = model_Fl.scaler(X[1])
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
        nb = X.copy()
        dt = X.copy()
        
        mod = [model_Fl.CatBoost(cb), 
               model_Fl.K_NN(knn), 
               model_Fl.LogisticReg(lr), 
               model_Fl.LogisticRegCV(lrcv), 
               model_Fl.RandomForest(rf), 
               model_Fl.Svc(sv), 
               model_Fl.Xgboost(xgb),
               model_Fl.NaiveB(nb),
               model_Fl.DecisionT(dt)]
        return mod
        