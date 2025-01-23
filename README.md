# Predictive Analysis for Manufacturing Operations

This repository contains the implementation of a predictive analysis API designed for manufacturing workflows. The API uses machine learning to predict machine downtime or production defects, enhancing operational efficiency and decision-making.

## Features
- **Data Upload:** Upload manufacturing data through a POST endpoint.
- **Model Training:** Train a Random Forest model fine-tuned using Optuna and obtain performance metrics like accuracy and F1-score.
- **Prediction:** Generate predictions using JSON input, with results including confidence scores in JSON format.

## Technologies Used
- **Backend Framework:** FastAPI
- **Machine Learning:** scikit-learn (Random Forest)
- **Hyperparameter Tuning:** Optuna
- **Data Preprocessing:** numpy, pandas, and StandardScaler
- **Testing Tools:** requests module

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)


### Endpoints
1. **Predict:** POST `/predict`
   - Accepts JSON input with feature values and returns predictions with confidence scores.

### Example Request
**Input Example:**
```python

data = {
    "SupplierQuality": 86.648534,
    "DefectRate": 3.121492,
    "QualityScore": 63.463494,
    "MaintenanceHours": 9,
    "DowntimePercentage": 0.052343,
    "SafetyIncidents": 1,
    "EnergyConsumption": 2419.616785
}
```
**Response Example:**
```json
{
  "Downtime": "Yes",
  "Confidence": 0.85
}
```

## Project Structure
- `app.py`: Contains the API implementation.
- `predictive_analysis.ipynb`: Includes the ML model training and prediction logic with Random Forest and Optuna.
- `test.py`: Test script with sample data.
- `final_random_forest_model.pkl`: Pre-trained model.
- `Scaler.pkl`: Serialized scaler for data preprocessing.

## Testing
Use the requests module or similar tools to test the API endpoints locally. Ensure the server is running before making requests.

## Acknowledgments
- Dataset sources: Kaggle.
- Frameworks and libraries: numpy, pandas, FastAPI, scikit-learn, Optuna, requests.

---
Feel free to contribute or open issues for any questions or enhancements!
