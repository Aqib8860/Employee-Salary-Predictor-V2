import logging
from fastapi import FastAPI, HTTPException

from .model import predict_salary
from .schemas import EmployeeData, SalaryPredictionResponse



# ---------------------------------------------------------
# Application logger
# ---------------------------------------------------------
logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# Create FastAPI application
# ---------------------------------------------------------
app = FastAPI(
    title="Salary Prediction API",
    description="Production-style ML prediction API.",
    version="1.0.0",
)


# ---------------------------------------------------------
# Health-check endpoint
# ---------------------------------------------------------
@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }


# ---------------------------------------------------------
# Prediction endpoint
# ---------------------------------------------------------
@app.post(
    "/predict",
    response_model=SalaryPredictionResponse,
)
def predict(employee: EmployeeData):

    try:
        # Send validated data to the ML layer.
        predicted_salary = predict_salary(
            age=employee.age,
            experience=employee.experience,
            department=employee.department,
        )

        # Return prediction using the response schema.
        return SalaryPredictionResponse(
            predicted_salary=predicted_salary,
        )

    except Exception:
        # Full traceback server logs mein record hoga.
        logger.exception("Salary prediction failed")

        # Client ko internal implementation details nahi denge.
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again later.",
        )