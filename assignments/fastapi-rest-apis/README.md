# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API with FastAPI to manage a collection of items. You will create routes, define request and response models, and practice handling common API behaviors such as validation and errors.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Set up a FastAPI application and create a basic root endpoint so the server responds when it starts.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a `GET /` endpoint that returns a welcome message
- Run successfully with a local development server such as `uvicorn`

### 🛠️ Build CRUD Endpoints

#### Description
Add endpoints for a simple resource such as books, tasks, or notes. Use an in-memory list or dictionary to store the data.

#### Requirements
Completed program should:

- Implement endpoints to create, read, update, and delete items
- Support `GET` for listing all items and `GET /items/{id}` for one item
- Return JSON responses for each endpoint
- Keep the data in memory for the duration of the program

### 🛠️ Add Validation and Error Handling

#### Description
Use Pydantic models to validate incoming requests and handle invalid or missing data with clear API responses.

#### Requirements
Completed program should:

- Define request and response models with Pydantic
- Reject invalid input with a useful error response
- Return `404 Not Found` when a requested item does not exist
- Include at least one example request in the README comments or code block

Example request:
```http
POST /items
Content-Type: application/json

{
  "title": "Learn FastAPI",
  "completed": false
}
```