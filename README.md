# Data-Pipeline-automating-ETL-process
📄 A working ETL Data Pipeline in Python  📂 Cleaned, transformed, split, and saved datasets  📌 Code compatible with future deep learning/image classification models

📦 Data Pipeline — Manufacturing Defect Detection
📌 What is a Data Pipeline?
A Data Pipeline is an automated workflow that moves raw data through a sequence of steps:

Extract → Collect or load raw data

Transform → Clean, preprocess, and format the data

Load → Store the processed data for analysis or modeling

ETL pipelines are essential in Data Science projects to prepare clean, usable data for AI and analytics applications.

📊 Dataset Used:
Manufacturing Defect Detection Dataset

✅ Columns include:

ProductionVolume, ProductionCost, SupplierQuality, DeliveryDelay, DefectRate, etc.

DefectStatus — Categorical target (defective or not)

No missing values were present initially — but handled missing value strategy was added for completeness.

📌 Pipeline Stages in this Project:
📍 Extract:
Imported required libraries: pandas, numpy, sklearn

Loaded dataset using pd.read_csv()

Inspected the first few records and data info (datatypes, non-null counts)

📍 Transform:
Handled Missing Values

Checked with data.isnull().sum()

Applied data.fillna(data.mean(), inplace=True) to impute numerical missing values (if any)

Encoded Categorical Variables

Detected object-type columns using data.select_dtypes(include=['object'])

Applied LabelEncoder from sklearn to convert categorical data to numeric

Feature Scaling

Separated features (X) and target (y)

Used StandardScaler to normalize feature values

Converted scaled values back to a DataFrame

Split Dataset

Applied train_test_split() (80% train, 20% test split)

📍 Load:
Saved the processed train and test datasets as CSV files:

X_train.csv, X_test.csv, y_train.csv, y_test.csv

📌 How It’s Implemented:
A clean, step-by-step Python notebook (.ipynb) / script (.py)

Used Pandas for data handling, scikit-learn for preprocessing

Followed a modular ETL structure to automate preprocessing

Prepared processed data ready for future Deep Learning (Task-2) or ML model deployment (Task-3)

✅ Deliverable:
📄 A working ETL Data Pipeline in Python

📂 Cleaned, transformed, split, and saved datasets

📌 Code compatible with future deep learning/image classification models
