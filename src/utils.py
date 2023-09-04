import pandas as pd
import numpy as np
import sys
import os
import warnings
import logging
from datetime import datetime



def write_summary(ci,y,X,timestamp):
	with open('/home/output/ci_summary_'+y+'_'+X+'_'+timestamp+'.txt', 'w') as f:
		original_stdout = sys.stdout
		sys.stdout = f
		print(ci.summary())
		sys.stdout = original_stdout
		return None

def make_dataframe(csv, date, region, kpi, y, X):
	df = pd.read_csv(csv, sep=';')
	df = df.pivot(index = date, columns = region, values = kpi)
	data = df[[y,X]]
	data.rename({y:'y', X:'X'}, axis=1, inplace=True)
	data = data.head(-3) #Custom for this dataset
	return data

def test_simulation(data, test_percent, date):
    df_pre = data[data.index < date]
    df_post = data[data.index >= date]
    df_post.y = test_percent * df_post.y
    return pd.concat([df_pre,df_post], axis = 0)
