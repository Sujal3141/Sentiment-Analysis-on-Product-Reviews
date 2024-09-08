from flask import Flask, render_template, request
import pandas as pd
import pickle


app = Flask(__name__)

model,vectorizer = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = str(request.form['Text'])
    t = vectorizer.transform([text])

    

    
    prediction = model.predict(t)
    if prediction==1:
        prediction="Positive sentiment"
    else:
        prediction ="Negative sentiment"
    return render_template('home.html', sentiment=prediction)

if __name__ == "__main__": 
    app.run(debug=True)
