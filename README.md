# POULTRY_APP
# 🐔 Poultry Disease Prediction System

🔗 **[Live Demo](https://web-production-ed4b7.up.railway.app/login)** 
         username: admin
         password: password123
A smart web-based system to predict poultry diseases using deep learning models based on  images, helping farmers and poultry owners with early diagnosis.

## 🔍 Overview

Poultry farming is often affected by various diseases that spread rapidly and cause significant economic losses. This project aims to assist farmers by predicting diseases based on either user-input symptoms or uploaded images, allowing timely interventions.

## ✅ Features

- 🧠 Predict diseases using a trained ML/DL model  
- 📸 Image-based or form-based input options  
- 🐥 Common diseases like Newcastle, Salmonellosis,..etc 
- 🌐 Flask-based web interface for easy access  
- 📊 Displays disease name, confidence, uploaded image 

## 🧰 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow / Keras
- **Libraries**: NumPy, Pandas, Pillow

## 🧪 Model Training

- Dataset: Collected from online poultry disease databases and image datasets
- Preprocessing: Image resizing, normalization, and augmentation
- Algorithms: Transfer Lerning using ResNet50
- Accuracy: ~90%+ on validation data

## 🌐 Live Demo

Check out the deployed web app here:  
👉 (https://web-production-ed4b7.up.railway.app/login)


## 🧑‍💻 Setup & Run


1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/poultry-disease-prediction.git
   cd poultry-disease-prediction
2. Create a virtual environment and activate it (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Flask app:
   ```bash
   python app.py
5. Open browser and visit:
   http://127.0.0.1:500
   


