from flask import Flask, render_template, request
from src.predict import predict_anemia

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    values = [
        float(request.form['Hb']),
        float(request.form['RBC']),
        float(request.form['MCV']),
        float(request.form['MCH']),
        float(request.form['MCHC']),
        float(request.form['RDW']),
        float(request.form['Age'])
    ]

    prediction, probability = predict_anemia(values)

    result = "Anemia Detected" if prediction == 1 else "Normal"

    return render_template('index.html',
                           prediction_text=result,
                           probability=round(probability*100,2))

if __name__ == "__main__":
    app.run(debug=True)
