#!/bin/sh
echo ">>> ⏰ waiting for postgres to be ready..."

while ! nc -z app_name_db 5432 ; do sleep 10 ; done ;

echo ">>> 🐘 postgresql started..."

if [ ! -d "./migrations" ]
then
    echo ">>> 📂 creating migrations folder..."
    pipenv run init
fi

echo ">>> 🔍 building new migrations..."
pipenv run migrate
echo ">>> 💼 migrating & upgrading db..."
pipenv run upgrade

echo ">>> 💾 db ready... "
echo ">>> 🚀 launching app!"

pipenv run start

exit 0
