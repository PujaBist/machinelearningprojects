import os
import pickle
import numpy as np
import pandas as pd

MODEL_PATH = os.path.join("artifacts", "model.pkl")
PREPROCESSOR_PATH = os.path.join("artifacts", "preprocessor.pkl")

def load_model_and_preprocessor():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(PREPROCESSOR_PATH, "rb") as f:
        preprocessor = pickle.load(f)

    return model, preprocessor

def make_prediction(model, preprocessor, input_data: dict):
    # Convert input dict to DataFrame for preprocessing
    input_df = pd.DataFrame([input_data])

    # Preprocess the input data
    input_transformed = preprocessor.transform(input_df)

    # Predict using the model
    prediction = model.predict(input_transformed)

    return prediction[0]
