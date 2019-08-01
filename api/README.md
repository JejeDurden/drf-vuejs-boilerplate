# How to Git at

### Contributing

+ Make sure your develop branch is up to date ```git checkout develop``` and ```git pull```
+ Create your branch with ```git checkout -b name-of-my-branch```
+ Add, commit and push your changes to your branch
+ Create a pull request to develop on Github
+ Ask for someone to review your code

### Backend install

+ Install postgresql
+ Create altruist database with the settings in settings.py
    + Connect to posgresql
    + ```CREATE DATABASE altruist;```
    + ```\c altruist;```
    + ```CREATE USER altruist WITH PASSWORD 'test';```
    + ```ALTER DATABASE altruist OWNER TO altruist```
    + ```ALTER ROLE altruist SUPERUSER```
+ ```virtualenv env``` and start your virtualenv
+ ```pip3 install -r requirements.txt``` to install python dependencies
+ ```make migrate``` to install database

### Useful Commands

+ ```make reset_db``` to start the drop your current database and set up a new one
+ ```make fake_db``` to populate your database with fake data
+ ```make runserver``` to start the server
+ ```make shell``` to start the console

### Running Tests

+ Make sure your test file match ```test*.py```
+ Make sure your methods start with ```test_```
+ run ```make tests```

### API Documentation

+ run ```make runserver```
+ Go to ```http://localhost:8000/docs/```
+ Click on `authorize` and write ```Bearer someusertoken``` to access protected routes documentation

### Useful Links

+ Freedcamp : https://freedcamp.com/AltruistGroup_f3v/Altruist_6eJ/todos
+ Django Doc : https://docs.djangoproject.com/en/2.1/
+ Django Rest Framework : http://www.django-rest-framework.org/
+ Altruist Wiki : https://github.com/hel-hadi/Altruist/wiki
+ GDPR : https://bohzo.developpez.com/rgpd-guide-pratique-developpeurs/
+ Tips : https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
+ Python3 : https://learnxinyminutes.com/docs/python3/
+ Postico : https://eggerapps.at/postico/ (for Mac)
