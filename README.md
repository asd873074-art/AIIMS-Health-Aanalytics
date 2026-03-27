# 🏥 AIIMS Health Analytics: End-to-End Data Pipeline

## 📌 Overview
This project simulates a real-world healthcare analytics system using synthetic data of over 3 million patients. It demonstrates a complete data pipeline from data generation to analysis and prediction.

---

## 🎯 Objective
To build an end-to-end data analytics pipeline including data generation, data cleaning, exploratory data analysis (EDA), and machine learning.

---

## ⚙️ Project Workflow

### 1. Data Generation
- Generated large-scale dataset (3M+ records) using Python
- Created multiple tables:
  - Dim_Patients
  - Dim_Visits
  - Fact_Medical_Records
  - Fact_Billing

### 2. Data Storage
- Stored data in MySQL database

### 3. Data Cleaning
- Loaded data from SQL into Python
- Handled missing values
- Standardized categorical fields (Gender, City)
- Converted date formats

### 4. Exploratory Data Analysis (EDA)
- Performed analysis using Jupyter Notebook
- Identified patterns in patient visits, billing, and diagnoses

### 5. Machine Learning
- Applied Polynomial Regression to predict future patient trends

---

## 🛠️ Tools & Technologies
- Python (Pandas, NumPy)
- MySQL
- Jupyter Notebook
- Power BI (Planned)

---

## 📂 Project Structure
- scripts/ → Data generation & cleaning scripts  
- notebooks/ → EDA and ML notebook  

---

## 🚀 Key Highlights
- Handled large dataset (3 million+ records)
- Built complete end-to-end data pipeline
- Real-world healthcare simulation

---

## 🔮 Future Work
- Build interactive dashboard using Power BI
- Visualize patient trends and hospital performance

---

## 📌 Note
Dataset is not uploaded due to large size. It can be generated using the provided scripts.

---

## 👨‍💻 Author
- Aditya (NIT Jamshedpur)
