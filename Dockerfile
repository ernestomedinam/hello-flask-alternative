FROM python:3.11.4-alpine

# create nonroot user to eventually run container
# update <username> with desired user name, e.g.: e-shell
# needs to match one in .env file...
RUN adduser --no-create-home --system <username>
WORKDIR /app
RUN apk update
RUN apk add build-base mariadb-dev mariadb-client postgresql-dev libffi-dev
RUN apk add jpeg-dev
RUN pip install pipenv

COPY ./Pipfile ./Pipfile.lock /app/

RUN echo "pipenv about to sync..."
RUN pipenv sync --dev --clear

COPY . /app/
EXPOSE 5000
