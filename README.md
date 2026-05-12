# Django-Store-API

## What the project is

django-store-api is an project That includes features like CRUD operations, API endpoints, Register & login System so that any store can manage, update, add and delete products. This project makes business management easier, leading to less work.

## Tech stack used

Django, DRF: Django RestFramework, Python And PostgreSQL.
 

## How to set it up locally

1) install wsl in your system, go to cmd and type wsl --install 
2) Configure it's settings accordingly
3) install virtual environment in wsl & activate it
4) Clone repository with this command: git clone <repo_url>
5) install the dependencies via requirements.txt use: pip install -r requirements.txt
6) install vscode if don't have it.
7) in vscode, install thunder client or use postman
8) in wsl, type "python manage.py runserver" to run server locally.
9) use the api endpoints either in vscode or postman.
10) Register or login in the app first to use endpoints.

| Method | Endpoint | Auth Required | Description |
|--------|----------|--------------|-------------|
| GET    | /products/ | No | View all products |
| GET    | /products/<id>/ | No | View individual product by it's id |
| POST   | /products/ | Yes | Adds a product |
| PUT   | /products/<id>/ | Yes | Update product |
| DELETE    | /products/<id>/ | Yes | Deletes a product |


