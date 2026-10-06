from pydantic import BaseModel, Field


# ---------------------------------------------------------
# Request schema
#
# This defines exactly what the API expects from the client.
# ---------------------------------------------------------
class EmployeeData(BaseModel):

    # Employee age must be between 18 and 70.
    age: float = Field(
        ge=18,
        le=70,
    )

    # Experience cannot be negative.
    experience: float = Field(
        ge=0,
        le=50,
    )

    # Department must be provided as text.
    department: str = Field(
        min_length=1,
    )


# ---------------------------------------------------------
# Response schema
#
# This defines the structure of the API response.
# ---------------------------------------------------------
class SalaryPredictionResponse(BaseModel):

    predicted_salary: float