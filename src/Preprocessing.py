import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def pre_data(data):

    #seperating features and target
    x=data.drop('Price',axis=1)
    y=data['Price']

    # split the data 
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42)

    # numerical_col and pipeline
    num_col=x_train.select_dtypes(include=['float64','int64'])

    num_pip=Pipeline([('impute',SimpleImputer(strategy='median')),
                      ('scale',StandardScaler())
                      ])

    # categorical_col and pipeline
    cat_col=x_train.select_dtypes(include=['object'])

    cat_pip=Pipeline([('impute',SimpleImputer(strategy='most_frequent')),
                      ('encode',OneHotEncoder(handle_unknown='ignore'))
                      ])
    # combining numerical and categorical columns
    pre=ColumnTransformer([('num',num_pip,num_col.columns.tolist()),
                           ('cat',cat_pip,cat_col.columns.tolist())
                           ])
    return x_train,x_test,y_train,y_test,pre
    
