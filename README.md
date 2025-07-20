# AgroSmart: Crop Recommendation System

**AgroSmart** is a machine learning-based crop recommendation system that predicts the most suitable crop to cultivate based on environmental and soil conditions such as nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall.

## Project Description

This project leverages a trained deep learning model to classify the optimal crop using key agricultural features. AgroSmart can be accessed through both a command-line interface and a web application built with Flask.

## How It Works

1. **User Input**: Enter values for environmental parameters.
2. **Normalization**: Data is scaled based on min-max normalization.
3. **Prediction**: A neural network model classifies the most appropriate crop.
4. **Output**: Prediction is decoded into a readable crop label using a dictionary.

## Technologies Used

- Python
- TensorFlow / Keras
- Flask
- NumPy
- HTML, CSS (Jinja2 Templates)