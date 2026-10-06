from pathlib import Path

import pandas as pd
from joblib import load


# ---------------------------------------------------------
# Project root directory.
#
# __file__ = app/model.py
# parent     = app/
# parent     = Day34-2/
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# Trained ML model ka complete path.
# ---------------------------------------------------------
MODEL_PATH = (
    BASE_DIR
    / "models"
    / "salary_prediction_pipeline.joblib"
)


# ---------------------------------------------------------
# Trained pipeline ko application start hone par
# ek baar load karte hain.
# ---------------------------------------------------------
model_pipeline = load(MODEL_PATH)


# ---------------------------------------------------------
# Prediction function
#
# Ye function sirf ML prediction handle karta hai.
# FastAPI ka code main.py mein rahega.
# ---------------------------------------------------------
def predict_salary(
    age: float,
    experience: float,
    department: str,
) -> float:

    # Model training ke same column names use kar rahe hain.
    input_data = pd.DataFrame(
        {
            "Age": [age],
            "Experience": [experience],
            "Department": [department],
        }
    )

    # Saved ML pipeline se prediction generate karo.
    prediction = model_pipeline.predict(
        input_data
    )

    # NumPy value ko normal Python float mein convert karo.
    return float(prediction[0])