from flask import Flask, request, render_template

from functions import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/model', methods = ['GET'])
def render_html():
    return render_template('classifier.html')

@app.route('/model', methods = ['POST'])
def predict():
    text = request.form.get('text')
    prediction = classify_text(text)
    if prediction == 0:
        return render_template('nope.html', variable = text)
    if prediction == 1:
        return render_template('twss.html', variable = text)
