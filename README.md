### Predicting Disease from Age, Gender, Symptom

Creating and deploying a model as described in https://github.com/alexeygrigorev/mlbookcamp-code/

Disclaimer: The only purpose of this code repository is creating and deploying an example statistical model. No medical advice. The underlying data my be wrong and any conclusion made false.

Dataset: https://www.kaggle.com/datasets/abbotpatcher/respiratory-symptoms-and-treatment

Notebook: https://www.kaggle.com/code/bnzn261029/midterm-resp

Input:

	patient = {
		'Age': 60,
		'Sex=female': 0, 
		'Sex=male': 1, 
		'Sex=not to say': 0,
		'Symptoms_encoded': 48,
	}

Output:

	{
	  "disclaimer": "This script is for educational purpose only.",
	  "disease": "Pneumonia",
	  "disease_probability": 0.19968054490140236,
	  "patient:": {
		"Age": 60,
		"Sex=female": 0,
		"Sex=male": 1,
		"Sex=not to say": 0,
		"Symptoms_encoded": 48
	  }
	}

Create virtual environment and install requirements

	pip install -r requirements.txt

Run the flask app

	python flask_app.py

Run the example post request

	python test_service.py