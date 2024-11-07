#!/bin/sh
echo ">>> ⏰ waiting for postgres to be ready..."
IP=""
DB_PORT=""
if [[ $REMOTE_DATABASE_IP ]]
then 
    IP=$REMOTE_DATABASE_IP
else
    IP="10.10.80.73"
fi

if [[ $REMOTE_DATABASE_PORT ]]
then 
    DB_PORT=$REMOTE_DATABASE_PORT
else
    DB_PORT=5432
fi

TIMEOUT=30
ELAPSED_TIME=0

# Start a loop to keep trying to connect to the DB until it is successful
# while ! nc -z -v "$IP" "$PORT" ; do
while ! nc -z -v "$IP" "$DB_PORT" ; do
    # Add 10 to the ELAPSED_TIME variable
    ELAPSED_TIME=$(($ELAPSED_TIME + 10))
    # If the timeout has been reached, exit the script with an error code
    if [ "$ELAPSED_TIME" -ge "$TIMEOUT" ]; then
        echo ">>> 😠 not waiting anymore, fix that remote db server..."
        exit 1
    fi
    echo ">>> 😐 still waiting for remote production database on $IP:$DB_PORT..."
    # Sleep for 10 seconds
    sleep 10
done

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

pipenv run build

exit 0
