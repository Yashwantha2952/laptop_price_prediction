# Laptop Price Prediction

## 📌 Project Overview

This project predicts the price of a laptop based on its specifications using Machine Learning regression algorithms.

The project follows a modular ML project structure where preprocessing, model training, evaluation, model saving, and prediction are separated into reusable Python modules.

---

## 🎯 Objective

The main objective is to build a regression model that can predict laptop prices based on features such as:

- Company
- RAM
- Weight
- Processor
- Storage
- Display
- GPU
- Operating System
- Other laptop specifications

---

## 🗂️ Project Structure

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