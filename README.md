### Predicting Disease from Age, Gender, Symptom

Creating and deploying a model as described in https://github.com/alexeygrigorev/mlbookcamp-code/

Disclaimer: The only purpose of this code repository is creating and deploying an example statistical model. No medical advice. The underlying data my be wrong and any conclusion made false.

Dataset: https://www.kaggle.com/datasets/abbotpatcher/respiratory-symptoms-and-treatment
Notebook: https://www.kaggle.com/code/bnzn261029/midterm-resp
Model: multinomial logistic regression, low accuracy 0.2 %, pickle file resp-model.bin

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

LabelEncoder Symptoms

LabelEncoder Disease