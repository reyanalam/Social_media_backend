# Social Media API

A modern, secure, and scalable social media API built with FastAPI and PostgreSQL. This project provides a robust backend for social media applications with features like user authentication, post management, and more.

## Features

-  Secure user authentication with JWT tokens
-  User management (registration, login, profile)
-  Post creation and management
-  Database migrations with Alembic
-  Password hashing with bcrypt
-  SQLAlchemy ORM for database operations
-  FastAPI for high-performance API endpoints
-  PostgreSQL database

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: bcrypt
- **Database Migrations**: Alembic
- **Python Version**: 3.8+

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd socialmedia
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r myapp/requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run database migrations:
```bash
alembic upgrade head
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn myapp.main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
socialmedia/
├── myapp/
│   ├── routers/         # API route handlers
│   ├── main.py         # Application entry point
│   ├── models.py       # Database models
│   ├── schemas.py      # Pydantic schemas
│   ├── database.py     # Database configuration
│   ├── oauth2.py       # Authentication logic
│   ├── config.py       # Environment configuration
│   └── utils.py        # Utility functions
├── alembic/            # Database migration files
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## API Endpoints

The API provides the following main endpoints:

- `/users` - User management
- `/posts` - Post management
- `/auth` - Authentication endpoints

For detailed API documentation, visit the Swagger UI at `/docs` when the server is running.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contact

Email: reyanalam115@gmail.com
Linkedin: https://www.linkedin.com/in/reyanalam/
