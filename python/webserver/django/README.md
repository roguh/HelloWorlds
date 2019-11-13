read https://docs.djangoproject.com/en/2.2/intro/tutorial01/

to set this up, I ran:
pipenv install Django
pipenv run django-admin startproject hello_project
# something like mv hello_project/* .
pipenv run ./manage.py startapp hello_app

you run:

pipenv install
pipenv run ./manage.py runserver
