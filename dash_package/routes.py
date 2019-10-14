from flask import render_template, request

from dash_package.dashboard import app

from dash_package.functions import *



@app.server.route('/model', methods = ['GET'])
def render_html():
    return render_template('classifier.html')

@app.server.route('/model', methods = ['POST'])
def predict():
    text = request.form.get('text')
    prediction = classify_text(text)

    if prediction == 0:
        return render_template('nope.html')
    if prediction == 1:
        return render_template('twss.html')
