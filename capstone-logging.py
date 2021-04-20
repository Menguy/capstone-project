#!/usr/bin/env python

import time,os,re,csv,sys,uuid,joblib
from datetime import date
import numpy as np

def train_model(X,saved_model):
    model = sm.tsa.statespace.SARIMAX(X,order=(0, 1, 0),seasonal_order=(1, 1, 0, 12))
    result = model.fit()
    print('aic value :', result.aic)
    
    ## saving model
    print("... saving model: {}".format(saved_model))
    joblib.dump(result,saved_model)


def _update_forecast_log(forecast,query,runtime):
    """
    update forecast log file
    """

    ## name the logfile using something that cycles with date (day, month, year)    
    today = date.today()
    logfile = "capstone-predict-{}-{}.log".format(today.year, today.month)
    
    ## write the data to a csv file    
    header = ['unique_id','timestamp','forecast','x_shape','model_version','runtime']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        if write_header:
            writer.writerow(header)
    
        to_write = map(str,[uuid.uuid4(),time.time(),forecast,query,MODEL_VERSION,runtime])
        writer.writerow(to_write)

def forecast(query):
    """
    """

    ## start timer for runtime
    time_start = time.time()
    
    ## ensure the model is loaded
    model = joblib.load(saved_model)
   
    ## make prediction and gather data for log entry
    query = pd.DataFrame.from_dict(query,orient = 'index')
    print('query[0][0] : ',query[0][0])
    forecast = model.get_forecast(query[0][0])
    print('forecast : ', forecast)
    
    m, s = divmod(time.time()-time_start, 60)
    h, m = divmod(m, 60)
    runtime = "%03d:%02d:%02d"%(h, m, s)

    ## update the log file
    _update_forecast_log(forecast,query,runtime)
    
    return(forecast)


if __name__ == "__main__":

    ## import some data to play with
    X=pd.read_csv('invoices.csv')
    X = X[['date','price']]
    X = X.set_index('date')

    ## train the model
    MODEL_VERSION = 1.0
    saved_model = "capstone-forecast-{}.joblib".format(re.sub("\.","_",str(MODEL_VERSION)))
    model = train_model(X,saved_model)

    ## example forecast
    query={'steps':'2019-11-01'}
    forecast = forecast(query)
    print("forecast: {}".format(forecast))
