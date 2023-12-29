import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the model
regmodel=pickle.load(open("regmodel.pkl", 'rb'))
scalar=pickle.load(open("scaling.pkl", 'rb'))

@app.route('/')
def home():
    return render_template('home.html')  # Home page

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0]) # 2D array
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)