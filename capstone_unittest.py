import re
import numpy as np
import datetime
import pandas as pd
import unittest

# function or class to be tested
format = "%Y-%m-%d"

def slr_forecast(x_query):
    if not isinstance(x_query, dict):
        print("waiting for a dictionary")  
    elif isinstance(x_query, dict):
        try: 
            first_value = list(x_query.values())[0]
            datetime.datetime.strptime(first_value, format)
            print("This is the correct date string format.") 
        
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD") 
                
    # Generate a one step ahead
    data = {'date': ['2019-08-01','2019-09-01','2019-10-01','2019-11-01'], 'series': [10,20,30,40]}  
    df = pd.DataFrame(data)  
    value = list(x_query.values())[0]
    forecast = df['series'].loc[df['date']==value]             
    
    return(forecast.values[0])


class TestSimpleLForecast(unittest.TestCase):

    # example test method
    def test_numeric(self):
        forecast = slr_forecast(2019)
        self.assertEqual(30, forecast)

    def test_str(self):
        forecast = slr_forecast('2019-10-01')
        self.assertEqual(30, forecast)
        
    def test_str(self):
        forecast = slr_forecast({'steps' : '2019-10-01'})
        self.assertEqual(30, forecast)