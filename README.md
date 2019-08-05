# Django Rest Framework, VueJS with Quasar Boilerplate

### Pre-integrated third parties

- Djangosimplejwt : JWT library for django
- Djangorestswagger : automated documentation for django with swagger
- AmazonS3
- Flake8
- Postgresql
- Mailjet

### Backend install

- Install postgresql
- Create test database with the settings in settings.py
  - Connect to posgresql
  - `CREATE DATABASE test;`
  - `\c test;`
  - `CREATE USER test WITH PASSWORD 'test';`
  - `ALTER DATABASE test OWNER TO test`
  - `ALTER ROLE test SUPERUSER`
- `virtualenv env` and start your virtualenv
- `pip3 install -r requirements.txt` to install python dependencies
- `make migrate` to install database

### Useful Commands

- `make reset_db` to start the drop your current database and set up a new one
- `make fake_db` to populate your database with fake data
- `make runserver` to start the server
- `make shell` to start the console

### Running Tests

- Make sure your test file match `test*.py`
- Make sure your methods start with `test_`
- run `make tests`

### API Documentation

- run `make runserver`
- Go to `http://localhost:8000/docs/`
- Click on `authorize` and write `Bearer someusertoken` to access documentation for routes protected by jwt

### Useful Links

- Django Doc : https://docs.djangoproject.com/en/
- Django Rest Framework : http://www.django-rest-framework.org/
- GDPR : https://bohzo.developpez.com/rgpd-guide-pratique-developpeurs/
- Tips : https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
- Python3 : https://learnxinyminutes.com/docs/python3/
- Postico : https://eggerapps.at/postico/ (for Mac)
