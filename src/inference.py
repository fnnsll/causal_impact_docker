import sys
import os
import warnings
import logging
from datetime import datetime

logging.getLogger('tensorflow').setLevel(logging.FATAL)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from causalimpact import CausalImpact
from src.plotter import plot as plotter
from src.utils import *
from src.plotter import build_data as build_data

def main(csv,date,region,kpi,y,X,pre_period,post_period,test_percent, timestamp):
	data = make_dataframe(csv, date, region, kpi, y, X)
         
	data = test_simulation(data=data, test_percent=test_percent, date = post_period[0])

	ci = CausalImpact(data, pre_period, post_period)

	plotter(ci.inferences, ci.pre_data, ci.post_data[ci._mask],
	                    panels=['original', 'pointwise', 'cumulative'], figsize=(15, 12), show=False, timestamp=timestamp, y=y, X=X)

	write_summary(ci,y,X,timestamp)

	pre_data, post_data, inferences = build_data(ci.pre_data,ci.post_data[ci._mask], ci.inferences)
	pre_data.to_csv('/home/output/ci_pre_data_'+y+'_'+X+'_'+timestamp+'.csv')
	post_data.to_csv('/home/output/ci_post_data_'+y+'_'+X+'_'+timestamp+'.csv')
	inferences.to_csv('/home/output/ci_inferences_'+y+'_'+X+'_'+timestamp+'.csv')

	return None