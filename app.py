from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

class CombinedAttributesAdder:
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        import numpy as np
        rooms_per_household = X[:, 3] / X[:, 6]
        population_per_household = X[:, 5] / X[:, 6]
        bedrooms_per_room = X[:, 4] / X[:, 3]
        return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]



import pickle
preprocessor = pickle.load(open('pipeline.pkl', 'rb'))


model = pickle.load(open('randomized_search_random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        data = {
            'longitude': float(request.form['longitude']),
            'latitude': float(request.form['latitude']),
            'housing_median_age': float(request.form['housing_median_age']),
            'total_rooms': float(request.form['total_rooms']),
            'total_bedrooms': float(request.form['total_bedrooms']),
            'population': float(request.form['population']),
            'households': float(request.form['households']),
            'median_income': float(request.form['median_income']),
            'ocean_proximity': request.form['ocean_proximity']
        }

    
        input_df = pd.DataFrame([data])

        
        processed_input = preprocessor.transform(input_df)

        
        prediction = model.predict(processed_input)

        return render_template('index.html',
                               prediction_text=f"Estimated Price: {prediction[0]:,.2f}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)