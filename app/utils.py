import requests
import numpy as np
from flask import json
from app import config
from keras.models import load_model

# Load crop recommendation model
crop_recommendation = load_model('app/data/models/weights.193-0.042.keras')

# Cast numeric label back to wordish prediction
def recommendation_label(prediction):
  result = np.argmax(prediction)

  with open('app/data/labels/dict_crop_recommendation.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == value:
      return key

# Normalize input range
def normalization(array_parameter):
  # Value is retrieved from the df.describe()
  min_val = [0, 5, 5, 8.825675, 14.258040, 3.504752, 20.211267]
  max_val = [140, 145, 205, 43.675493, 99.981876, 9.935091, 298.560117]

  for i in range(len(array_parameter[0])):
    array_parameter[0][i] = (array_parameter[0][i] - min_val[i]) / (max_val[i] - min_val[i])

  np_scaled = np.array(array_parameter)
  return np_scaled

# Fetch weather API
def weather_fetch(city_name):
  WEATHER_API = config.BASE_URL + city_name + ',id' + '&appid=' + config.API_KEY

  weather = requests.get(WEATHER_API)
  response_weather = weather.json()

  if response_weather['cod'] != '404':
    main = response_weather['main']
    temperature = round((main['temp'] - 273.15), 2)
    humidity = main['humidity']
    return temperature, humidity
  else:
    return None