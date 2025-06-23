# 📚 Import required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# 📌 Extract — Load Dataset
data = pd.read_csv(r"C:\Users\Lathika S\Downloads\manufacturing_defect_dataset.csv")

# 📊 Check first few records
print("First 5 records:\n", data.head())

# 📑 Check dataset info
print("\nDataset Info:")
print(data.info())

# 📌 Transform — Data Preprocessing

# 🎛️ Encode categorical columns (if any)
categorical_cols = data.select_dtypes(include=['object']).columns
print("\nCategorical Columns:", list(categorical_cols))

if 'DefectStatus' in categorical_cols:
    le = LabelEncoder()
    data['DefectStatus'] = le.fit_transform(data['DefectStatus'])

# 📈 Feature Scaling
X = data.drop('DefectStatus', axis=1)  # Features
y = data['DefectStatus']               # Target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# 📊 Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("\nTrain and Test split completed.")
print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

# 📌 Load — Save processed data
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("\nProcessed data saved successfully as CSV files.")
