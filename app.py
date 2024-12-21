print("Starting script...")

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

print("Imports successful...")

app = Flask(__name__)
print("Flask app created...")

# Load and train model
data = pd.read_csv('diabetes_detection.csv')
X = data.drop('Outcome', axis=1)
y = data['Outcome']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = LogisticRegression()
model.fit(X_scaled, y)
print("Model trained successfully...")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    result = None
    if request.method == 'POST':
        try:
            features = []
            for i in range(1, 9):
                val = float(request.form[f'n{i}'])
                features.append(val)
            
            features_array = np.array(features).reshape(1, -1)
            features_scaled = scaler.transform(features_array)
            prediction = model.predict(features_scaled)
            
            if prediction[0] == 1:
                result = "You have high chances of getting Diabetes. Please consult a doctor."
            else:
                result = "You are safe from Diabetes, but please maintain a healthy diet."
        except Exception as e:
            result = f"Error in prediction: {str(e)}"
    
    return render_template('predict.html', result=result)

print("Routes defined...")

# Remove if __name__ == '__main__' and directly run the app
print("Starting Flask server...")
app.run(debug=True, port=5000, host='127.0.0.1')