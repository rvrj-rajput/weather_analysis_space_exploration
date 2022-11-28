import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__)
model = pickle.load(open('Weather_analysis.pkl','rb'))

@app.route('/')
def home():
    return render_template('grid.html', result=None)

@app.route('/grid')
def grid():
	return render_template('grid.html', result=None)

@app.route('/predict1')
def predict1():
	return render_template('index.html', result=None)

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    classes = ['Cannot determine','Unfavorable conditions for launch', 'Favorable conditions for launch']
    int_features = [x for x in request.form.values()]
    z=[]
    for j in range(0,14):
        if j==0:
            a= ['Uncrewed','Crewed']
            for i in range(len(a)):
                if a[i]==int_features[j]:
                    z.append(i)
        if j==1:
            z.append(int_features[j])
        if j==2:
            z.append(int_features[j])
        if j==3:
            z.append(int_features[j])
        if j==4:
            z.append(int_features[j])
        if j==5:
            z.append(int_features[j])
        if j==6:
            z.append(int_features[j])
        if j==7:
            z.append(int_features[j])
        if j==8:
            z.append(int_features[j])
        if j==9:
            a= ['E','W','N','S','SE','SW','NE','NW']
            for i in range(len(a)):
                if a[i]==int_features[j]:
                    z.append(i)
        if j==11:
            a = (int(int_features[j])//10)+1
            z.append(a)
        if j==12:
            a= ['Cloudy', 'Partly Cloudy', 'Mostly Cloudy', 'Fair', 'Windy','T-Storm', 'Rain', 'Thunder', 'Light Rain','Heavy T-Storm']
            for i in range(len(a)):
                if a[i]==int_features[j]:
                    z.append(i)
        if j==13:
            z.append(int_features[j])
    b = [float(k) for k in z]
    final_features=np.array(b)
    final_features = final_features.reshape(1,13)
    prediction = model.predict(final_features)[0]

    return render_template('index.html', prediction_text='The system suggests : {}'.format(classes[prediction]))

@app.route('/rock')
def rock():
	return render_template('upload.html', result=None)

if __name__ == "__main__":
    app.run(debug=True)