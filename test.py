import requests

url = 'http://127.0.0.1:5000/predict_defect_status'

# Chnage the values accordingly .
data = {
    "SupplierQuality":86.648534	 ,
    "DefectRate": 3.121492,
    "QualityScore": 63.463494	,
    "MaintenanceHours":9  ,
    "DowntimePercentage": 0.052343,
    "SafetyIncidents":1 ,
    "EnergyConsumption": 2419.616785,	
}
# headers = {'Content-Type': 'application/json'}

response = requests.post(url,json=data)
if response.status_code == 200:
    response = response.json()
    defecet_status = "NO"
    if response['DefectStatus'] == 1:
         defecet_status = "YES"
    print("Defect Status is :" , defecet_status)
    print("Confidence score is : " , response['ConfidenceScore'])
else:
    print(f"Error: {response.status_code}")