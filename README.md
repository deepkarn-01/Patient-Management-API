# Patient Management API

A beginner-friendly **Patient Management REST API** built with **Python, FastAPI, Pydantic, and JSON**. This project demonstrates how to build a CRUD-based backend API with data validation, automatic BMI calculation, patient health classification, sorting, and error handling.

## 🚀 Features

* Create new patient records
* View all patients
* View a specific patient by ID
* Update patient information
* Delete patient records
* Sort patients by:

  * Height
  * Weight
  * BMI
* Automatic BMI calculation
* Automatic BMI-based health verdict
* Request validation using Pydantic
* Path and query parameter validation
* HTTP exception handling
* JSON file-based data persistence
* Interactive API documentation provided by FastAPI

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Pydantic**
* **JSON**
* **Uvicorn**

## 📌 API Endpoints

| Method | Endpoint                | Description                             |
| ------ | ----------------------- | --------------------------------------- |
| GET    | `/`                     | API home                                |
| GET    | `/view`                 | View all patients                       |
| GET    | `/patient/{patient_id}` | Get patient by ID                       |
| GET    | `/sort`                 | Sort patients by height, weight, or BMI |
| POST   | `/create`               | Create a new patient                    |
| PUT    | `/edit/{patient_id}`    | Update patient information              |
| DELETE | `/delete/{patient_id}`  | Delete a patient                        |

## 🧮 BMI Calculation

The API automatically calculates BMI from the patient's height and weight:

```text
BMI = weight / height²
```

The calculated BMI is exposed as a computed field along with a corresponding health verdict.

## 📂 Project Structure

```text
patient-management-api/
│
├── main.py
├── patient.json
├── requirements.txt
└── README.md
```

## ▶️ Running the Project

Install the required dependencies:

```bash
pip install fastapi uvicorn pydantic
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI also automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## 🎯 Learning Objectives

This project was built to practice:

* REST API development
* FastAPI routing
* CRUD operations
* Pydantic models and validation
* Path and query parameters
* HTTP status codes and exceptions
* Computed fields
* JSON data storage
* Backend development fundamentals

## 🔮 Future Improvements

Possible improvements include:

* Replace JSON storage with PostgreSQL/MySQL
* Add authentication and authorization
* Add pagination
* Add search and filtering
* Add proper logging
* Add automated tests with Pytest
* Add Docker support
* Add a frontend dashboard
* Deploy the API to a cloud platform

---

**Built as a backend development learning project using FastAPI and Python.**
