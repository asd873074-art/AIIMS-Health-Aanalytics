import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Settings
num_patients = 3000000  
np.random.seed(42)

print("Generating Data... Thoda sabr rakho, 30 Lakh rows hain!")

# --- 1. Dim_Patients Table ---
patients_data = {
    'patient_id': np.arange(10001, 10001 + num_patients),
    'Name': np.random.choice(['Aditya', 'Rajesh', 'Suman', 'Anjali', 'Rohan', 'Priya', 'Amit', 'Vikram', 'Suresh', 'Meena'], num_patients),
    'Age': np.random.randint(1, 95, size=num_patients),
    'Gender': np.random.choice(['Male', 'Female', 'Other'], num_patients, p=[0.49, 0.49, 0.02]),
    'City': np.random.choice(['Ranchi', 'Patna', 'Jamshedpur', 'Delhi', 'Bhopal', 'Bhubaneswar', 'Raipur'], num_patients),
    'Income_Bracket': np.random.choice(['Low', 'Medium', 'High'], num_patients, p=[0.4, 0.4, 0.2])
}
df_patients = pd.DataFrame(patients_data)
df_patients.to_csv('Dim_Patients.csv', index=False)
print("1/4: Patients Table Ready.")

# --- 2. Dim_Visits Table ---
visits_data = {
    'visit_id': np.arange(50001, 50001 + num_patients),
    'patient_id': df_patients['patient_id'],
    'Visit_Date': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_patients)],
    'Hospital_Name': np.random.choice(['AIIMS Delhi', 'AIIMS Patna', 'RIMS Ranchi', 'AIIMS Bhopal', 'AIIMS Raipur'], num_patients),
    'Department': np.random.choice(['Cardiology', 'Neurology', 'General OPD', 'Emergency', 'Pediatrics'], num_patients)
}
df_visits = pd.DataFrame(visits_data)
df_visits.to_csv('Dim_Visits.csv', index=False)
print("2/4: Visits Table Ready.")

# --- 3. Fact_Medical_Records Table ---
medical_data = {
    'record_id': np.arange(90001, 90001 + num_patients),
    'patient_id': df_patients['patient_id'],
    'Blood_Pressure': np.random.randint(90, 180, num_patients),
    'Sugar_Level': np.random.randint(70, 250, num_patients),
    'Cholesterol': np.random.randint(150, 300, num_patients),
    'Diagnosis': np.random.choice(['Diabetes', 'Hypertension', 'Viral Fever', 'Heart Issue', 'Normal'], num_patients)
}
df_medical = pd.DataFrame(medical_data)
df_medical.to_csv('Fact_Medical_Records.csv', index=False)
print("3/4: Medical Records Ready.")

# --- 4. Fact_Billing Table ---
billing_data = {
    'bill_id': np.arange(20001, 20001 + num_patients),
    'patient_id': df_patients['patient_id'],
    'Total_Amount_INR': np.random.randint(1000, 200000, num_patients),
    'Insurance_Claimed': np.random.choice(['Yes', 'No'], num_patients, p=[0.6, 0.4]),
    'Payment_Method': np.random.choice(['Cash', 'UPI', 'Card', 'Insurance'], num_patients)
}
df_billing = pd.DataFrame(billing_data)
df_billing.to_csv('Fact_Billing.csv', index=False)
print("4/4: Billing Table Ready. Mission Successful!")      
