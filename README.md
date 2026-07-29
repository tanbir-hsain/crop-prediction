# Crop Prediction System

## Project Description

Crop Prediction System built using Python, Flask, and Machine Learning to recommend the most suitable crop based on soil and environmental conditions.

The application allows users to enter farming details such as soil nutrients, temperature, humidity, rainfall, land area, and number of workers. A trained Decision Tree model predicts the suitable crop and also estimates farming cost and expected profit.

This project demonstrates Machine Learning model training, Flask web development, and deployment on AWS EC2.

---

## Tech Stack

- Python
- Flask
- Machine Learning
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS
- AWS EC2
- Git & GitHub

---

## System Architecture

```text
User
   ↓
Flask Web Application
   ↓
User Input
   ↓
Decision Tree Model
   ↓
Crop Prediction
   ↓
Cost & Profit Estimation
   ↓
Prediction Result
```

---

## Features

- Crop recommendation using Machine Learning
- User-friendly Flask web interface
- Decision Tree prediction model
- Farming cost estimation
- Expected profit estimation
- AWS EC2 deployment

---

## Project Workflow

1. User enters farming details.
2. Flask receives the input values.
3. Input is sent to the trained Decision Tree model.
4. The model predicts the most suitable crop.
5. Farming cost and expected profit are calculated.
6. The prediction is displayed on the webpage.

---

## Machine Learning Model

### Dataset

- crop_data.csv

### Algorithm

- Decision Tree Classifier

### Libraries

- Scikit-learn
- Pandas
- Joblib

---

## Input Parameters

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- Rainfall
- Area
- Workers

---

## Output

- Recommended Crop
- Estimated Farming Cost
- Estimated Profit

---

## Installation

Clone the repository

```bash
git clone https://github.com/tanbir-hsain/crop-prediction.git
```

Move into the project

```bash
cd crop-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

## Project Structure

```text
crop-prediction
│
├── app.py
├── train.py
├── model.pkl
├── crop_data.csv
├── requirements.txt
├── templates/
├── static/
└── .gitignore
```

---

## Skills Demonstrated

- Python Programming
- Flask Development
- Machine Learning
- Decision Tree Classifier
- Model Training
- Web Application Development
- AWS EC2 Deployment
- Git & GitHub

---

## Future Improvements

- Use larger datasets for improved prediction accuracy.
- Add fertilizer recommendations.
- Add weather API integration.
- Support multiple regional languages.
- Deploy using a custom domain.

---

## Demo Video

https://youtu.be/z-CKW1FL1Xw

---

## Author

**Tanbir Hussain**

GitHub  
https://github.com/tanbir-hsain

LinkedIn  
https://www.linkedin.com/in/tanbir-hussain-76320b414
