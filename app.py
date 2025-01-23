import flask
from flask import request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle  
from sklearn.preprocessing import StandardScaler

with open('final_random_forest_model.pkl', 'rb') as f: 
    best_model = pickle.load(f)

with open('Scaler.pkl', 'rb') as f: 
    Scaler = pickle.load(f)

app = flask.Flask(__name__)

@app.route('/predict_defect_status', methods=['POST'])
def predict_defect_status():
  try:
    # Get input data from the request
    data = request.get_json()

    # Extracting input features
    supplier_quality = data.get('SupplierQuality')
    defect_rate = data.get('DefectRate')
    quality_score = data.get('QualityScore')
    maintenance_hours = data.get('MaintenanceHours')
    downtime_percentage = data.get('DowntimePercentage')
    safety_incidents = data.get('SafetyIncidents')
    energy_consumption = data.get('EnergyConsumption')

    if any(value is None for value in [supplier_quality, defect_rate, quality_score, maintenance_hours, downtime_percentage, safety_incidents, energy_consumption]):
        return jsonify({'error': 'Missing input values'}), 400

    
    X_new = [[supplier_quality, defect_rate, quality_score, maintenance_hours, downtime_percentage, safety_incidents, energy_consumption]]
    X_new = Scaler.transform(X_new)
    prediction = best_model.predict(X_new)[0]
    confidence = best_model.predict_proba(X_new)[0][prediction]  
    
    response = {
        'DefectStatus': int(prediction),
        'ConfidenceScore': float(confidence)
    }

    return jsonify(response)
  except Exception as e:
        app.logger.error(f"An error occurred: {e}") 
        return jsonify({'error': 'An internal server error occurred.'}), 500 
      

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug = True)  