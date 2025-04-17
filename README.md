# recipes-api
A recipes api for CF built with Django and MySQL hosted on AWS 


## Getting started
- you can run this in docker if you are brave
- or create a virtual env and do it locally
- run this when you first clone project
- `python -m venv venv`  
- make sure (venv) is in terminal or run this
- `.\venv\Scripts\Activate.ps1`# 
- `pip install -r requirements.txt`

## Migrations
- create your model or make changes in models.py
- this generate the migration files in migrations
- `python manage.py makemigrations`
- this applies the migrations in that folder to the database
- `python manage.py migrate`

## Running the app
- `python manage.py runserver`

## Testing
- create tests in tests.py
- `python manage.py test`