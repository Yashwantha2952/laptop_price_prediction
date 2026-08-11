import joblib


def load_model(path):
    return joblib.load(path)


def predict_price(model, data):
    prediction = model.predict(data)

    return prediction[0]