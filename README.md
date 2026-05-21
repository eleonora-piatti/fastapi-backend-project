## FastAPI-backend-project
Backend REST API built with FastAPI and SQLAlchemy, designed to manage users with full CRUD operations.
The project focuses on clean architecture, data validation and proper database handling using modern Python backend practices.

## Tech stack
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```
app/
├── core/       # Configuration
├── db/         # Database engine and session
├── models/     # ORM models
├── schemas/    # Pydantic schemas (validation layer)
├── routers/    # API routes
└── main.py     # Application entry point
```


## Features

- Create, read, update, delete users (CRUD)
- Input validation using Pydantic
- Db interaction via SQLAlchemy ORM
- Dependency injection for db sessions
- Error handling with proper HTTP status codes


## Installation
```
bash
git clone <https://github.com/eleonora-piatti/fastapi-backend-project>
cd fastapi-backend-project
python -m venv venv
source venv/bin/activate # windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run the app
```
bash
python -m uvicorn app.main:app --reload
```

## Learning goals

- Better understand application architecture with FastAPI
- Learn ORM concepts with SQLAlchemy
- Implement request validation and schema separation
- Build a scalable and modular python backend


