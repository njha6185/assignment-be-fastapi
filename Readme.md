# Requirement

- Python 3.13.5
- install docker desktop (For postgres db docker containerisation)

# Setps to SetUp

- unzip or git checkout project
- add this in .env file DATABASE_URL=postgresql://test:test@localhost:5432/test
- python -m venv .venv
- .venv/Scripts/Activate.ps1 (For Windows)
- source .venv/bin/activate (For Mac/Linux)
- python -m pip install --upgrade pip
- python install -r requirements.txt
- docker-compose up

# To Run Application

- uvicorn app.main:app --reload

Note: When application server starts it automatically creates an Employe table and insert some dummy data into the table in public Schema
Consideration: It is assumed that status filter is multi select and rest is string
Also Assuming that org_id is being configured to show columns differently and hence here created a hardcoded file and added condition accordingly

# Swagger Docs

- http://localhost:8000/docs

# Api Documentation

- http://localhost:8000/redoc
