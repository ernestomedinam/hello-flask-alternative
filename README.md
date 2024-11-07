# hello flask + psql! 🤓
lightly opinionated base template for flask api projects with use case examples for module based folder structure, OOP + SQLAlchemy (ORM) & self documented resource management under REST standards; built for 4GeeksAcademy community & open for all.

recently added docker support!

## how to use 😎

### 🐳 if docker: 
- make sure you have docker engine up & running
- update `.env` file variables
- follow docker instructions (pending), basically `$ docker compose build` & `$ docker compose up` on success

### 🐍 no docker: 
- check python's version is greater or equal than the version in Pipfile
- install project dependencies based on boilerplate's lock file with `$pipenv sync`
- make sure you have a running psql instance & update variables in `.env` file
- create a database on your psql instance named like the value for the corresponding variable in your `.env file`
- run `$pipenv run upgrade` to bring your db up to date with your code
- run `$pipenv run start-chicken-barn` to populate your barn with a couple of chickens
- start dev server with `$pipenv run start`
- check swagger api docs at `/swagger-iu`
- test with `$pipenv run test`
- code away

> need to add new code for a feature? first thing is to build tests based on desired behaviour of your objects when running this feature

> need to mock some objects for testing purposes based on dummy data? create a file for this purpose under the data folder on the current module

> need a new table on your database? update your classes that extend BaseModel and then run `$pipenv run migrate` to create a migration version file with required changes, and then `$pipenv run upgrade` to implement these changes to your database

> need to populate database table with dummy data? use mocking functions & data under the data folder, and add a file under the commands folder to create an app cli command to do so

> need a new endpoint? just add corresponding schema and resource files, and then make sure to register the resource on the current module's routes.py file

## pending 🤪
- update readme to add instructions to change app_name variable and folder name
- update docs on how to use this docker implementation

## notes 📝
> built with python 3.11.4

> note: this is not official 4GeeksAcademy content but I'd be really glad for it to be considered as such, so in spirit it kind of is 😅

> note: please, DO NOT use this boilerplate for your 4Geeks final project nor any of 4Geeks program projects as your TA's will reject them and I will be reprimanded 😐

made with ♥ by mentors @4GeeksAcademy.
