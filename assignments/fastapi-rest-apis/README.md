# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple RESTful API using the FastAPI framework. Students will build endpoints, validate input, return JSON responses, and run the app locally.

## 📝 Tasks

### 🛠️	Build a Basic REST API

#### Description
Create a FastAPI application that exposes endpoints to create, read, update, and delete simple resources (e.g., items). The API should follow RESTful conventions and provide clear JSON responses and appropriate HTTP status codes.

#### Requirements
Completed project should:

- Include at least these endpoints:
  - `GET /` — health or welcome message
  - `GET /items/{item_id}` — return a single item
  - `GET /items` — return a list of items
  - `POST /items` — create a new item with request body validation
  - `PUT /items/{item_id}` or `PATCH /items/{item_id}` — update an item
  - `DELETE /items/{item_id}` — delete an item
- Use Pydantic models for request and response validation
- Return appropriate HTTP status codes (e.g., 200, 201, 404)
- Handle common errors and return JSON error messages
- Provide inline README instructions for running the app locally

Example response:

```
GET /items/1
Response 200
{
  "id": 1,
  "name": "Example",
  "price": 9.99
}
```

## 🛠️	Starter Code

A minimal FastAPI skeleton is provided in `starter-code.py` to help you get started. It includes example endpoints and models — modify or extend it as needed.

To run locally (recommended):

```
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

## 🛠️	Optional Enhancements

#### Description
Add features that improve the API, developer experience, or deployment readiness.

#### Requirements
Completed project may include any of the following enhancements:

- Persistence using an in-memory store, SQLite, or other DB
- Query parameters for filtering/sorting (`GET /items?min_price=...`)
- Pagination for list endpoints
- Authentication (API key or basic token) for write endpoints
- Automated tests using `pytest` and `httpx` or `requests`
