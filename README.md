# 🏠 California Housing Price Prediction

A comprehensive machine learning project that predicts housing prices in California using the California Housing Dataset. This project includes data exploration, model training, hyperparameter tuning, and a web application for real-time predictions.

## 📋 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models and Performance](#models-and-performance)
- [Web Application](#web-application)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Data Exploration & Visualization**: Comprehensive analysis of the California Housing Dataset
- **Feature Engineering**: Custom transformers for creating meaningful features
- **Multiple ML Models**: Linear Regression, Decision Tree, and Random Forest implementations
- **Hyperparameter Tuning**: Grid Search and Randomized Search for optimal model performance
- **Web Interface**: Flask-based web application for easy price predictions
- **Preprocessing Pipeline**: Automated data preprocessing with imputation, scaling, and encoding
- **Model Persistence**: Saved models and pipelines for deployment

## 🛠 Technologies Used

- **Python 3.x**
- **Machine Learning**: Scikit-learn, NumPy, Pandas
- **Web Framework**: Flask
- **Data Visualization**: Matplotlib
- **Environment Management**: Virtual Environment
- **Model Serialization**: Pickle

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ml
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset** (optional - the notebook handles this):
   The dataset will be automatically downloaded when running the Jupyter notebook.

## 🚀 Usage

### Running the Jupyter Notebook

1. Start Jupyter:
   ```bash
   jupyter notebook
   ```

2. Open `housing.ipynb` and run all cells to:
   - Download and explore the dataset
   - Train and evaluate models
   - Perform hyperparameter tuning
   - Save the final model

### Running the Web Application

1. **First, run the Jupyter notebook** to generate the model files:
   ```bash
   jupyter notebook housing.ipynb
   ```
   Run all cells to train models and save `pipeline.pkl` and `randomized_search_random_forest_model.pkl`

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/`

4. Enter housing features and get price predictions

## 📁 Project Structure

```
ml/
├── app.py                          # Flask web application
├── housing.ipynb                   # Main analysis and modeling notebook
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── datasets/
│   └── housing/
│       └── housing.csv            # California housing dataset
├── static/
│   └── style.css                  # Web app styling
├── templates/
│   └── index.html                 # Web app template
├── env/                           # Virtual environment (ignored)
├── *.pkl                          # Saved models and pipelines
├── *_rmse_scores.npy              # Model evaluation scores
└── README.md                      # This file
```

## 🤖 Models and Performance

### Models Implemented

1. **Linear Regression**
   - RMSE: ~$68,628
   - Simple baseline model

2. **Decision Tree Regressor**
   - Training RMSE: ~$0 (overfitted)
   - CV RMSE: ~$71,000

3. **Random Forest Regressor**
   - Training RMSE: ~$18,600
   - CV RMSE: ~$50,000
   - Final tuned model: ~$48,000 RMSE on test set

### Final Model: Tuned Random Forest

- **Hyperparameters**: Optimized via RandomizedSearchCV
- **Features**: 16 (including engineered features)
- **Preprocessing**: Imputation, feature engineering, scaling, one-hot encoding

## 🌐 Web Application

The Flask web app provides an intuitive interface for housing price prediction:

- **Input Features**:
  - Longitude/Latitude
  - Housing median age
  - Total rooms/bedrooms
  - Population and households
  - Median income
  - Ocean proximity

- **Output**: Predicted median house value in dollars

## 📊 Dataset

**California Housing Dataset** from the 1990 US Census:

- **Source**: Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow
- **Size**: 20,640 samples
- **Features**: 8 numerical + 1 categorical
- **Target**: Median house value
- **Geographic Coverage**: California districts

### Key Insights from EDA

- Strong correlation between median income and house prices
- Coastal areas have higher property values
- Feature engineering improved model performance
- Stratified sampling ensured representative train/test splits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



