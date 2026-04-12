import joblib

def load_model():
    return joblib.load("models/model.pkl")

def predict(model, input_data):
    result = model.predict(input_data)

    if result[0] != 0:
        return "THREAT"
    else:
        return "NORMAL"