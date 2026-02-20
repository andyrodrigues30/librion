# Librion
>An open-source, self-hosted library management system designed for small to medium libraries.

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

## Installation
### Prerequisites
- Docker & Docker Compose installed
- Git installed

### Steps
1. Clone the repository:
```bash
git clone git@github.com:andyrodrigues30/librion.git

cd librion
````

2. Copy the example environment file and update the `.env` file with your database credentials and secret keys.
```bash
cp .env.example .env
```

3. Start the application:
```bash
docker-compose up -d
```

4. Access the application:
	- Frontend: `http://localhost:7811`
	- API: `http://localhost:7815/`

## Usage
- Add books, authors, and categories through the frontend.
- Register library members and manage loans.
- Use the dashboard to view analytics and overdue statistics.
- Access API endpoints for automation or integration with other systems.

## API Documentation
The FastAPI backend provides auto-generated Swagger documentation.
- Visit: `http://localhost:7815/docs`

## Tech Stack
**Backend:**
- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework with automatic API docs
- [Pydantic](https://pydantic-docs.helpmanual.io/) – Data validation
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for PostgreSQL
- [Alembic](https://alembic.sqlalchemy.org/) – Database migrations

**Database:**  
- [PostgreSQL](https://www.postgresql.org/) – Relational database

**Frontend:**  
- [Next.js](https://nextjs.org/) (React)
- [TypeScript](https://www.typescriptlang.org/)
- [TailwindCSS](https://tailwindcss.com/)

**Deployment:**
- Docker & Docker Compose for containerized setup

## License
This project is licensed under the **GPL-3.0 License**. See the LICENSE file for details.

## Future Enhancements
- Barcode/QR code integration for books
- Multi-library support
- Analytics Dashboard: Monitor most borrowed books, active borrowers, and overdue statistics with charts and graphs
- Mobile-friendly PWA or mobile version
