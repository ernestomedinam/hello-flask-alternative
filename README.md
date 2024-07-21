# hello flask + psql! 🤓
lightly opinionated base template for flask api projects with use case examples for app folder structure, OOP + SQLAlchemy (ORM) & self documented resources management under REST standards; built for 4GeeksAcademy students & opaen for all.

## how to use 😎
- check python's version is greater or equal than the version in Pipfile
- install project dependencies base on boilerplate's lock file with `$pipenv sync`
- make sure you have a running psql instance & update variables in .env file
- create a database on your psql instance named like the variable in .env file
- run `$pipenv run upgrade` to bring your db up to date with your code
- run `$pipenv run start-chicken-barn` to populate your barn with a couple of chickens
- start dev server with `$pipenv run start`
- check swagger api docs at `/swagger-iu`
- test with `$pipenv run test`
- code away

> need to adds...

## pending 🤪
- update readme
- update according to changes on reactJS * reactTS boilerplates

## notes 📝
> built with python 3.11.4

> note: this is not official 4GeeksAcademy content but I'd be really glad for it to be considered as such, so in spirit if kind of is 😅

made with ♥ by mentors @4GeeksAcademy.
