# Librion

> An open-source, self-hosted library management system designed for small to medium libraries.

It provides an intuitive web interface and a powerful API for managing books, borrowers, loans, reservations, and library analytics.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Books Management:** Add, edit, delete, and categorize books; track availability.
- **Borrowers Management:** Add members, track loans, overdue books, and fines.
- **Loan & Reservation System:** Issue books, reserve unavailable books, automatic overdue notifications.
- **Search & Filtering:** Search by title, author, genre, or ISBN; filter by availability and category.
- **User Roles:** Admin, Librarian, and Member access levels.
- **REST API:** CRUD operations for books, borrowers, loans, and reservations with Swagger docs.

## Setup

### Prerequisites

- Docker (>= 20.x)
- Docker Compose (>= 2.x)
- Git (to clone the repository)

### Clone the repository and set up environment

```bash
# Clone the repository
git clone git@github.com:andyrodrigues30/librion.git
cd librion

# Copy example environment variables
cp .env.example .env

# Edit .env if needed
nano .env

Example .env contents:

POSTGRES_DB=librionDB
POSTGRES_USER=developer
POSTGRES_PASSWORD=YourPasswordHere
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

*Make sure the database credentials match your setup.*

### API & Frontend Dockerfiles

#### API

- Python 3.11
- Uvicorn runs FastAPI
- Migrations in production are run automatically

#### Frontend

- Node 20 (bullseye)
- Development mode: live reload (npm run dev)
- Production mode: build + start (npm run start)

### Running the project

#### Development

```bash
# Start all services in dev mode
docker compose up -d

# Stop containers
docker compose down
```

- Hot reload enabled for both API and frontend
- Code changes in `api/` and `frontend/` will reflect automatically

#### Production

```bash
# start all services in production mode
docker compose -f docker-compose.yml up -d

# migrations are run automatically on container startup
# check logs
docker compose logs -f
```

- Alembic migrations run automatically before API starts
- Live reload is disabled
- Uses built images, no volume mounts

## Accessing in the browser/tools

| Service  | Container Name | Container Port | Host Port |
| -------- | -------------- | -------------- | --------- |
| Postgres | db             | 5432           | 5678      |
| FastAPI  | api            | 8000           | 7815      |
| Next.js  | frontend       | 3000           | 7811      |

- Frontend: `http://localhost:7811`
- API: `http://localhost:7815`
- Swagger Docs: `http://localhost:7815/docs`
- Database: `localhost:5678`

### Database Migrations (Alembic)

#### Generate a new migration after model changes

```bash
docker compose exec librion-api alembic revision --autogenerate -m "describe change"

sudo chown -R user:user db/migrations

docker compose exec librion-api alembic upgrade head
```

Example: `add genre table`

#### Apply migrations

- Dev (manual):

```bash
docker compose exec librion-api alembic upgrade head
```

- Production (automatic via command in compose)

#### Rollback a migration

```bash
docker compose exec librion-api alembic downgrade -1
```

## Usage

- Add books, authors, and categories through the frontend.
- Register library members and manage loans.
- Use the dashboard to view analytics and overdue statistics.
- Access API endpoints for automation or integration with other systems.

## Tech Stack

### Backend

- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework with automatic API docs
- [Pydantic](https://pydantic-docs.helpmanual.io/) – Data validation
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for PostgreSQL
- [Alembic](https://alembic.sqlalchemy.org/) – Database migrations

### Database

- [PostgreSQL](https://www.postgresql.org/) – Relational database

### Frontend

- [Next.js](https://nextjs.org/) (React)
- [TypeScript](https://www.typescriptlang.org/)
- [TailwindCSS](https://tailwindcss.com/)

### Deployment

- Docker & Docker Compose for containerized setup

## License

GPL-3.0
