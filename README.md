# 🐱🐶 CatDog AI

A Deep Learning image classification project that uses a **Convolutional Neural Network (CNN)** to classify an input image as either a **Cat** or a **Dog**.

## 🚀 Project Overview

CatDog AI is an image classification application built using **TensorFlow/Keras** and **Streamlit**.

The CNN model is trained on **2,000 cat and dog images** and learns visual patterns from the images to make predictions on new images.

## ✨ Features

* 🐱 Cat vs Dog image classification
* 🧠 CNN-based Deep Learning model
* 🖼️ Image upload support
* ⚡ Real-time prediction
* 🌐 Streamlit web interface
* 📊 Model performance information

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pillow
* Streamlit
* CNN (Convolutional Neural Network)

## 📊 Model Performance

| Metric              |   Accuracy |
| ------------------- | ---------: |
| Training Accuracy   | **83.20%** |
| Validation Accuracy | **74.06%** |
| Test Accuracy       | **74.50%** |

## 🧠 How It Works

The application follows this workflow:

```text
Upload Image
     ↓
Image Preprocessing
     ↓
CNN Model
     ↓
Feature Extraction
     ↓
Classification
     ↓
Cat / Dog
```

The uploaded image is processed into the format expected by the CNN model. The trained model then analyzes the image and predicts whether it belongs to the **Cat** or **Dog** class.

## 📁 Project Structure

```text
CatDog_AI/
│
├── app.py
├── Cat_Dog_Classifier(CNN).ipynb
├── cat_dog_model.keras
├── requirements.txt
├── archive.zip
└── README.md
```

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/thedevcodex/CatDog_AI.git
```

### 2. Open the project

```bash
cd CatDog_AI
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

## 🌐 Live Demo

Try the CatDog AI classifier:

👉 [**CatDog AI — Live Demo**](https://catdogai-thedevcodex.streamlit.app/)

## 🎯 Project Goal

The goal of this project is to understand and implement **Convolutional Neural Networks for image classification** and deploy the trained Deep Learning model as an interactive web application.

## 👨‍💻 Built By

**thedevcodex**

---

⭐ If you found this project useful, feel free to explore the repository.
