# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple, production-ready REST API using the FastAPI framework. Students will create CRUD endpoints, validate input with Pydantic models, and run the app locally using Uvicorn.

## 📝 Tasks

### 🛠️ Project Setup and Models

#### Description
Create a minimal FastAPI project structure and define Pydantic models for request and response validation.

#### Requirements
Completed project should:

- Include a working `starter-code.py` FastAPI app
- Define at least one Pydantic model for the API resource(s)
- Provide clear instructions to install dependencies and run the app locally


### 🛠️ Implement CRUD Endpoints

#### Description
Implement Create, Read, Update, and Delete endpoints for a simple resource (e.g., `Item`). Ensure endpoints return appropriate status codes and JSON responses.

#### Requirements
Completed project should:

- Implement `POST`, `GET`, `PUT`, and `DELETE` endpoints for the resource
- Validate incoming data using Pydantic models
- Return meaningful HTTP status codes for success and error cases
- Handle basic in-memory storage for demo purposes (no DB required)


### 🛠️ Run and Test Locally

#### Description
Provide steps to run the server and example `curl` or HTTP client commands students can use to test the API.

#### Requirements
Completed project should:

- Include `requirements.txt` listing `fastapi` and `uvicorn`
- Start with `uvicorn starter-code:app --reload` and respond to requests
- Contain at least three example `curl` commands demonstrating create, read, and delete
