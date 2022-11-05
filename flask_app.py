# Serving a model as described in mlbookcamp-code\chapter-05-deployment\churn_serving.py
# This script is for educational purpose only.

import pickle
import numpy as np

from flask import Flask, request, jsonify

def predict_single(patient, dv, model):
    X = dv.transform([patient])
    # y_pred = model.predict_proba(X)[:, 1]
    y_pred = model.predict_proba(X)
    # return y_pred[0]
    return y_pred


with open("resp-model.bin", "rb") as f_in:
    le_disease, le_symptoms, dv, model = pickle.load(f_in)


app = Flask('resp-pred')

@app.route('/')
def index():
    return 'Predicting Respiratory Disease from Age, Gender, Symptom'

@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()

    prediction = predict_single(patient, dv, model)
    
    p, d = list(reversed(sorted(zip([p for p in prediction[0]], le_disease.classes_))))[0]

    result = {
        'patient:': patient,
        'disease_probability': p,
        'disease': d,
        'disclaimer': "This script is for educational purpose only.",
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)