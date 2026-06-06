# 📘 Assignment: Secure REST APIs with FastAPI and SQLite

## 🎯 Objective

Build a secure, persistent REST API using FastAPI and SQLite. Students will learn how to store data in a database, validate requests with Pydantic, and protect write operations with a simple API key.

## 📝 Tasks

### 🛠️	Create SQLite-powered API endpoints

#### Description
Implement a FastAPI application that stores items in a SQLite database. The API should support CRUD actions and use Pydantic models for request validation.

#### Requirements
Completed project should:

- Use SQLite for item persistence
- Expose RESTful endpoints for:
  - `GET /` — health check
  - `GET /items` — list all items
  - `GET /items/{item_id}` — retrieve one item
  - `POST /items` — create an item
  - `PUT /items/{item_id}` — update an item
  - `DELETE /items/{item_id}` — delete an item
- Validate request bodies with Pydantic models
- Return proper HTTP status codes
- Handle missing items with a JSON 404 error
- Include inline instructions for running locally

Example response:

```
GET /items/1
Response 200
{
  "id": 1,
  "name": "Notebook",
  "description": "A school notebook",
  "price": 4.50
}
```

### 🛠️	Add simple API security

#### Description
Add a basic authorization layer so that only requests with a valid API key can create, update, or delete items.

#### Requirements
Completed project should:

- Require an API key header such as `X-API-Key` for write operations
- Reject unauthorized requests with a JSON 401 response
- Allow read-only endpoints to remain public
- Document the expected API key in the README or code comments

### 🛠️	Optional Enhancements

#### Description
Extend the API to improve usability, maintainability, or developer experience.

#### Requirements
Completed project may include any of the following enhancements:

- Add query parameters for filtering or sorting `GET /items`
- Use SQLAlchemy or another ORM instead of raw SQLite queries
- Add automated API tests with `pytest` and `httpx`
- Implement pagination or search for item lists
- Use environment variables for the API key and database path
