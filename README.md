# Quart API

A Python-based asynchronous REST API built with [Quart](https://pgjones.gitlab.io/quart/), [SQLAlchemy (async)](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html), and [PostgreSQL], using [Poetry](https://python-poetry.org/) for dependency management.

## 🚀 Features

- Fast async API with Quart
- PostgreSQL + SQLAlchemy (async ORM)
- JWT authentication with `quart-jwt-extended`
- Fully typed models
- Alembic for migrations

---

## 🛠️ Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)
- PostgreSQL database

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/engrmarkk/quart-api.git
cd quart-api
````

### 2. Install dependencies

```bash
poetry install
```

### 3. Create `.env`

```bash
touch .env
```

Edit `.env` and set your database credentials or JWT secret, e.g.:

```
DB_URI=postgresql+asyncpg://username:password@localhost:5432/quart-api # or your external db (but +asyncpg: should be present in the uri)
SECRET_KEY=supersecretkey
```

---

## 🗃️ Database Setup

### Create the PostgreSQL database

```sql
CREATE DATABASE quart_api;
```

### Run migrations

```bash
poetry run alembic upgrade head
```

---

## 🔐 JWT Auth (Optional Setup)

Ensure you're using `quart-jwt-extended`.
Poetry handles this if you ran `poetry install`.

---

## ▶️ Running the Server

```bash
chmod u+x run_it.sh # to give the file permission the first time only
./run_it.sh
```

This will start the API on [http://localhost:5000](http://localhost:5000).

---

## 🧪 Example Endpoints

| Method | Path                | Description               |
| ------ | ---------------     | ------------------------- |
| `POST` | `/api/v1/authlogin` | Get JWT token             |
| `GET`  | `/api/v1/users/me`  | Auth route (JWT required) |

---

## 🧰 Useful Commands

| Command                           | Purpose                   |
| --------------------------------- | ------------------------- |
| `poetry install`                  | Install dependencies      |
| `eval $(poetry env activate)`     | Enter virtual environment |
| `poetry add package-name`         | Add a new package         |
| `poetry run alembic revision`     | Create new DB migration   |
| `poetry run alembic upgrade head` | Apply migrations          |
