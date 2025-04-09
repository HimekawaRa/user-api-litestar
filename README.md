# User API with Litestar

This project is a RESTful API for managing users, built using **Litestar 2.x**, **PostgreSQL**, and **Advanced Alchemy**.

## 🚀 Features
- Full CRUD operations for User model
- Swagger (OpenAPI) documentation
- PostgreSQL with SQLAlchemy ORM
- Asynchronous API
- Docker-based setup

## 🔧 Tech Stack
- **Backend:** Litestar 2.x
- **ORM:** Advanced-Alchemy (SQLAlchemy based)
- **DB:** PostgreSQL 15
- **Infra:** Docker, Docker Compose
- **Python version:** 3.12
- **Package Manager:** Poetry 1.8.3

## 📦 Installation & Run
```bash
git clone https://github.com/<your-username>/user-api-litestar.git
cd user-api-litestar
docker-compose up --build
litestar database upgrade
```

## 📘 API Endpoints
| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| POST   | /users           | Create user       |
| GET    | /users           | List users        |
| GET    | /users/{id}      | Retrieve user     |
| PUT    | /users/{id}      | Update user       |
| DELETE | /users/{id}      | Delete user       |

## 📑 API Docs
- [Swagger UI](http://localhost:8000/schema)

## 🧑 Author
Raul