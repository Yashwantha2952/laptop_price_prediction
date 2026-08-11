# 💻 Laptop Price Prediction

## 📌 Project Overview

This project predicts the price of a laptop based on its specifications using Machine Learning regression algorithms.

The project is structured as a modular Machine Learning repository where data preprocessing, model training, evaluation, model saving, and prediction are separated into reusable Python modules.

The goal is not only to build an accurate regression model, but also to follow a proper **Machine Learning project structure** that can later be extended toward API deployment and production.

---

## 🎯 Objective

The main objective is to predict laptop prices using available laptop specifications such as:

* Company
* RAM
* Weight
* Processor
* Storage
* Display
* GPU
* Operating System
* Other laptop specifications

This is a **supervised learning regression problem** because the target variable, `Price`, is continuous.

---

## 🔄 Machine Learning Workflow

```text
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Train/Test Split
     ↓
Data Preprocessing
     ↓
Numerical + Categorical Pipelines
     ↓
ColumnTransformer
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Best Model Selection
     ↓
Model Saving
     ↓
Prediction
```

---

## 🏗️ Project Architecture

The project follows a modular architecture:

```text
laptop_price_prediction/
│
├── Data/
│   ├── Raw/
│   │   └── laptop_data (1).csv
│   └── Processed/
│
├── Notebooks/
│   └── Experimental.ipynb
│
├── src/
│   ├── __init__.py
│   ├── Preprocessing.py
│   ├── model.py
│   ├── evaluation.py
│   ├── save_model.py
│   └── predict.py
│
├── models/
│   └── laptop_price_model.pkl
│
│
├── requirements.txt
└── README.md
```

### Why this structure?

The notebook is used mainly for **experimentation and analysis**, while reusable Machine Learning logic is maintained inside `src/`.

This avoids copying the same preprocessing and model code across multiple notebooks.

---

## ⚙️ Data Preprocessing

The preprocessing workflow is implemented in:

```text
src/Preprocessing.py
```

The preprocessing function performs:

### 1. Feature and Target Separation

```python
X = data.drop("Price", axis=1)
y = data["Price"]
```

### 2. Train/Test Split

The dataset is split into training and testing data before fitting preprocessing transformations.

### 3. Numerical Features

Numerical columns use:

* Median imputation
* StandardScaler

```text
Numerical Features
       ↓
Median Imputation
       ↓
StandardScaler
```

### 4. Categorical Features

Categorical columns use:

* Most-frequent imputation
* One-Hot Encoding
* `handle_unknown="ignore"`

```text
Categorical Features
       ↓
Most Frequent Imputation
       ↓
One-Hot Encoding
```

### 5. ColumnTransformer

The numerical and categorical pipelines are combined using `ColumnTransformer`.

---

## 🤖 Machine Learning Models

The following regression algorithms are evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

Model training is implemented in:

```text
src/model.py
```

Each model is combined with the preprocessing pipeline using Scikit-learn's `Pipeline`.

This ensures that the same preprocessing steps are consistently applied during both training and prediction.

---

## 📊 Model Evaluation

Model evaluation is implemented in:

```text
src/evaluation.py
```

The following metrics are used:

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted prices.

### RMSE — Root Mean Squared Error

Measures prediction error while giving greater weight to larger errors.

### R² Score

Measures how well the model explains the variation in the target variable.

The models are compared using these metrics, and the best-performing model is selected.

---

## 💾 Model Saving

The selected trained pipeline is saved using `joblib`.

```text
models/
└── laptop_price_model.pkl
```

The saved file contains the complete trained pipeline, including:

```text
Preprocessing
     +
Machine Learning Model
```

This means the same preprocessing logic does not need to be manually recreated when making predictions.

---

## 🔮 Prediction

Prediction functionality is implemented in:

```text
src/predict.py
```

The saved model can be loaded and used to predict the price of new laptop data.

```text
New Laptop Data
       ↓
Saved Pipeline
       ↓
Preprocessing
       ↓
Trained Model
       ↓
Predicted Price
```

---


## 📈 Results

Model performance is evaluated using:

| Model             | MAE | RMSE | R² Score |
| ----------------- | --: | ---: | -------: |
| Linear Regression | 0.21|  0.27|      0.80|
| Decision Tree     | 0.20|  0.28|      0.79|
| Random Forest     | 0.16|  0.21|      0.88|
| XGBoost           | 0.16|  0.21|      0.87|


---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate into the project:

```bash
cd laptop_price_prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Open the experimental notebook:

```text
Notebooks/Experimental.ipynb
```

The notebook can be used to:

1. Load the dataset
2. Perform exploratory analysis
3. Run preprocessing
4. Train models
5. Evaluate models
6. Select the best model
7. Save the trained model
8. Test predictions

---

## 🔑 Key Design Decisions

### Modular Code

Reusable ML logic is separated from the experimentation notebook.

### Pipeline-Based Preprocessing

Preprocessing and model training are connected through Scikit-learn pipelines.

### Data Leakage Prevention

Preprocessing is fitted using training data and then applied to test data through the pipeline.

### Reusable Model

The complete trained pipeline is saved as a `.pkl` file so it can be loaded later without retraining.

### Reproducibility

Random states are defined where applicable to make experiments more consistent.

---

## 🧠 What This Project Demonstrates

This project demonstrates practical understanding of:

* Supervised Learning
* Regression
* Exploratory Data Analysis
* Train/Test Split
* Missing Value Imputation
* Feature Scaling
* One-Hot Encoding
* ColumnTransformer
* Scikit-learn Pipeline
* Multiple Regression Algorithms
* Model Evaluation
* Model Selection
* Model Serialization
* Modular Python Project Structure

---

## 🚀 Future Improvements

The project can be extended toward a production Machine Learning system by adding:

* Hyperparameter tuning
* Automated unit testing
* Better experiment tracking
* MLflow
* FastAPI
* Docker
* CI/CD
* Cloud deployment
* Monitoring
* User interface for predictions

Possible future architecture:

```text
Machine Learning Model
        ↓
FastAPI
        ↓
Docker
        ↓
Cloud Deployment
        ↓
Prediction API
```

---

## 👨‍💻 Author

**Yashwantha Gowda S**

M.Tech — Data Science & Artificial Intelligence

---

## ⭐ Project Goal

This project is part of a practical journey toward building **production-ready Machine Learning systems**, moving from experimentation in notebooks to modular code, model serialization, APIs, containerization, and deployment.
