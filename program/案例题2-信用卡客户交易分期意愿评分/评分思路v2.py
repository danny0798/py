# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:00:21 2019

@author: hxm
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from sklearn import ensemble
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_auc_score
import scorecard_function
import xlrd
import csv
import codecs
#xlsx转为csv
def xlsx_to_csv(path,doc_name):
    workbook = xlrd.open_workbook(path)
    table = workbook.sheet_by_index(0)
    with codecs.open(doc_name, 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)

if __name__ == '__main__':
    xlsx_to_csv('试题2数据.xlsx','data.csv')
    
    #读取csv

data = pd.read_csv('data.csv')

data.describe()
             
data = data.drop(['six_optial_mp_num','six_optial_mp_avg_amt'],axis=1)
# id 没什么用处 也删掉
data = data.drop(['id'],axis=1)

trainData=data

allFeatures=trainData.columns.values.tolist()