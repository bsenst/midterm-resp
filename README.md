# Predicting Respiratory Disease from Age, Gender, Symptom

Creating and deploying a model as described in https://github.com/alexeygrigorev/mlbookcamp-code/

*Disclaimer: The only purpose of this code repository is creating and deploying an example statistical model. No medical advice. The underlying data my be wrong and any conclusion made false.*

Dataset: https://www.kaggle.com/datasets/abbotpatcher/respiratory-symptoms-and-treatment

* 1st Notebook for EDA and initial Model: https://www.kaggle.com/code/bnzn261029/midterm-resp
* 2nd Notebook with cleaned data (i.e. symptom list) and rebuild, second Model: https://www.kaggle.com/code/bnzn261029/fork-of-midterm-resp-symptoms-cleaned
* 3rd Notebook with Decision Tree: https://www.kaggle.com/code/bnzn261029/midterm-resp-decision-tree

### Problem Description

In medicine finding the right diagnosis is key for successful treatment and thus restituation of health. Diagnosing a disease involves several steps. It includes history taking, physical examination and diagnostic procedures followed by a preliminary list of possible diagnoses. Then estimation of the most likely diagnosis can be made through different statistic techniques and experienced clinicians develop an instinct to come to a conclusion fast. But improving the diagnostic process and reducing uncertainty is an ongoing challenge and offers opportunities for data science solutions.

Ahsan MM, Luna SA, Siddique Z. Machine-Learning-Based Disease Diagnosis: A Comprehensive Review. Healthcare (Basel). 2022 Mar 15;10(3):541. doi: 10.3390/healthcare10030541. PMID: 35327018; PMCID: PMC8950225.

Raita Y, Camargo CA Jr, Liang L, Hasegawa K. Big Data, Data Science, and Causal Inference: A Primer for Clinicians. Front Med (Lausanne). 2021 Jul 6;8:678047. doi: 10.3389/fmed.2021.678047. PMID: 34295910; PMCID: PMC8290071.

### Example

Input (as used in test_service.py)

	patient = {
		'Age': 60,
		'Sex=female': 0, 
		'Sex=male': 1, 
		'Sex=not to say': 0,
		'Symptoms_encoded': 48,
	}

Or send curl request to Flask API https://bsenst.pythonanywhere.com/predict (availability not guaranteed)

	curl --location --request POST 'https://bsenst.pythonanywhere.com/predict' \
	--header 'Content-Type: application/json' \
	--data-raw '{"Age": 60, "Sex=female": 0, "Sex=male": 1, "Sex=not to say": 0, "Symptoms_encoded": 48}'

Output (response from the model served as flask app):

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

### Run the Service using Python

Create virtual environment (as described in [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html))

	python3 -m venv virtualenv
	
Then activate the virtual environment for Windows

	virtualenv\Scripts\activate.bat

Or on Unix/MacOS
	
	source virtualenv/bin/activate
	
Install requirements

	pip install -r requirements.txt

Run the flask app

	python flask_app.py

Open another command window and run the example post request

	python test_service.py

Make sure the test script sends the request to the url the flask app is being served (i.e. https://172.17.0.2:9696).
	
### Run the Service using Docker

Download the docker image (206.6 MB)

	docker pull fritz.jfrog.io/default-docker-local/midterm-resp-docker:latest

Compare the checksum sha256 78583fdc866a728a2d3588d3d7c45b44b7a9f9a9c2175e81688d9ec5ab6d5a42

Build and run the docker image
	
	docker build --tag midterm-resp-docker

	docker run midterm-resp-docker

You should see that the flask app is being served. Open another terminal and run the test script.

	python test_service.py

Make sure the test script sends the request to the url the flask app is being served (i.e. https://172.17.0.2:9696).

### 



### Labels

LabelEncoder() Disease:

|Label |Disease|
|--- |---|
|0 |Acute Respiratory Distress Syndrome|
|1 |Asbestosis|
|2 |Aspergillosis|
|3 |Asthma|
|4 |Bronchiectasis|
|5 |Chronic Bronchitis|
|6 |Influenza|
|7 |Mesothelioma|
|8 |Pneumonia|
|9 |Pneumothorax|
|10 |Pulmonary hypertension|
|11 |Respiratory syncytial virus|
|12 |Tuberculosis|
|13 |bronchiolitis|
|14 |bronchitis|
|15 |chronic obstructive pulmonary disease|
|16 |sleep apnea|

LabelEncoder() Symptoms:

|Label |Symptom|
|--- |---|
|0  |coughing|
|1  |coughing|
|2  |fatigue|
|3  |low energy|
|4  |shortness of breath|
|5  |wheezing|
|6 |A cough that lasts more than three weeks|
|7 |A dry, crackling sound in the lungs while breathing in|
|8 |Bluish skin|
|9 |Chest congestion|
|10 |Chest pain|
|11 |Chills|
|12 |Coughing up blood|
|13 |Coughing up yellow or green mucus daily|
|14 |Daytime sleepiness|
|15 |Difficulties with memory and concentration|
|16 |Dry mouth|
|17 |Fatigue|
|18 |Fatigue, feeling run-down or tired|
|19 |Feeling run-down or tired|
|20 |Fever|
|21 |Frequently waking|
|22 |Headache|
|23 |Loss of appetite|
|24 |Loss of appetite and unintentional weight loss|
|25 |Low-grade fever|
|26 |Morning headaches|
|27 |Nasal congestion|
|28 |Nausea|
|29 |Night sweats|
|30 |Pauses in breathing|
|31 |Persistent dry coug|
|32 |Persistent dry cough|
|33 |Rapid breathing|
|34 |Rapid heartbeat|
|35 |Runny nose|
|36 |Shortness of breath|
|37 |Shortness of breath that gets worse during flare-ups|
|38 |Snoring|
|39 |Sore throat|
|40 |Unusual moodiness|
|41 |Weight loss from loss of appetite|
|42 |Wheezing|
|43 |Wider and rounder than normal fingertips and toes|
|44 |allergy|
|45 |breath|
|46 |chest pain|
|47 |chronic cough|
|48 |cold|
|49 |cough|
|50 |cough with blood|
|51 |coughing|
|52 |diarrhea|
|53 |distressing|
|54 |dizziness|
|55 |dry cough|
|56 |edema|
|57 |fainting|
|58 |faster heart beating|
|59 |fatigue|
|60 |fever|
|61 |greenish cough|
|62 |heart palpitations|
|63 |high fever|
|64 |irritability|
|65 |joint pain|
|66 |loss of appetite|
|67 |low energy|
|68 |lower back pain|
|69 |mucus|
|70 |muscle aches|
|71 |nausea|
|72 |pain|
|73 |runny nose|
|74 |shaking|
|75 |shallow breathing|
|76 |sharp chest pain|
|77 |short of breath|
|78 |short, shallow and rapid breathing|
|79 |shortness of breath|
|80 |stuffy nose|
|81 |sweating|
|82 |tight feeling in the chest|
|83 |vomiting|
|84 |weight loss|
|85 |wheezing|
|86 |wheezing cough|
|87 |whistling sound while breathing|
|88 |whistling sound while you breathe|
|89 |yellow cough|