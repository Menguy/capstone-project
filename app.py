
from flask import Flask, jsonify, request
import joblib
import socket
import json
import pandas as pd
import os

MODEL_DIR = 'models'
DATA_DIR = 'data'

app = Flask(__name__)

@app.route("/")
#def hello():
#    html = "<h3>Capstone {name}!</h3>" \
#           "<b>Hostname:</b> {hostname}<br/>"
#    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route('/get_forecast', methods=['GET','POST'])

def get_forecast():   
    ## input checking
    if not request.json:
        print("ERROR: API (predict): did not receive request data")
        return jsonify([])
    
    query = request.json
    query_init = query
    query = pd.DataFrame.from_dict(query,orient = 'index')

    if len(query.shape) == 1:
         query = query.reshape(1, -1)

    forecast = model.get_forecast(query[0][0])
    
    result = forecast.summary_frame()
    result.drop(columns=['mean_se','mean_ci_lower','mean_ci_upper'],inplace=True)
    result.rename(columns={"mean": "forecast"},inplace=True)
    result.index = result.index.set_names(['date'])
    result = result.reset_index()
    result['date'] = result['date'].astype(str)

    dict=result.to_dict('records')
    
    return(jsonify(dict))

            
if __name__ == '__main__':
    saved_model = 'capstone.joblib'
    model = joblib.load(os.path.join(MODEL_DIR, saved_model))
    app.run(host='127.0.0.1', port=5000,debug=True)
