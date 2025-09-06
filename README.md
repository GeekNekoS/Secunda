![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-000000?style=flat)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker)

## *SECUNDA*
Python Developer's Test Assignment
<br /> <br />


## Architecture
[Client] → [Endpoints] → [Services] → [Repositories] → [Database]
<br /><br />


# Navigation
 - [Setting up a project](#setting_up_a_project)
 - [Setting up a project](#setting_up_a_project)
 - [API Documentation](#api_documentation)
 - [Project structure](#project_structure)
 - [Database Structure](#database_structure)
<br /> <br />


<a name="setting_up_a_project"></a> 
## Setting up a project
1. Select the Python version: 3.11 (Work through the `Linux` console or `WSL`)
2. Fill in the environment variables according to the `.env` variables template in the file `README.md` and `.env.example`
3. Make sure that Docker is installed on your device
4. `docker-compose up -d`
5. Create a migration `alembic -c api/alembic.ini revision --autogenerate -m "Create all models"`
6. Apply Migration `alembic -c api/alembic.ini upgrade head`
7. Generate test data: `python api/gen_test_data.py`
<br /> <br />


<a name="dotenv_variables"></a> 
# `.env` variables
| Variable               | Description                    | Example                                                |
|------------------------|--------------------------------| ------------------------------------------------------ |
| `POSTGRES_DB_PORT`     | Port for PostgreSQL            | `5432`                                                 |
| `POSTGRES_DB_NAME`     | Name of the database           | `secunda_db`                                           |
| `POSTGRES_DB_USER`     | PostgreSQL User                | `postgres`                                             |
| `POSTGRES_DB_PASSWORD` | PostgreSQL user's password     | `secret`                                               |
| `POSTGRES_DB_URL`      | Database connection URL        | `postgres://postgres:secret@localhost:5432/secunda_db` |
| `API_KEY`              | API key for endpoint requests  | `supersecretapikey`                                    |
<br /> <br />


<a name="api_documentation"></a> 
# API Documentation
Once the server is running, you can access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
<br /> <br />


<a name="project_structure"></a> 
# Project structure
    Secunda
    ├── api/   
    │   ├── alembic/
    │   │   ├── versions/
    │   │   ├── env.py
    │   │   └── script.py.mako   
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── config.py                      # Project configuration
    │   │   ├── db.py                          # Connecting to the database
    │   │   └── exceptions.py                  # Сustom exceptions (for example, EntityNotFound, DuplicateError...)
    │   ├── endpoints/
    │   │   ├── organizations.py
    │   │   ├── buildings.py
    │   │   ├── search.py
    │   │   └── __init__.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── activity.py
    │   │   ├── base.py
    │   │   ├── office.py
    │   │   ├── organization.py
    │   │   ├── organization_activity_assoc.py
    │   │   └── phone.py
    │   ├── repositories/                      # DAL, data access layer
    │   │   ├── __init__.py
    │   │   ├── activity_repo.py               # Queries to the organization table
    │   │   ├── office_repo.py                 # Access to offices/buildings
    │   │   └── organization_repo.py           # Working with types of activities
    │   ├── services/                          # Business logic of the application
    │   │   ├── __init__.py
    │   │   ├── organization_service.py        # Сombines calls from organization_repo, processes rules
    │   │   └── search_service.py              # Search logic (nested activities up to 3 levels, working with radius)
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   ├── test_activity_repo.py
    │   │   ├── test_office_repo.py
    │   │   └── test_organization_repo.py
    │   ├── __init__.py
    │   ├── alembic.ini
    │   ├── app.py
    │   ├── config.py
    │   ├── Dockerfile
    │   ├── main.py
    │   └── requirements-api.txt
    ├── .dockerignore
    ├── .env
    ├── .env.example
    ├── .gitignore
    ├── docker-compose.yml
    ├── pytest.ini
    ├── README.md                               # Project documentation
    └── Secunda.drawio.png                      # The structure of the Postgres database
<br /> <br />


<a name="database_structure"></a> 
# Database Structure
![Database Schema](Secunda.drawio.png)
<br /> <br />
