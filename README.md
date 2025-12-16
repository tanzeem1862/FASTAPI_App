# FastAPI Assignment

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn app.main:app --reload
```

3. Access the application:
- API: http://127.0.0.1:8000
- Documentation: http://127.0.0.1:8000/docs
- Admin Dashboard: http://127.0.0.1:8000/admin

## API Endpoints

### 1. GET /hello
Returns a hello message.

**Response:**
```json
{
  "message": "Hello FastAPI!"
}
```

### 2. POST /users
Create a new user with validation.

**Request Body:**
```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

**Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "name": "Alice",
    "email": "alice@example.com"
  }
}
```

### 3. GET /users
Fetch all users from the database.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
]
```

## Admin Dashboard

Access the admin dashboard at http://127.0.0.1:8000/admin to manage products:
- Create products
- View all products
- Update product details
- Delete products

Note: Products are NOT exposed via any REST API endpoints.

## Validation Rules

- Name must not be empty
- Email must contain @ symbol

## Database

The application uses SQLite database (app.db) with two tables:
1. users (id, name, email)
2. product (id, name, price, stock)
"""# ============================================
"""
# FastAPI Assignment

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn app.main:app --reload
```

3. Access the application:
- API: http://127.0.0.1:8000
- Documentation: http://127.0.0.1:8000/docs
- Admin Dashboard: http://127.0.0.1:8000/admin

## API Endpoints

### 1. GET /hello
Returns a hello message.

**Response:**
```json
{
  "message": "Hello FastAPI!"
}
```

### 2. POST /users
Create a new user with validation.

**Request Body:**
```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

**Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "name": "Alice",
    "email": "alice@example.com"
  }
}
```

### 3. GET /users
Fetch all users from the database.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
]
```

## Admin Dashboard

Access the admin dashboard at http://127.0.0.1:8000/admin to manage products:
- Create products
- View all products
- Update product details
- Delete products

Note: Products are NOT exposed via any REST API endpoints.

## Validation Rules

- Name must not be empty
- Email must contain @ symbol

## Database

The application uses SQLite database (app.db) with two tables:
1. users (id, name, email)
2. product (id, name, price, stock)
"""