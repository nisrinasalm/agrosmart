import numpy as np
from flask import redirect, render_template, request, url_for
from markupsafe import Markup
from app import utils
from app import app

# Render homepage
@app.route('/')
def home():
  return render_template('index.html')

# Render crop recommendation page
@app.route('/crop-recommendation')
def crop_recommendation():
  return render_template('crop-recommendation.html')

# Render predicted crop recommendation page
@app.route('/predicted-crop-recommendation', methods=['POST'])
def predicted_crop_recommendation():
  N = int(request.form['nitrogen'])
  P = int(request.form['phosphorous'])
  K = int(request.form['potassium'])
  city = request.form.get('city')
  ph = float(request.form['ph'])
  rainfall = float(request.form['rainfall'])

  if utils.weather_fetch(city) != None:
    temperature, humidity = utils.weather_fetch(city)
    user_input = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled = utils.normalization(user_input)
    prediction = utils.crop_recommendation.predict(scaled)
    result = utils.recommendation_label(prediction)
    return render_template('predicted-recommendation.html', prediction=result)
  else:
    return redirect(url_for('crop_recommendation'))
