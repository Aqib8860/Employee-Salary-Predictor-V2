# Salary Prediction API

Production-style Machine Learning API built with **FastAPI**.

The project serves a trained **Scikit-learn salary prediction pipeline** through a REST API. It demonstrates how a trained ML model can be persisted, loaded, validated, and exposed as a production-style API.

## Architecture

```text
Client
  |
  | HTTP POST /predict
  v
FastAPI
  |
  v
Pydantic Validation
  |
  v
Prediction Service
  |
  v
Saved Scikit-learn Pipeline
  |
  +-- Missing Value Imputation
  +-- Feature Scaling
  +-- One-Hot Encoding
  +-- Feature Selection
  +-- Linear Regression
  |
  v
Predicted Salary
```

## Project Structure

```text
Day34-2/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
│
├── models/
│   └── salary_prediction_pipeline.joblib
│
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Pydantic

## Machine Learning Pipeline

The trained model is not used as a standalone estimator. The complete preprocessing and prediction workflow is persisted as a single Scikit-learn pipeline.

```text
Raw Input
   |
   v
Missing Value Handling
   |
   v
Numerical Feature Scaling
   |
   v
Categorical Encoding
   |
   v
Feature Selection
   |
   v
Linear Regression
   |
   v
Salary Prediction
```

This ensures that the same preprocessing logic used during training is automatically applied during inference.

## Model Persistence

The trained pipeline is stored using Joblib:

```text
models/salary_prediction_pipeline.joblib
```

The application loads the model when the API starts.

```text
Application Startup
       |
       v
Load Joblib Pipeline
       |
       v
Keep Model in Memory
       |
       v
Handle Prediction Requests
```

The model is **not retrained for every API request**.

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Salary Prediction

```http
POST /predict
```

Request:

```json
{
  "age": 29,
  "experience": 4,
  "department": "Backend"
}
```

Response:

```json
{
  "predicted_salary": 55153.33333333334
}
```

## Input Validation

Request validation is handled using Pydantic.

| Field        | Type   | Validation          |
| ------------ | ------ | ------------------- |
| `age`        | float  | 18–70               |
| `experience` | float  | 0–50                |
| `department` | string | Minimum 1 character |

Invalid input is rejected before reaching the ML prediction layer.

Example:

```json
{
  "age": -10,
  "experience": -5,
  "department": ""
}
```

The API returns a validation error instead of sending invalid data to the model.

## Unknown Categories

The preprocessing pipeline uses:

```python
OneHotEncoder(handle_unknown="ignore")
```

This allows the API to safely receive a department that was not present during training.

For example:

```json
{
  "age": 29,
  "experience": 4,
  "department": "DevOps"
}
```

The API remains functional instead of failing because of an unseen categorical value.

## Error Handling

The API separates client-facing errors from internal application errors.

Internal prediction failures are logged server-side while the client receives a generic response:

```json
{
  "detail": "Prediction failed. Please try again later."
}
```

This prevents internal implementation details and stack traces from being exposed through the API.

## Dependency Management

Project dependencies are pinned in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

The project was also verified in a fresh virtual environment to ensure that the API and persisted model can run independently of the original development environment.

## Running the API

Clone or copy the project and install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

For development with automatic reload:

```bash
uvicorn app.main:app --reload
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

## Example Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "age": 29,
  "experience": 4,
  "department": "Backend"
}'
```

Example response:

```json
{
  "predicted_salary": 55153.33333333334
}
```

## Design Principles

The project follows a simple separation of responsibilities:

```text
main.py
  |
  +-- API endpoints
  +-- HTTP handling
  +-- Error handling

schemas.py
  |
  +-- Request validation
  +-- Response validation

model.py
  |
  +-- Model loading
  +-- Prediction logic

models/
  |
  +-- Trained ML artifact
```

This keeps FastAPI-specific logic separate from the machine-learning layer.

## Key Engineering Concepts

This project demonstrates:

* End-to-end ML pipeline
* Data preprocessing
* Missing-value handling
* Numerical feature scaling
* Categorical feature encoding
* Feature selection
* Linear Regression
* Model persistence with Joblib
* REST API model serving
* FastAPI
* Pydantic validation
* Structured API responses
* Error handling
* Server-side logging
* Dependency management
* Reproducible environment setup
* Separation of API and ML logic
* Handling unseen categorical values

## Project Workflow

```text
Training Data
     |
     v
Data Preprocessing
     |
     v
Feature Engineering / Selection
     |
     v
Model Training
     |
     v
Complete Pipeline
     |
     v
Joblib Serialization
     |
     v
FastAPI Application
     |
     v
Request Validation
     |
     v
ML Prediction
     |
     v
JSON Response
```

## Status

**Completed**

The API has been verified with:

* Valid prediction requests
* Invalid input validation
* Unknown categorical values
* API health check
* Persisted model loading
* Fresh virtual environment
* Reproducible dependency installation

## Future Improvements

Potential production extensions:

* Docker containerization
* Environment-based configuration
* Authentication and authorization
* Request/response logging
* Model versioning
* Model monitoring
* Prediction monitoring
* Automated tests
* CI/CD pipeline
* Cloud deployment
* Database-backed prediction history
* Model retraining pipeline
