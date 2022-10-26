# Predicting Respiratory Disease from Age, Gender, Symptom

Creating and deploying a model as described in https://github.com/alexeygrigorev/mlbookcamp-code/

*Disclaimer: The only purpose of this code repository is creating and deploying an example statistical model. No medical advice. The underlying data my be wrong and any conclusion made false.*

Dataset: https://www.kaggle.com/datasets/abbotpatcher/respiratory-symptoms-and-treatment

Notebook: https://www.kaggle.com/code/bnzn261029/midterm-resp

### Example

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
	
This version of the model suffers from low accuracy. For a male 60 years old patient with a cold it predicts pneumonia with a probability of 20 %. If the age is changed to 10 years old it suggests bronchitis with a probability of 22 %.

Output:

	{
	  "disclaimer": "This script is for educational purpose only.",
	  "disease": "bronchitis",
	  "disease_probability": 0.2179886636147549,
	  "patient:": {
		"Age": 10,
		"Sex=female": 0,
		"Sex=male": 1,
		"Sex=not to say": 0,
		"Symptoms_encoded": 48
	  }
	}

### Run the Service

Create virtual environment and install requirements

	pip install -r requirements.txt

Run the flask app

	python flask_app.py

Open another command window and run the example post request

	python test_service.py

### Labels

LabelEncoder() Disease:

0 Acute Respiratory Distress Syndrome
1 Asbestosis
2 Aspergillosis
3 Asthma
4 Bronchiectasis
5 Chronic Bronchitis
6 Influenza
7 Mesothelioma
8 Pneumonia
9 Pneumothorax
10 Pulmonary hypertension
11 Respiratory syncytial virus
12 Tuberculosis
13 bronchiolitis
14 bronchitis
15 chronic obstructive pulmonary disease
16 sleep apnea

LabelEncoder() Symptoms:

0  coughing
1  coughing
2  fatigue
3  low energy
4  shortness of breath
5  wheezing
6 A cough that lasts more than three weeks
7 A dry, crackling sound in the lungs while breathing in
8 Bluish skin
9 Chest congestion
10 Chest pain
11 Chills
12 Coughing up blood
13 Coughing up yellow or green mucus daily
14 Daytime sleepiness
15 Difficulties with memory and concentration
16 Dry mouth
17 Fatigue
18 Fatigue, feeling run-down or tired
19 Feeling run-down or tired
20 Fever
21 Frequently waking
22 Headache
23 Loss of appetite
24 Loss of appetite and unintentional weight loss
25 Low-grade fever
26 Morning headaches
27 Nasal congestion
28 Nausea
29 Night sweats
30 Pauses in breathing
31 Persistent dry coug
32 Persistent dry cough
33 Rapid breathing
34 Rapid heartbeat
35 Runny nose
36 Shortness of breath
37 Shortness of breath that gets worse during flare-ups
38 Snoring
39 Sore throat
40 Unusual moodiness
41 Weight loss from loss of appetite
42 Wheezing
43 Wider and rounder than normal fingertips and toes
44 allergy
45 breath
46 chest pain
47 chronic cough
48 cold
49 cough
50 cough with blood
51 coughing
52 diarrhea
53 distressing
54 dizziness
55 dry cough
56 edema
57 fainting
58 faster heart beating
59 fatigue
60 fever
61 greenish cough
62 heart palpitations
63 high fever
64 irritability
65 joint pain
66 loss of appetite
67 low energy
68 lower back pain
69 mucus
70 muscle aches
71 nausea
72 pain
73 runny nose
74 shaking
75 shallow breathing
76 sharp chest pain
77 short of breath
78 short, shallow and rapid breathing
79 shortness of breath
80 stuffy nose
81 sweating
82 tight feeling in the chest
83 vomiting
84 weight loss
85 wheezing
86 wheezing cough
87 whistling sound while breathing
88 whistling sound while you breathe
89 yellow cough