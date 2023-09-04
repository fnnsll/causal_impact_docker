from datetime import datetime
from src.inference import main as f_inference
from src.consts import csv,date,region,kpi,y,X,pre_period,post_period, test_percent

timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

def main(timestamp=timestamp):
    f_inference(csv,date,region,kpi,y,X,pre_period,post_period,test_percent,timestamp)
    string = 'run completed for {0}'.format(timestamp)
    return print(string)

main(timestamp)
    