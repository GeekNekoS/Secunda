![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)&nbsp;

## *SECUNDA*
Python Developer's Test Assignment
<br /> <br />


# Navigation
 - [Setting up a project](#setting_up_a_project)
 - [Project structure](#project_structure)
<br /> <br />


<a name="setting_up_a_project"></a> 
## Setting up a project
1. Select the Python version: 3.11 (Work through the `Linux` console or `WSL`)
2. Fill in the environment variables in `.env`. Example - `.env.example`
3. Make sure that Docker is installed on your device
4. `docker-compose up -d`
5. Create a migration `alembic -c api/alembic.ini revision --autogenerate -m "Create all models"`
6. Apply Migration `alembic -c api/alembic.ini upgrade head`
<br /> <br />


<a name="project_structure"></a> 
# Project structure
    Secunda
    ├── api/   
    │   ├── alembic/
    │   │   ├── versions/
    │   │   ├── env.py
    │   │   └── script.py.mako   
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
    │   ├── __init__.py
    │   ├── alembic.ini
    │   ├── app.py
    │   ├── config.py
    │   └── main.py
    ├── .env
    ├── .env.example
    ├── .gitignore
    ├── docker-compose.yml
    ├── README.md                               # Project documentation
    ├── gen_test_data.py
    ├── requirements.txt
    └── Secunda.drawio.png                      # The structure of the Postgres database
<br /> <br />
